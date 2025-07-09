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
requirements = python3,kivy==2.1.0,flask,flask-cors,numpy,Pillow,requests,git+https://github.com/ageitgey/face_recognition

# (str) Main application file
entrypoint = main.py

# (str) The directory where your main.py and other source files are located.
source.dir = .

# (list) List of target machine for android/ios/desktop (comma separated)
target = android

# (list) Android permissions
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (bool) Enable or disable Android's fullscreen mode
android.fullscreen = True

# (list) Android archs to build for (arm64-v8a is for newer devices, armeabi-v7a for older)
android.archs = arm64-v8a,armeabi-v7a

# (bool) Allow networking (important for Flask apps)
android.allow_networking = True

# (list) Include these file extensions
source.include_exts = py,png,jpg,json,mp3,xml
source.exclude_dirs = .buildozer, .git, __pycache__

# (str) Log level for the build process (debug, info, warning, error, critical)
log_level = info
