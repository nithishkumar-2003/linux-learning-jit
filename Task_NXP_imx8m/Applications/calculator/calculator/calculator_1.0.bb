SUMMARY = "Calculator application"
DESCRIPTION = "A simple terminal-based calculator for i.MX8MM"
LICENSE = "CLOSED"

SRC_URI = "file://calculator/"

S = "${WORKDIR}/calculator"

do_compile() {
    make
}

do_install() {
    install -d ${D}/home/root/Desktop
    install -m 0755 ${S}/calculator ${D}/home/root/Desktop/calculator
}

FILES:${PN} += "/home/root/Desktop/calculator"
