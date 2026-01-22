#!/bin/bash
# Script لإعداد بيئة Android تلقائياً

echo "Setting up Android environment for Buildozer..."

# تعيين متغيرات البيئة
export ANDROID_HOME="/usr/local/lib/android/sdk"
export ANDROID_SDK_ROOT="$ANDROID_HOME"
export ANDROID_NDK_HOME="$ANDROID_HOME/ndk/25.2.9519653"
export ANDROID_NDK="$ANDROID_NDK_HOME"
export ANDROID_NDK_ROOT="$ANDROID_NDK_HOME"

# تحديث PATH
export PATH="$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_NDK_HOME"

# التأكد من وجود NDK
if [ ! -d "$ANDROID_NDK_HOME" ]; then
    echo "❌ Android NDK not found at $ANDROID_NDK_HOME"
    exit 1
else
    echo "✅ Android NDK found: $ANDROID_NDK_HOME"
fi

echo "Environment setup complete!"
