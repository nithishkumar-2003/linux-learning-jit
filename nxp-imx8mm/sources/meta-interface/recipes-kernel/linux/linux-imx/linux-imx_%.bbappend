#LICENSE = "GPL-2.0-only"

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

SRC_URI += "file://imx8mm-adv7533.dtsi file://hdmi.config" 

DEPENDS += "dtc-native"

KCONFIG_DEFCONFIG = "${WORKDIR}/defconfig"                                                             KERNEL_CONFIG_FRAGMENTS += "file://hdmi.config"


