FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI:append = " file://config.txt"

do_install:append() {
    install -m 0644 ${WORKDIR}/config.txt ${D}${BOOTFILES_DIR}/config.txt
}

