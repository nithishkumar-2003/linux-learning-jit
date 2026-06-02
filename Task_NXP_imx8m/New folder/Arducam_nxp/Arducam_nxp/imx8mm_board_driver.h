
#ifndef IMX8MM_BOARD_DRIVER_H
#define IMX8MM_BOARD_DRIVER_H

#include <stdint.h>
#include <stddef.h>

int board_spi_init();
int board_spi_transfer(uint8_t *tx_buf, uint8_t *rx_buf, size_t len);
void board_spi_close();

int board_gpio_init();
void board_gpio_set_rst(int value);
void board_gpio_set_cs(int value);
void board_gpio_close();

#endif // IMX8MM_BOARD_DRIVER_H
