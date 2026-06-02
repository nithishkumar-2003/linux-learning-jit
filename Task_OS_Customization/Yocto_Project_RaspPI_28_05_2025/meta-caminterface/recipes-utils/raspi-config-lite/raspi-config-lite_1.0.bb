DESCRIPTION = "Minimal raspi-config-like interface for Yocto"
LICENSE = "CLOSED"
#LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835c1a4b4f9dede8b7ed063ef76b16d"

RDEPENDS:${PN} += "bash"
SRC_URI = "file://raspi-config-lite"                                                                  
S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}
    if [ -f ${WORKDIR}/raspi-config-lite ]; then
        install -m 0755 ${WORKDIR}/raspi-config-lite ${D}${bindir}/raspi-config-lite
    else
        bbwarn "Source file raspi-config-lite not found!"
    fi
}

