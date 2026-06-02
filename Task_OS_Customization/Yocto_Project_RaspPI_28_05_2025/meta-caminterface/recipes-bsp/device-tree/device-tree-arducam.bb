SUMMARY = "Device Tree overlay for Arducam OV5642"
LICENSE = "CLOSED"

SRC_URI = "file://arducam-ov5642-overlay.dts"

DEPENDS += "dtc-native"

S = "${WORKDIR}"

do_compile() {
    ${STAGING_BINDIR_NATIVE}/dtc -@ -I dts -O dtb -o ${S}/arducam-ov5642.dtbo ${S}/arducam-ov5642-overlay.dts
}

do_install() {
    install -d ${D}${sysconfdir}/boot/overlays
    install -m 0644 ${S}/arducam-ov5642.dtbo ${D}${sysconfdir}/boot/overlays/
}

