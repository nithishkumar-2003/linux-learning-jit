SUMMARY = "Modern Python interface for Raspberry Pi cameras using libcamera"
HOMEPAGE = "https://github.com/raspberrypi/picamera2"
LICENSE = "BSD-2-Clause"
LIC_FILES_CHKSUM = "file://LICENSE;md5=6541a38108b5accb25bd55a14e76086d"

SRC_URI = "git://github.com/raspberrypi/picamera2.git;protocol=https;branch=main"

SRCREV = "63f3be10e317c4b4b0a93e357d7db18fe098e9d4"

S = "${WORKDIR}/git"

inherit setuptools3 python3-dir

RDEPENDS:${PN} += " \
    python3-numpy \
    python3-prctl \
    python3-pyqt5 \
    python3-libcamera \
    "

BB_NO_NETWORK = "0"

