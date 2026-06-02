
#ifndef PLATFORM_NXP_SPI_H
#define PLATFORM_NXP_SPI_H

#include <stdint.h>

int spi_init(const char* device, int speed_hz);
void spi_transfer(uint8_t *tx_buf, uint8_t *rx_buf, uint32_t len);
int spi_send_receive(int fd, unsigned char tx, unsigned char* rx);

#endif
