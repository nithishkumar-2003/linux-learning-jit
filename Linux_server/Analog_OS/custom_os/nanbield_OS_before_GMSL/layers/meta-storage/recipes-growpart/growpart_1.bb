DESCRIPTION = "growpart utility from cloud-utils"
HOMEPAGE = "https://launchpad.net/cloud-utils"
LICENSE = "CLOSED"
#LIC_FILES_CHKSUM = "file://growpart;endline=10;md5=5f3e6e32b07a4e94c9c0a6e50b21612a"

SRC_URI = "https://git.launchpad.net/cloud-utils/plain/bin/growpart?id=refs/heads/master;downloadfilename=growpart"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/growpart ${D}${bindir}/growpart
}

RDEPENDS:${PN} = "python3 bash util-linux"

