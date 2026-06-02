FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"
 
SRC_URI = " \
    git://github.com/raspberrypi/libcamera-apps.git;protocol=https;branch=main \
    file://0001-utils-version.py-use-usr-bin-env-in-shebang.patch \
"
 
PV = "1.2.1+git${SRCPV}"
SRCREV = "7e4d3d71867f60f5398687180972798baad85f1b"
