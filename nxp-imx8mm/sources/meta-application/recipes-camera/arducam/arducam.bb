SUMMARY = "Build and install Arducam application for OV5642 on i.MX8M"
DESCRIPTION = "User-space application for interfacing Arducam OV5642 camera using GPIO, SPI, and I2C"
LICENSE = "CLOSED"
SECTION = "camera"
PR = "r0"

SRC_URI = "file://Makefile \
           file://src/"

S = "${WORKDIR}"
DEPENDS += "libgpiod"
# Enable pkgconfig support if using pkg-config based detection
inherit pkgconfig

do_compile() {
    make
}

do_install() {
    install -d ${D}/home/root/
    install -m 0755 ${S}/build/arducam_app ${D}/home/root/arducam_app
}

FILES:${PN} += "/home/root/arducam_app"
