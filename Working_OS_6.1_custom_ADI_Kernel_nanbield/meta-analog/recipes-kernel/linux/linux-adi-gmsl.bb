DESCRIPTION = "ADI Linux kernel with GMSL support for Raspberry Pi 4"
LICENSE = "CLOSED"

inherit kernel

DEPENDS += "linux-firmware"
RDEPENDS:${PN} += "linux-firmware"

# Make this kernel available as virtual/kernel
PROVIDES = "linux-adi-gmsl virtual/kernel"

SRC_URI = "git://github.com/analogdevicesinc/linux.git;branch=gmsl/rpi-6.1.y;protocol=https"
SRCREV = "${AUTOREV}"

PV = "6.1+adi-gmsl"
S = "${WORKDIR}/git"

KCONFIG_MODE = "alldefconfig"
KBUILD_DEFCONFIG = "adi_gmsl_defconfig"

# -------------------------------------------------------------------
# Configure: Use ADI defconfig
# -------------------------------------------------------------------
do_configure:prepend() {
    cp ${S}/arch/arm64/configs/${KBUILD_DEFCONFIG} ${B}/.config
}

# -------------------------------------------------------------------
# Compile: Build kernel Image, DTBs, and overlays
# -------------------------------------------------------------------
do_compile:append() {
    # Build kernel Image
    oe_runmake ARCH=arm64 -C ${S} O=${B} Image

    # Build DTBs
    oe_runmake ARCH=arm64 -C ${S} O=${B} dtbs

    # Build overlays if dtbo target exists
    if oe_runmake -C ${S} O=${B} help | grep -q dtbo; then
        oe_runmake ARCH=arm64 -C ${S} O=${B} dtbo
    fi
}


#-------------------------------------------------------------------------
# Python to add overlays
# Working to get overlays/gmsl.dtbo like all .dtbo in txt file in build directory
# /home/jasminpoc/Analog_OS/custom_os/nanbield/poky/build/tmp/work/raspberrypi4_64-poky-linux/linux-adi-gmsl/6.1+adi-gmsl/build/arch/arm64/boot/dts/overlays/overlays_list.txt
# Working 
#-------------------------------------------------------------------------
#python __anonymous () {
#    import os
#
#    build_dir = d.getVar('B')
#    overlay_dir = os.path.join(build_dir, 'arch/arm64/boot/dts/overlays')
#
#    if os.path.exists(overlay_dir):
#        overlays = [f"overlays/{f}" for f in os.listdir(overlay_dir) if f.endswith(".dtbo") or f.endswith(".dtb")]
#        overlays.sort()
#
#        overlays_str = ' \\\n'.join(overlays)
#        content = f'RPI_KERNEL_DEVICETREE_OVERLAYS ?= " \\\n{overlays_str} \\\n"\n'
#
#        output_file = os.path.join(overlay_dir, 'overlays_list.txt')
#        with open(output_file, 'w') as f:
#            f.write(content)
#
#        # Don't set any variable, just write the file
#}


# -------------------------------------------------------------------
# Install: Kernel Image, DTBs, and overlays
# -------------------------------------------------------------------

do_install:append() {
    # Create boot directories inside the install directory
    install -d ${D}/boot
	install -d ${D}/boot/overlays

    # Install kernel Image
    install -m 0644 ${B}/arch/arm64/boot/Image ${D}/boot/

    # Install each device tree blob (.dtb)
    for dtb in ${KERNEL_DEVICETREE}; do
        install -m 0644 ${B}/arch/arm64/boot/dts/${dtb} ${D}/boot/
    done

    # Install all overlays (.dtbo)
    for dtbo in ${B}/arch/arm64/boot/dts/overlays/*.dtbo; do
        install -m 0644 ${dtbo} ${D}/boot/overlays/
    done

}


# -------------------------------------------------------------------
# Deploy
# -------------------------------------------------------------------

do_deploy:append() {

    # Create bootfiles and overlays directories
    install -d ${DEPLOYDIR}/bootfiles

    # Copy kernel Image
    install -m 0644 ${B}/arch/arm64/boot/Image ${DEPLOYDIR}/

    # Copy DTBs, skipping if file already exists
    if [ -d ${B}/arch/arm64/boot/dts/broadcom ]; then
        for dtb in ${B}/arch/arm64/boot/dts/broadcom/*.dtb; do
            if [ -f "$dtb" ]; then
                filename=$(basename "$dtb")
                if [ ! -f "${DEPLOYDIR}/bootfiles/$filename" ]; then
                    cp -v "$dtb" ${DEPLOYDIR}/
                else
                    echo "Skipping $filename, already exists in deploy directory."
                fi
            fi
        done
    fi

}


# -------------------------------------------------------------------
# Packaging
# -------------------------------------------------------------------

FILES:${PN} += "/boot/overlays/ /boot/overlays/*.dtbo /boot/Image /boot/*.dtb /boot/config.txt"









