#include "ArduCAM.h"
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

unsigned int length = 0;
char readbuf[JPEG_BUF_SIZE];
static int spi_fd = -1;

void ArduCAM_CS_init(int CS1, int CS2, int CS3, int CS4) {
    gpio_set_output(CS1);
    gpio_write(CS1, 1);
}

void CS_HIGH(int CS) {
    gpio_write(CS, 1);
    usleep(1);
}

void CS_LOW(int CS) {
    gpio_write(CS, 0);
    usleep(1);
}

unsigned char spiSendReceive(unsigned char data) {
    unsigned char rx = 0;
    spi_send_receive(spi_fd, data, &rx);
    return rx;
}

unsigned char bus_read(int address, int CS) {
    unsigned char value;
    CS_LOW(CS);
    spiSendReceive(address);
    value = spiSendReceive(0x00);
    CS_HIGH(CS);
    return value;
}

unsigned char bus_write(int address, int value, int CS) {
    CS_LOW(CS);
    spiSendReceive(address);
    spiSendReceive(value);
    CS_HIGH(CS);
    return 1;
}

unsigned char read_reg(unsigned char addr, int CS) {
    return bus_read(addr & 0x7F, CS);
}

void write_reg(unsigned char addr, unsigned char data, int CS) {
    bus_write(addr | 0x80, data, CS);
}

unsigned char read_fifo(int CS) {
    return bus_read(0x3D, CS); // SINGLE_FIFO_READ
}

void flush_fifo(int CS) {
    write_reg(0x04, 0x01, CS); // FIFO_CLEAR_MASK
}

void start_capture(int CS) {
    write_reg(0x04, 0x02, CS); // FIFO_START_MASK
}

void clear_fifo_flag(int CS) {
    write_reg(0x04, 0x01, CS);
}

unsigned int read_fifo_length(int CS) {
    unsigned int len1 = read_reg(0x42, CS);
    unsigned int len2 = read_reg(0x43, CS);
    unsigned int len3 = read_reg(0x44, CS) & 0x7f;
    return ((len3 << 16) | (len2 << 8) | len1) & 0x07fffff;
}

void set_bit(unsigned char addr, unsigned char bit, int CS) {
    unsigned char temp = read_reg(addr, CS);
    write_reg(addr, temp | bit, CS);
}

void clear_bit(unsigned char addr, unsigned char bit, int CS) {
    unsigned char temp = read_reg(addr, CS);
    write_reg(addr, temp & ~bit, CS);
}

unsigned char get_bit(unsigned char addr, unsigned char bit, int CS) {
    return read_reg(addr, CS) & bit;
}

void ArduCAM_Init(unsigned char model) {
    // For simplicity in this port, we assume model is OV5642 and JPEG is default.
    // Full reg writing via SCCB needs to be added.
    printf("ArduCAM_Init: camera model = %d
", model);
    // This should be extended to call wrSensorRegs16_8(ov5642_320x240);
}

void set_format(unsigned char fmt) {
    // Assume JPEG default
}
