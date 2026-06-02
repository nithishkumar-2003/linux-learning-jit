#ifndef __ARDUCAM_H
#define __ARDUCAM_H

#define JPEG_BUF_SIZE   2*1024*1024
#define CAM_CS1         8

#define OV5642 3

#include "platform_nxp_gpio.h"
#include "platform_nxp_spi.h"

extern unsigned int length;
extern char readbuf[JPEG_BUF_SIZE];

void ArduCAM_Init(unsigned char model);
void ArduCAM_CS_init(int CS1, int CS2, int CS3, int CS4);
void set_format(unsigned char fmt);
void write_reg(unsigned char addr, unsigned char data, int CS);
unsigned char read_reg(unsigned char addr, int CS);
unsigned char read_fifo(int CS);
void flush_fifo(int CS);
void start_capture(int CS);
void clear_fifo_flag(int CS);
unsigned int read_fifo_length(int CS);
void set_bit(unsigned char addr, unsigned char bit, int CS);
void clear_bit(unsigned char addr, unsigned char bit, int CS);
unsigned char get_bit(unsigned char addr, unsigned char bit, int CS);

#endif
