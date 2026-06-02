
SUMMARY = "ArduCAM application"
DESCRIPTION = "A simple ArduCAM application for Raspberry Pi"
LICENSE = "CLOSED"

SRC_URI = "file://SPI_Camera/"

S = "${WORKDIR}/SPI_Camera"

do_compile() {
    make
}

do_install() {
    install -d ${D}/home/root/Desktop
    install -m 0755 ${S}/run_Arducam_Demo ${D}/home/root/Desktop/run_Arducam_Demo
}

FILES:${PN} += "/home/root/Desktop/run_Arducam_Demo"


#    install -d ${D}${bindir}
#    install -m 0755 ${S}/run_Arducam_Demo ${D}${bindir}/run_Arducam_Demo

#install -d ${D}/usr/bin
#install -m 0755 ${WORKDIR}/run_Arducam_Demo ${D}/usr/bin/run_Arducam_Demo

#FILES:${PN} = " /home/root/welcome.sh"  
