DESCRIPTION = "Recipe to install two analog video_cfg.sh and qv4l2.desktop in desktop"
LICENSE = "CLOSED"

SRC_URI = " \
    file://qv4l2.desktop \
    file://video_cfg.sh \
"

S = "${WORKDIR}"

do_install() {
    install -d ${D}/home/root/Desktop
    install -m 0755 ${WORKDIR}/video_cfg.sh ${D}/home/root/Desktop/video_cfg.sh
    install -m 0755 ${WORKDIR}/qv4l2.desktop ${D}/home/root/Desktop/qv4l2.desktop
}

FILES:${PN} += "/home/root/Desktop/video_cfg.sh /home/root/Desktop/qv4l2.desktop"

# Ensure bash is available since video_cfg.sh uses #!/bin/bash
RDEPENDS:${PN} += "bash"
