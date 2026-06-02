DESCRIPTION = "WiringPi library for Raspberry Pi"
HOMEPAGE = "https://github.com/WiringPi/WiringPi"
LICENSE = "LGPLv3"
LIC_FILES_CHKSUM = "file://LICENSE;md5=8dbe3c4fc010b680fa80a56d8a92e8a9"

SRC_URI = "git://github.com/WiringPi/WiringPi.git;branch=master;protocol=https"
SRCREV = "latest"

S = "${WORKDIR}/git"

do_compile() {
    cd ${S}
    ./build
}

do_install() {
    cd ${S}
    # Ensure wiringPi is installed
    install -d ${D}${bindir}
    install -m 755 gpio ${D}${bindir}/gpio
    install -m 755 ./wiringPi/* ${D}${libdir}
}

