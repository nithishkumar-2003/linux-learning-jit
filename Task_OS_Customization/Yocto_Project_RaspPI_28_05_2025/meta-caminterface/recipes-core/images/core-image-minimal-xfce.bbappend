# Append to IMAGE_INSTALL to include NetworkManager and necessary components
IMAGE_INSTALL += "networkmanager networkmanager-wifi wpa-supplicant"

# Function to enable NetworkManager for systemd
enable_networkmanager() {
    echo "Enabling NetworkManager for systemd"
    mkdir -p ${IMAGE_ROOTFS}/etc/systemd/system/multi-user.target.wants
    ln -sf /lib/systemd/system/NetworkManager.service ${IMAGE_ROOTFS}/etc/systemd/system/multi-user.target.wants/NetworkManager.service
}

# Add this function to the post-processing steps
ROOTFS_POSTPROCESS_COMMAND += "enable_networkmanager; "

