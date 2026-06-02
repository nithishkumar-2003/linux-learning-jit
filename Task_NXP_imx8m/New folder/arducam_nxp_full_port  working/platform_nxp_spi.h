
#ifndef PLATFORM_NXP_SPI_H
#define PLATFORM_NXP_SPI_H

int spi_init(const char* device, int speed_hz);
int spi_send_receive(int fd, unsigned char tx, unsigned char* rx);

#endif
