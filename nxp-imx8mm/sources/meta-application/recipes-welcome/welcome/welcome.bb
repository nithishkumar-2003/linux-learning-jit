SUMMARY = "Calculator application"
DESCRIPTION = "A simple terminal-based calculator for i.MX8MM"
LICENSE = "CLOSED"

SRC_URI = "file://welcome.c"

S = "${WORKDIR}"

do_compile() {
    ${CC} ${CFLAGS} ${LDFLAGS} -o welcome welcome.c
}

do_install() {
    install -d ${D}/home/root/
    install -m 0755 ${S}/welcome ${D}/home/root/welcome
}

FILES:${PN} += "/home/root/welcome"

                                  
