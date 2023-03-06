# Appdome Android Fuse&Sign action

An action for fuse and sign you android vanilla application with Appdome.

# Usage

See [action.yml](action.yml)

```yaml
# "AUTO_SIGNING" - Android:
steps:
- name: Appdome build-2secure
  uses: Appdome/github_build-2secure@1.0
  with:
    APP_FILE: "# none_protected_application can be pass as path/on/repository OR https://download_link"
    FUSION_SET_ID: "Appdome Fusion Set_Id Android/iOS"
    SIGN_OPTIONS: "AUTO_SIGNING"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    KEYSTORE_FILE: ${{secrets.KEYSTORE}}
    KEYSTORE_PASSWORD: ${{secrets.KEYSTORE_PASSWORD}}
    KEYSTORE_ALIAS: ${{secrets.KEYSTORE_ALIAS}}
    KEYSTORE_KEY_PASSWORD: ${{secrets.KEYSTORE_KEY_PASS}}
    
# "AUTO_SIGNING" - iOS:
steps:
- name: Appdome build-2secure
  uses: Appdome/github_build-2secure@1.0
  with:
    APP_FILE: "# none_protected_application can be pass as path/on/repository OR https://download_link"
    FUSION_SET_ID: "Appdome Fusion Set_Id Android/iOS"
    SIGN_OPTIONS: "AUTO_SIGNING"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    KEYSTORE_FILE: ${{secrets.KEYSTORE}}
    KEYSTORE_PASSWORD: ${{secrets.KEYSTORE_PASSWORD}}
    ENTITLEMENTS_FILE: "path/on/repository" "path/on/repository" ... 
                        OR “https download link” “https download link” ....
                        OR ${{secrets.ENTITLEMENTS_BASE64}}
    MOBILE_PROVISION_PROFILE_FILE: "path/on/repository" "path/on/repository" ...
                                    OR “https download link” “https download link” ....
                                    OR ${{secrets.PROVISION_PROFILE_BASE64}}

# Private Signing option:
steps:
uses: nirappdome/appdome_android_action@1.0
with:
  android_vanilla_file: "Https download link OR path to vanilla file on your repository"
  Fusion_set_id: "Appdome fusion set id"
  sign_options: "Private_Signing"
  signing_fingerprint: "SHA1 signing fingerprint"
  appdome_key: ${{secrets.APPDOME_API_KEY}}
  google_play_signing: true/false
  sign_overrides: "Https download link OR path to sign_overrides.json file on your repository OR delete the input if no need "


# Auto-Dev Private Signing option:
steps:
uses: nirappdome/appdome_android_action@1.0
with:
  android_vanilla_file: "Https download link OR path to vanilla file on your repository"
  Fusion_set_id: "Appdome fusion set id"
  sign_options: "Auto_Dev_Private_Signing"
  signing_fingerprint: "SHA1 signing fingerprint"
  appdome_key: ${{secrets.APPDOME_API_KEY}}
  google_play_signing: true
```
