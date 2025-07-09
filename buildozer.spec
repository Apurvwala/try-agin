[app]

# (str) Title of your application
title = FaceApp Attendance System

# (str) Package name
package.name = faceappattendance

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yourcompany

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Add necessary libraries. face_recognition is complex due to dlib and might require specific handling.
# python3==3.9.5 is a common stable version for Kivy builds.
requirements = python3==3.9.5,kivy==2.1.0,flask,flask-cors,numpy,Pillow,requests,face_recognition

# (str) Main application file
main.py = main.py

# (list) List of target machine for android/ios/desktop (comma separated)
target = android

# (list) Android API levels
# android.api = 27 # You can try a higher API level if needed, but 27 is often stable.
# android.minapi = 21
# android.maxapi = 27

# (list) Android permissions
# CAMERA is essential for face recognition.
# INTERNET for Flask server and Google Forms/Email.
# WRITE_EXTERNAL_STORAGE/READ_EXTERNAL_STORAGE for saving known faces.
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (bool) Enable or disable Android's fullscreen mode
android.fullscreen = True

# (list) Android archs to build for (arm64-v8a is for newer devices, armeabi-v7a for older)
android.archs = arm64-v8a,armeabi-v7a

# (int) The Android SDK will be downloaded in the build process
# if not found, specify here the directory of the Android SDK
# android.sdk_path = /path/to/android-sdk

# (int) The Android NDK will be downloaded in the build process
# if not found, specify here the directory of the Android NDK
# android.ndk_path = /path/to/android-ndk

# (bool) If you want to use the Google Play Store, you might need to sign your APK.
# For debugging, keep it False.
# android.release = False

# (str) Path to a custom icon file (optional)
# icon.filename = %(source.dir)s/icon.png

# (list) Add your application files and folders to the APK
# Ensure all necessary files like images, JSON config files are included.
source.include_exts = py,png,jpg,json,mp3
source.exclude_dirs = .buildozer, .git, __pycache__

# (str) Log level for the build process (debug, info, warning, error, critical)
log_level = info

# (str) A string that will be displayed in the Android notification bar
# when the application is running in the background
# android.notification_title = FaceApp

# (str) A string that will be displayed in the Android notification bar
# when the application is running in the background
# android.notification_icon = %(source.dir)s/icon.png

# (list) Add additional Java files to be compiled for your app (advanced)
# android.add_libs =

# (list) Add additional Java classes to be compiled for your app (advanced)
# android.add_classes =

# (list) Add additional Java jars to be included in your app (advanced)
# android.add_jars =

# (str) Path to your Java keystore file (for release builds)
# android.release_keystore =

# (str) Password for your Java keystore (for release builds)
# android.release_keystore_pass =

# (str) Alias for your Java keystore (for release builds)
# android.release_keyalias =
