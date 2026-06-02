
#include "imx8mm_board_driver.h"
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>
#include <gpiod.h>

#define SPI_DEVICE "/dev/spidev0.0"
#define SPI_MODE SPI_MODE_0
#define SPI_BITS 8
#define SPI_SPEED 8000000

static int spi_fd = -1;
static struct gpiod_chip *gpio_chip;
static struct gpiod_line *cs_line, *rst_line;

int board_spi_init() {
    spi_fd = open(SPI_DEVICE, O_RDWR);
    if (spi_fd < 0) {
        perror("Failed to open SPI device");
        return -1;
    }

    uint8_t mode = SPI_MODE;
    uint8_t bits = SPI_BITS;
    uint32_t speed = SPI_SPEED;

    ioctl(spi_fd, SPI_IOC_WR_MODE, &mode);
    ioctl(spi_fd, SPI_IOC_WR_BITS_PER_WORD, &bits);
    ioctl(spi_fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed);

    return 0;
}

int board_spi_transfer(uint8_t *tx_buf, uint8_t *rx_buf, size_t len) {
    struct spi_ioc_transfer tr = {
        .tx_buf = (unsigned long)tx_buf,
        .rx_buf = (unsigned long)rx_buf,
        .len = len,
        .speed_hz = SPI_SPEED,
        .bits_per_word = SPI_BITS,
    };
    return ioctl(spi_fd, SPI_IOC_MESSAGE(1), &tr);
}

void board_spi_close() {
    if (spi_fd >= 0) {
        close(spi_fd);
    }
}

int board_gpio_init() {
    gpio_chip = gpiod_chip_open_by_name("gpiochip0");
    if (!gpio_chip) {
        perror("Failed to open gpiochip");
        return -1;
    }

    // Adjust line numbers to match your hardware
    rst_line = gpiod_chip_get_line(gpio_chip, 17);
    cs_line = gpiod_chip_get_line(gpio_chip, 27);

    gpiod_line_request_output(rst_line, "rst", 1);
    gpiod_line_request_output(cs_line, "cs", 1);

    return 0;
}

void board_gpio_set_rst(int value) {
    gpiod_line_set_value(rst_line, value);
}

void board_gpio_set_cs(int value) {
    gpiod_line_set_value(cs_line, value);
}

void board_gpio_close() {
    gpiod_chip_close(gpio_chip);
}
