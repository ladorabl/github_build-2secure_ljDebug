import os
import boto3


def main():
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_default_region = 'eu-central-1'
    bucket_name = "appdome-automation-vanilla-apps"
    objects = {
        'aab_app': 'Thomas/FileFinder.aab',
        'apk_app': 'Thomas/TimeCard.apk',
        'keystore_file': 'Thomas/appdome.keystore',
        'ipa_app_1': 'Thomas/FileFinder.ipa',
        'ipa_app_2': 'Thomas/Trends256-iOS16.ipa',
        'certificate_file': 'Thomas/AutomationCert.p12',
        'ipa_1_mobile_provisioning': 'Thomas/Automation.mobileprovision',
        'ipa_1_entitlements': 'Thomas/AutomationEntitlements.plist',
        'ipa_2_mobile_provisioning_1': 'Thomas/Trendsappstoredist.mobileprovision',
        'ipa_2_mobile_provisioning_2': 'Thomas/Trends_watchkit_appstoredist.mobileprovision',
        'ipa_2_mobile_provisioning_3': 'Thomas/Trends_watchkit_extension_appstoredist.mobileprovision',
        'ipa_2_entitlements_1': 'Thomas/main.plist',
        'ipa_2_entitlements_2': 'Thomas/watchkit.plist',
        'ipa_2_entitlements_3': 'Thomas/watchkitextension.plist',
    }

    if aws_access_key_id is None or aws_secret_access_key is None:
        print("Missing required environment variables.")
        exit(1)

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_default_region)

    presigned_urls = {}

    for key, object_key in objects.items():
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_key
            },
            ExpiresIn=3600  # 1 hour
        )
        presigned_urls[key] = presigned_url

    if not os.path.exists("presigned_urls"):
        os.mkdir("presigned_urls")

    for key, url in presigned_urls.items():
        with open(f"presigned_urls/{key}.txt", 'w') as url_file:
            url_file.write(url)


if __name__ == "__main__":
    main()
