DESCRIPTION = "Arducam Mega SDK and CLI tool"
LICENSE = "CLOSED"
SRC_URI = "git://github.com/ArduCAM/Arducam_Mega.git;protocol=https;branch=main"
S = "${WORKDIR}/git/RaspberryPi/ArducamMega_C"
DEPENDS = "libserialport"
inherit pkgconfig

do_compile() {
    oe_runmake
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 arducam_demo ${D}${bindir}/arducam_demo
}
