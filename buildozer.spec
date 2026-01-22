[app]
title = Architect Net
package.name = stealthinjector
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0

# ⭐ المتطلبات الأساسية فقط
requirements = python3,kivy==2.3.0,requests

orientation = portrait
fullscreen = 0
log_level = 2

# ⭐ إعدادات أندرويد مبسطة
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 23b
android.ndk_path = 
android.sdk_path = 
android.p4a_dir = 

# ⭐ الصلاحيات
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# ⭐ إعدادات البناء
android.arch = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

# ⭐ إعدادات لتقليل استخدام الذاكرة
android.skip_update = False
p4a.branch = master
p4a.local_recipes = 
