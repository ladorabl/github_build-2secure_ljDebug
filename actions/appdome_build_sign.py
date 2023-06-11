import argparse
import glob
import sys
import os
import subprocess


def parse_args():
    """
    Command line arguments
    :return: args parser
    """
    parser = argparse.ArgumentParser("Appdome Build-2secure args")
    parser.add_argument("-sign", dest='sign_option', required=True,
                        help="AUTO_SIGNING OR PRIVATE_SIGNING OR AUTO_DEV_SIGNING")
    parser.add_argument("-api_key", dest='appdome_api_key', required=True,
                        help='Appdome API key')
    parser.add_argument("-fs", dest='fusion_set', required=True,
                        help="Appdome fusion set")
    parser.add_argument("-kp", dest='keystore_pass', required=False,
                        help="keystore password", default="None")
    parser.add_argument("-ka", dest='keystore_alias', required=False,
                        help="keystore alias", default="None")
    parser.add_argument("-kkp", dest='keystore_key_pass', required=False,
                        help="keystore key pass", default="None")
    parser.add_argument("-team_id", dest='team_id', required=False,
                        help="team id", default="None")
    parser.add_argument("-google-play-signing", dest='google_play_signing', required=False,
                        help="google play signing", default="false")
    parser.add_argument("-signing_fingerprint", dest='signing_fingerprint', required=False,
                        help="signing_fingerprint", default="None")
    parser.add_argument("-bl", dest='build_with_logs', required=True,
                        help="Do you want to build with logs?")
    return parser.parse_args()


sys.path.extend([os.path.join(sys.path[0], '../..')])

new_env = os.environ.copy()

new_env["APPDOME_CLIENT_HEADER"] = "Github/1.0.0"
new_env["APPDOME_SERVER_BASE_URL"] = "https://staging.appdome.com/"

args = parse_args()


def main():
    os.makedirs('./output', exist_ok=True)
    sign_option = args.sign_option
    appdome_api_key = args.appdome_api_key
    fusion_set = args.fusion_set
    keystore_pass = args.keystore_pass
    extensions = ["*.apk", "*.aab", "*.ipa"]
    app_file = [file for extension in extensions for file in glob.glob(f"./files/{extension}")]
    if len(app_file) == 0:
        print("Couldn't locate non_protected app file on ./files/non_protected.*")
        exit(1)
    app_file = app_file[0]
    app_name = os.path.basename(app_file) 
    app_ext = app_name[-4:]
    keystore_file = glob.glob('./files/cert.*')
    build_with_logs = "-bl" if args.build_with_logs != "false" else ""
    team_id = f"--team_id {args.team_id}" if args.team_id != "None" else ""
    provision_profiles = f"--provisioning_profiles {' '.join(glob.glob('./files/provision_profiles/*'))}" \
        if os.path.exists("./files/provision_profiles") else ""
    entitlements = f"--entitlements {' '.join(glob.glob('./files/entitlements/*'))}" \
        if os.path.exists("./files/entitlements") else ""
    if sign_option == 'SIGN_ON_APPDOME':
        keystore_alias = f"--keystore_alias {args.keystore_alias}" if args.keystore_alias != "None" else ""
        keystore_key_pass = f"--key_pass {args.keystore_key_pass}" if args.keystore_key_pass != "None" else ""

        cmd = f"python3 appdome/appdome-api-python/appdome_api.py -key {appdome_api_key} --app {app_file} " \
              f"--sign_on_appdome -fs {fusion_set} {team_id} --keystore {keystore_file[0]} " \
              f"--keystore_pass {keystore_pass} --output ./output/Appdome_secured_app{app_ext} " \
              f"--certificate_output ./output/certificate.pdf {keystore_alias} {keystore_key_pass} " \
              f"{provision_profiles} {entitlements} {build_with_logs}"

        subprocess.check_output([i for i in cmd.split(" ") if i != ''], env=new_env)

    elif sign_option == 'PRIVATE_SIGNING':
        google_play_signing = f"--google_play_signing" if args.google_play_signing != "false" else ""
        signing_fingerprint = f"--signing_fingerprint {args.signing_fingerprint}" if args.signing_fingerprint != "None" else ""

        cmd = f"python3 appdome/appdome-api-python/appdome_api.py -key {appdome_api_key} " \
              f"--app {app_file} --private_signing -fs {fusion_set} {team_id} " \
              f"--output ./output/Appdome_secured_app{app_ext} --certificate_output ./output/certificate.pdf " \
              f"{google_play_signing} {signing_fingerprint} {provision_profiles} {build_with_logs}"

        subprocess.check_output([i for i in cmd.split(" ") if i != ''], env=new_env)

    elif sign_option == 'AUTO_DEV_SIGNING':
        google_play_signing = f"--google_play_signing" if args.google_play_signing != "false" else ""
        signing_fingerprint = f"--signing_fingerprint {args.signing_fingerprint}" if args.signing_fingerprint != "None" else ""

        cmd = f"python3 appdome/appdome-api-python/appdome_api.py -key {appdome_api_key} " \
              f"--app {app_file} --auto_dev_private_signing -fs {fusion_set} {team_id} " \
              f"--output ./output/Appdome_secured_app{app_ext} --certificate_output ./output/certificate.pdf " \
              f"{google_play_signing} {signing_fingerprint} {provision_profiles} {entitlements} {build_with_logs}"
        subprocess.check_output([i for i in cmd.split(" ") if i != ''], env=new_env)
    else:
        print("Signing option not found!\nValid signs: AUTO_SIGNING/PRIVATE_SIGNING/AUTO_DEV_SIGNING")


if __name__ == '__main__':
    main()
