[app]
title = Architect Net
package.name = stealthapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0
log_level = 2

# ⭐⭐⭐ الإعدادات الحاسمة ⭐⭐⭐
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25.2.9519653

android.permissions = INTERNET

android.arch = arm64-v8a
android.accept_sdk_license = True

p4a.branch = master
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
