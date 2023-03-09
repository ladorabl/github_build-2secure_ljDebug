import glob
import sys
import os
import subprocess

# sign_option = argv[0]
# appdome_api_key = argv[1]
# fusion_set = argv[2]
# keystore_pass = argv[3]
# keystore_alias = argv[4]
# keystore_key_pass = argv[5]
# team_id = argv[6]
# google-play-signing = argv[7]
# signing_fingerprint = argv[8]
sys.path.extend([os.path.join(sys.path[0], '../..')])

new_env = os.environ.copy()
new_env["APPDOME_CLIENT_HEADR"] = "Github/1.0.0"

def main(argv):
    os.mkdir('./output')
    sign_option = argv[0]
    appdome_api_key = argv[1]
    fusion_set = argv[2]
    keystore_pass = argv[3]
    app_file = glob.glob('./files/non_protected.*')
    app_extension = app_file[0][-4:]
    keystore_file = glob.glob('./files/cert.*')
    team_id = f"--team_id {argv[6]}" if argv[6] != "!" else ""
    provision_profiles = f"--provisioning_profiles {' '.join(glob.glob('./files/provision_profiles/*'))}" \
        if os.path.exists("./files/provision_profiles") else ""
    entitlements = f"--entitlements {' '.join(glob.glob('./files/entitlements/*'))}" \
        if os.path.exists("./files/entitlements") else ""
    if sign_option == 'AUTO_SIGNING':
        keystore_alias = f"--keystore_alias {argv[4]}" if argv[4] != "!" else ""
        keystore_key_pass = f"--key_pass {argv[5]}" if argv[5] != "!" else ""

        cmd = f"sudo python3 appdome/appdome-api-python/appdome_api.py -key {appdome_api_key} --app {app_file[0]} " \
              f"--sign_on_appdome -fs {fusion_set} {team_id} --keystore {keystore_file[0]} " \
              f"--keystore_pass {keystore_pass} --output ./output/appdome_protected{app_extension} " \
              f"--certificate_output ./output/certificate.pdf {keystore_alias} {keystore_key_pass} " \
              f"{provision_profiles} {entitlements}"

        subprocess.check_output([i for i in cmd.split(" ") if i != ''], env=new_env)

    elif sign_option == 'PRIVATE_SIGNING':
        google_play_signing = f"--google_play_signing" if argv[7] != "false" else ""
        signing_fingerprint = f"--signing_fingerprint {argv[8]}" if argv[8] != "!" else ""

        cmd = f"sudo python3 appdome/appdome-api-python/appdome_api.py -key {appdome_api_key} " \
              f"--app {app_file[0]} --private_signing -fs {fusion_set} {team_id} " \
              f"--output ./output/appdome_protected{app_extension} --certificate_output ./output/certificate.pdf " \
              f"{google_play_signing} {signing_fingerprint} {provision_profiles}"

        subprocess.check_output([i for i in cmd.split(" ") if i != ''], env=new_env)

    elif sign_option == 'AUTO_DEV_SIGNING':
        google_play_signing = f"--google_play_signing" if argv[7] else ""
        signing_fingerprint = f"--signing_fingerprint {argv[8]}" if argv[8] != "!" else ""
        
        cmd = f"sudo python3 appdome/appdome-api-python/appdome_api.py -key {appdome_api_key} " \
              f"--app {app_file[0]} --auto_dev_private_signing -fs {fusion_set} {team_id} " \
              f"--output ./output/appdome_protected{app_extension} --certificate_output ./output/certificate.pdf " \
              f"{google_play_signing} {signing_fingerprint} {provision_profiles} {entitlements}"
        subprocess.check_output([i for i in cmd.split(" ") if i != ''], env=new_env)
    else:
        print("Signing option not found!\nValid signs: AUTO_SIGNING/PRIVATE_SIGNING/AUTO_DEV_SIGNING")


if __name__ == '__main__':
    main(sys.argv[1:])
