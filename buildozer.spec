[app]
title = Ahmed Native
package.name = ahmednative
package.domain = org.ahmed
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
requirements = python3==3.11,kivy==https://github.com/kivy/kivy/archive/refs/tags/2.3.1.zip,cython==3.0.11,requests
p4a.branch = develop
