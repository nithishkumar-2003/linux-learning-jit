SUMMARY = "Raspberry Pi configuration files"
LICENSE = "CLOSED"
DESCRIPTION = "Configure Raspberry Pi settings via config.txt"
PR = "r0"

SRC_URI = "file://config.txt"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${sysconfdir}/
    install -m 0644 ${WORKDIR}/config.txt ${D}${sysconfdir}/
}
