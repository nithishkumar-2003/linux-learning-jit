#!/bin/bash
set -e

# 1️⃣ Update system and install dependencies
sudo apt update
sudo apt install -y \
  build-essential cmake git meson ninja-build pkg-config \
  libjpeg-dev libtiff-dev libpng-dev libavcodec-dev libavformat-dev \
  libavutil-dev libavdevice-dev libexif-dev libboost-program-options-dev \
  qt6-base-dev gstreamer1.0-plugins-base python3-pip python3-yaml python3-jinja2 python3-ply

# 2️⃣ Install Python modules for Meson builds
sudo apt install python3-ply python3-jinja2 python3-yaml

# 3️⃣ Clone or update libcamera
cd ~
#if [ ! -d libcamera ]; then
#  git clone https://git.linuxtv.org/libcamera.git
#fi
cd libcamera
git fetch --all
git checkout v0.7.0   # Pi 5 supported release
rm -rf build
meson setup build
meson compile -C build -j$(nproc)
sudo meson install -C build
sudo ldconfig

# 4️⃣ Clone or update rpicam-apps

# 5️⃣ Verify installation
echo "Verification:"
rpicam-hello --version
