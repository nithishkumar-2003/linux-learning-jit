SUMMARY = "Python interface for the Raspberry Pi Camera using libcamera"
DESCRIPTION = "Picamera2 is a Python library that provides an easy interface to the Raspberry Pi Camera using libcamera."
HOMEPAGE = "https://github.com/raspberrypi/picamera2"
LICENSE = "CLOSED"
#LIC_FILES_CHKSUM = "file://LICENSE;md5=<insert-md5sum>"

SRC_URI = "file://."

S = "${WORKDIR}"

inherit setuptools3

# Runtime dependencies - adjust as needed based on actual dependencies
RDEPENDS:${PN} += " \
    python3 \
    python3-numpy \
"

# No manual do_install needed; setuptools3 handles install

