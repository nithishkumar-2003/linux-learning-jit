#include <stdio.h>
#include <fcntl.h>
#include <stdint.h>
#include <linux/spi/spidev.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include "platform_nxp_spi.h"

static int spi_fd = -1;  // Global SPI file descriptor

#include <stdio.h>  // make sure included

int spi_init(const char* device, int speed_hz) {
    int fd = open(device, O_RDWR);
    if (fd < 0) {
        perror("SPI open failed");
        return -1;
    }

    uint8_t mode = SPI_MODE_0;
    uint8_t bits = 8;

    if (ioctl(fd, SPI_IOC_WR_MODE, &mode) < 0) {
        perror("SPI: Can't set SPI mode");
        close(fd);
        return -1;
    }

    if (ioctl(fd, SPI_IOC_WR_BITS_PER_WORD, &bits) < 0) {
        perror("SPI: Can't set bits per word");
        close(fd);
        return -1;
    }

    if (ioctl(fd, SPI_IOC_WR_MAX_SPEED_HZ, &speed_hz) < 0) {
        perror("SPI: Can't set max speed");
        close(fd);
        return -1;
    }

    printf("SPI initialized on %s with fd %d\n", device, fd);
    return fd;
}

// Called from ArduCAM library
void spiInit(uint32_t speed, uint8_t mode) {
    spi_fd = spi_init("/dev/spidev1.0", speed);
    if (spi_fd < 0) {
        fprintf(stderr, "Failed to initialize SPI\n");
    } else {
        printf("SPI initialized successfully, fd=%d\n", spi_fd);
    }
}

// Transfer a single byte (already written)
int spi_send_receive(int fd, unsigned char tx, unsigned char* rx) {
    struct spi_ioc_transfer tr = {
        .tx_buf = (unsigned long)&tx,
        .rx_buf = (unsigned long)rx,
        .len = 1,
        .speed_hz = 0,
        .delay_usecs = 0,
        .bits_per_word = 8,
    };
    return ioctl(fd, SPI_IOC_MESSAGE(1), &tr);
}

// New: Multi-byte transfer used by ArduCAM
void spi_transfer(uint8_t *tx_buf, uint8_t *rx_buf, uint32_t len) {
    for (uint32_t i = 0; i < len; i++) {
        if (spi_send_receive(spi_fd, tx_buf[i], &rx_buf[i]) < 0) {
            perror("spi_transfer failed");
            break;
        }
    }
}

