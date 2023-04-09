# Appdome Android Fuse&Sign action

Actions are reusable snippets of code that help automate repeated processes, speed up project setup, and make it easy to integrate with third-party tools.

Now you can easily secure and customize your mobile apps on GitHub using the Appdome GitHub Actions. No coding or technical expertise is required. Automate the process of adding security features such as encryption, biometric authentication, and more to your mobile apps. Additionally, sign your app with your own enterprise certificate for added flexibility and control. Get the flexibility and control you need to secure and customize your mobile apps with the Appdome GitHub action.


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
    SIGN_OPTIONS: "SIGN_ON_APPDOME"
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
    FUSION_SET_ID: "Appdome Fusion Set_Id iOS"
    SIGN_OPTIONS: "SIGN_ON_APPDOME"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    KEYSTORE_FILE: ${{secrets.KEYSTORE}}
    KEYSTORE_PASSWORD: ${{secrets.KEYSTORE_PASSWORD}}
    ENTITLEMENTS_FILE: "path/on/repository" "path/on/repository" ... 
                        OR “https download link” “https download link” ....
                        OR ${{secrets.ENTITLEMENTS_BASE64}}
    MOBILE_PROVISION_PROFILE_FILE: "path/on/repository" "path/on/repository" ...
                                    OR “https download link” “https download link” ....
                                    OR ${{secrets.PROVISION_PROFILE_BASE64}}

# "PRIVATE_SIGNING" - Android:
steps:
- name: Appdome build-2secure
  uses: Appdome/github_build-2secure@1.0
  with:
    APP_FILE: "# none_protected_application can be pass as path/on/repository OR https://download_link"
    FUSION_SET_ID: "Appdome Fusion Set_Id Android"
    SIGN_OPTIONS: "PRIVATE_SIGNING"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    SIGN_FINGERPRINT: ${{secrets.APPDOME_SIGN_FINGERPRINT}}
    GOOGLE-PLAY-SIGNING: "true" -Optional


# "PRIVATE_SIGNING" - iOS:
steps:
- name: Appdome build-2secure
  uses: Appdome/github_build-2secure@1.0
  with:
    APP_FILE: "# none_protected_application can be pass as path/on/repository OR https://download_link"
    FUSION_SET_ID: "Appdome Fusion Set_Id iOS"
    SIGN_OPTIONS: "PRIVATE_SIGNING"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    KEYSTORE_FILE: ${{secrets.KEYSTORE}}
    KEYSTORE_PASSWORD: ${{secrets.KEYSTORE_PASSWORD}}
    MOBILE_PROVISION_PROFILE_FILE: "path/on/repository" "path/on/repository" ...
                                    OR “https download link” “https download link” ....
                                    OR ${{secrets.PROVISION_PROFILE_BASE64}}
                                    
# "AUTO_DEV_SIGNING" - Android:
steps:
- name: Appdome build-2secure
  uses: Appdome/github_build-2secure@1.0
  with:
    APP_FILE: "# none_protected_application can be pass as path/on/repository OR https://download_link"
    FUSION_SET_ID: "Appdome Fusion Set_Id Android"
    SIGN_OPTIONS: "AUTO_DEV_SIGNING"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    SIGN_FINGERPRINT: ${{secrets.APPDOME_SIGN_FINGERPRINT}}
    GOOGLE-PLAY-SIGNING: "true" -Optional

# "AUTO_DEV_SIGNING" - iOS:
steps:
- name: Appdome build-2secure
  uses: Appdome/github_build-2secure@1.0
  with:
    APP_FILE: "# none_protected_application can be pass as path/on/repository OR https://download_link"
    FUSION_SET_ID: "Appdome Fusion Set_Id iOS"
    SIGN_OPTIONS: "AUTO_DEV_SIGNING"
    APPDOME_API_TOKEN: ${{secrets.APPDOME_API_KEY}}
    MOBILE_PROVISION_PROFILE_FILE: "path/on/repository" "path/on/repository" ...
                                    OR “https download link” “https download link” ....
                                    OR ${{secrets.PROVISION_PROFILE_BASE64}}
    ENTITLEMENTS_FILE: "path/on/repository" "path/on/repository" ... 
                        OR “https download link” “https download link” ....
                        OR ${{secrets.ENTITLEMENTS_BASE64}}
```
