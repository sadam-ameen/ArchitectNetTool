[app]
title = Architect Net
package.name = arch.stealth.injector
package.domain = org.architect
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3,kivy,requests,urllib3,openssl
orientation = portrait
fullscreen = 0

# ⭐ إعدادات أندرويد مهمة
osx.python_version = 3
osx.kivy_version = 2.3.0
android.api = 33  # ⭐ تحديث API
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.ndk_api = 21

# ⭐ الصلاحيات
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# ⭐ المعماريات
android.archs = arm64-v8a, armeabi-v7a

# ⭐ إعدادات إضافية
android.allow_backup = True
android.gradle_dependencies = 'com.android.support:multidex:1.0.3'
p4a.branch = develop

# ⭐ إعدادات البناء
[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
