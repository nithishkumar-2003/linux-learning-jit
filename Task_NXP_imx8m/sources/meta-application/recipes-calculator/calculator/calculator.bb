SUMMARY = "Calculator application"
DESCRIPTION = "A simple terminal-based calculator for i.MX8MM"
LICENSE = "CLOSED"

SRC_URI = "file://calculator.c"

S = "${WORKDIR}"

do_compile() {
   ${CC} ${CFLAGS} ${LDFLAGS} -o calculator calculator.c
}

do_install() {
    install -d ${D}/home/root/
    install -m 0755 ${S}/calculator ${D}/home/root/calculator
}

FILES:${PN} += "/home/root/calculator"
