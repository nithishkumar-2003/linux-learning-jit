SUMMARY = "Custom welcome message"
LICENSE = "CLOSED"
SRC_URI += "file://welcome.sh"

S = "${WORKDIR}"

do_install() {
    # Install the welcome.sh script in a directory
    install -d ${D}/usr/bin
    install -m 0755 ${WORKDIR}/welcome.sh ${D}/usr/bin/welcome.sh
}

#FILES:${PN} = " /home/root/welcome.sh"
