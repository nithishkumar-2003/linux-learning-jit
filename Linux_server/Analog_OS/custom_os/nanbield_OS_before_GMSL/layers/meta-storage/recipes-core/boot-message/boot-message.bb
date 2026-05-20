DESCRIPTION = "Custom Boot Message Display"
LICENSE = "CLOSED"
SRC_URI = "file://boot-message.c \
           file://boot-message.service"

S = "${WORKDIR}"

do_compile() {
    ${CC} ${CFLAGS} ${LDFLAGS} boot-message.c -o boot_message
}

do_install() {
    install -d ${D}${bindir}
    install -m 0755 boot_message ${D}${bindir}/boot_message

    install -d ${D}${systemd_system_unitdir}
    install -m 0644 ${WORKDIR}/boot-message.service ${D}${systemd_system_unitdir}
}

SYSTEMD_SERVICE_${PN} = "boot-message.service"

inherit systemd

#debug step added 
#python () {
#    bb.warn("systemd_system_unitdir resolves to: %s" % d.getVar("systemd_system_unitdir"))
#}

#FILES_${PN} += "/usr/lib/systemd/system/boot-message.service"
FILES:${PN} += "${systemd_system_unitdir}/boot-message.service"
