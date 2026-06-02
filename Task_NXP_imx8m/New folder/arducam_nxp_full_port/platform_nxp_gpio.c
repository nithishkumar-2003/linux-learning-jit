
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include "platform_nxp_gpio.h"

#define SYSFS_GPIO_DIR "/sys/class/gpio"

void export_gpio(int pin) {
    char buffer[64];
    int fd = open(SYSFS_GPIO_DIR "/export", O_WRONLY);
    if (fd < 0) return;
    snprintf(buffer, sizeof(buffer), "%d", pin);
    write(fd, buffer, strlen(buffer));
    close(fd);
}

void gpio_set_output(int pin) {
    char path[64];
    export_gpio(pin);
    snprintf(path, sizeof(path), SYSFS_GPIO_DIR "/gpio%d/direction", pin);
    int fd = open(path, O_WRONLY);
    if (fd >= 0) {
        write(fd, "out", 3);
        close(fd);
    }
}

void gpio_set_input(int pin) {
    char path[64];
    export_gpio(pin);
    snprintf(path, sizeof(path), SYSFS_GPIO_DIR "/gpio%d/direction", pin);
    int fd = open(path, O_WRONLY);
    if (fd >= 0) {
        write(fd, "in", 2);
        close(fd);
    }
}

void gpio_write(int pin, int value) {
    char path[64];
    snprintf(path, sizeof(path), SYSFS_GPIO_DIR "/gpio%d/value", pin);
    int fd = open(path, O_WRONLY);
    if (fd >= 0) {
        write(fd, value ? "1" : "0", 1);
        close(fd);
    }
}

int gpio_read(int pin) {
    char path[64], value_str[3];
    snprintf(path, sizeof(path), SYSFS_GPIO_DIR "/gpio%d/value", pin);
    int fd = open(path, O_RDONLY);
    if (fd >= 0) {
        read(fd, value_str, 3);
        close(fd);
        return atoi(value_str);
    }
    return 0;
}

void gpio_init(void) {
    // Optional: batch export/setup
}
