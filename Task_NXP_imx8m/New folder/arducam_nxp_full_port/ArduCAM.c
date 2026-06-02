#include "ArduCAM.h"
#include "sccb_bus.h"
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

unsigned int length = 0;
char readbuf[JPEG_BUF_SIZE];
static int spi_fd = -1;

// Initialize CS pin
void ArduCAM_CS_init(int CS1, int CS2, int CS3, int CS4) {
    gpio_set_output(CS1);
    gpio_write(CS1, 1);  // Set CS high (inactive)
}

void CS_HIGH(int CS) {
    gpio_write(CS, 1);
    usleep(1);
}

void CS_LOW(int CS) {
    gpio_write(CS, 0);
    usleep(1);
}

// SPI single-byte transfer
unsigned char spiSendReceive(unsigned char data) {
    unsigned char rx = 0;
    spi_send_receive(spi_fd, data, &rx);
    return rx;
}

// SPI read with chip select
unsigned char bus_read(int address, int CS) {
    unsigned char value;
    CS_LOW(CS);
    spiSendReceive(address);
    value = spiSendReceive(0x00);
    CS_HIGH(CS);
    return value;
}

// SPI write with chip select
unsigned char bus_write(int address, int value, int CS) {
    CS_LOW(CS);
    spiSendReceive(address);
    spiSendReceive(value);
    CS_HIGH(CS);
    return 1;
}

// Register access helpers
unsigned char read_reg(unsigned char addr, int CS) {
    return bus_read(addr & 0x7F, CS);
}

void write_reg(unsigned char addr, unsigned char data, int CS) {
    bus_write(addr | 0x80, data, CS);
}

// FIFO functions
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

// Read FIFO length (3 bytes)
unsigned int read_fifo_length(int CS) {
    unsigned int len1 = read_reg(0x42, CS);
    unsigned int len2 = read_reg(0x43, CS);
    unsigned int len3 = read_reg(0x44, CS) & 0x7F;
    return ((len3 << 16) | (len2 << 8) | len1) & 0x07FFFFF;
}

// Bit-level control
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

// OV5642 JPEG 320x240 (example: extend this list)
const struct sensor_reg ov5642_320x240[] = {
    {0x3103, 0x11}, // System clock from PLL
    {0x3008, 0x82}, // Software reset
    {0x3008, 0x42}, // Wake up from reset
    {0x3103, 0x03},
    {0x3017, 0xFF},
    {0x3018, 0xFF},
    {0x3034, 0x1A},
    {0x3035, 0x11},
    {0x3036, 0x69},
    {0x3C07, 0x07},
    {0x3820, 0x41},
    {0x3821, 0x07},
    {0x3814, 0x31},
    {0x3815, 0x31},
    {0x3800, 0x00},
    {0x3801, 0x00},
    {0x3802, 0x00},
    {0x3803, 0x04},
    {0x3804, 0x0A},
    {0x3805, 0x3F},
    {0x3806, 0x07},
    {0x3807, 0x9B},
    {0x3808, 0x01},
    {0x3809, 0x40},
    {0x380A, 0x00},
    {0x380B, 0xF0},
    {0x3811, 0x08},
    {0x3813, 0x02},
    {0x3618, 0x04},
    {0x3612, 0x2B},
    {0x3709, 0x52},
    {0x370C, 0x03},
    {0x3A02, 0x02},
    {0x3A03, 0xE0},
    {0x3A08, 0x01},
    {0x3A09, 0x27},
    {0x3A0A, 0x00},
    {0x3A0B, 0xF6},
    {0x3A0E, 0x01},
    {0x3A0D, 0x02},
    {0x3A14, 0x02},
    {0x3A15, 0xE0},
    {0x4004, 0x02},
    {0x3002, 0x1C},
    {0x3006, 0xC3},
    {0x4713, 0x03},
    {0x4407, 0x04},
    {0x460B, 0x35},
    {0x460C, 0x22},
    {0x4837, 0x22},
    {0x3824, 0x02},
    {0x5001, 0xA3},
    {0x3008, 0x02}, // Wake up again
    {0xFFFF, 0xFF}  // End marker
};


// Camera initialization
void ArduCAM_Init(unsigned char model) {
    printf("ArduCAM_Init: camera model = %d\n", model);
    wrSensorRegs16_8(ov5642_320x240);
}

// Optional: format selection (e.g., JPEG vs RAW)
void set_format(unsigned char fmt) {
    // Stub for format change if needed later
}

