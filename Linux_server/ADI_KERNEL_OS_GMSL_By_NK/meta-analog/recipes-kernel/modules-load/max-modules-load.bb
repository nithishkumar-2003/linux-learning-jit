DESCRIPTION = "Load max series kernel modules at boot"
LICENSE = "CLOSED"
SRC_URI = "file://max_modules.conf"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${sysconfdir}/modules-load.d
    install -m 0644 ${WORKDIR}/max_modules.conf ${D}${sysconfdir}/modules-load.d/
}

FILES_${PN} += "${sysconfdir}/modules-load.d/max_modules.conf"

