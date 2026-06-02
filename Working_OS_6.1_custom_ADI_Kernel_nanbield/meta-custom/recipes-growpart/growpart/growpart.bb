DESCRIPTION = "growpart utility from cloud-utils"
HOMEPAGE = "https://launchpad.net/cloud-utils"
LICENSE = "CLOSED"

SRC_URI = "https://git.launchpad.net/cloud-utils/plain/bin/growpart;downloadfilename=growpart"
SRC_URI[sha256sum] = "129fc52cff14669b6ae9e7b31d534ce30a453a8ee3d6d20acbeb61aec73deebf"

S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/growpart ${D}${bindir}/growpart
}

RDEPENDS:${PN} = "python3 bash util-linux"

