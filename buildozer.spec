[app]

# (str) Title of your application
title = TarotAI

# (str) Package name
package.name = tarotai

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tarotai

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = kivy

# (str) Custom source folders for requirements
# Sets custom folder for module `bar` to `foo/bar`.
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements = 

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Indicate if the application should be resizable or not
resizable = 0

# (str) Whether to compile the application or not ('debug', 'release')
compile_mode = release

# (str) Custom source folders for requirements
# Sets custom folder for module `bar` to `foo/bar`.
#requirements.source.kivy = ../../kivy


# Extra configuration options for Android

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 29

# (str) Android NDK version to use
#android.ndk = 19b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Java classes to add as they are found through the static analysis feature (using regexp)
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) Java classes to add directly (use dots for paths, e.g org.test.ClassName)
#android.add_classpath = com/android/vending/billing/IInAppBillingService.aidl

# (str) Path to a custom AndroidManifest.xml file to be used instead of the default one
#android.manifest.custom = ./android/AndroidManifest.xml

# (str) Path to a custom android icon.
#android.icon.custom = ./android/icon.png

# (str) Path to a custom sample configuration file (see folder ./ios/ for examples)
#android.sample_config.custom = ./path/to/config/file

