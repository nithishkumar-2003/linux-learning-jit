LICENSE = "GPL-2.0-only"

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

# Include required source files
SRC_URI += "file://hdmi.config \
            file://imx8mm-evk-hdmi.dts \
            file://hdmi-fragment.dtsi"

DEPENDS += "dtc-native"

#do_compile:prepend() {
#    cp ${WORKDIR}/imx8mm-evk-hdmi.dts ${S}/arch/arm64/boot/dts/freescale/
#}

# Kernel configuration
KCONFIG_DEFCONFIG = "${WORKDIR}/defconfig"
KERNEL_CONFIG_FRAGMENTS += "file://hdmi.config"

# Device tree file to build
KERNEL_DEVICETREE += "freescale/imx8mm-evk-hdmi.dtb"




