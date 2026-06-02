#include "sccb_bus.h"
#include "platform_nxp_gpio.h"
#include <unistd.h>

#define SDA_PIN 2
#define SCL_PIN 3
#define I2C_DELAY_US 30

#define SDA_HIGH() gpio_write(SDA_PIN, 1)
#define SDA_LOW()  gpio_write(SDA_PIN, 0)
#define SCL_HIGH() gpio_write(SCL_PIN, 1)
#define SCL_LOW()  gpio_write(SCL_PIN, 0)

#define SDA_IN()   gpio_set_input(SDA_PIN)
#define SDA_OUT()  gpio_set_output(SDA_PIN)
#define SDA_READ() gpio_read(SDA_PIN)

void delay_us(int us) {
    usleep(us);
}

void sccb_bus_init(void) {
    gpio_set_output(SDA_PIN);
    gpio_set_output(SCL_PIN);
    SDA_HIGH();
    SCL_HIGH();
}

void sccb_bus_start(void) {
    SDA_OUT();
    SDA_HIGH(); SCL_HIGH(); delay_us(I2C_DELAY_US);
    SDA_LOW();  delay_us(I2C_DELAY_US);
    SCL_LOW();  delay_us(I2C_DELAY_US);
}

void sccb_bus_stop(void) {
    SDA_OUT();
    SDA_LOW();  SCL_HIGH(); delay_us(I2C_DELAY_US);
    SDA_HIGH(); delay_us(I2C_DELAY_US);
}

void sccb_bus_send_ack(void) {
    SDA_OUT(); SDA_LOW(); delay_us(I2C_DELAY_US);
    SCL_HIGH(); delay_us(I2C_DELAY_US);
    SCL_LOW();  delay_us(I2C_DELAY_US);
}

void sccb_bus_send_noack(void) {
    SDA_OUT(); SDA_HIGH(); delay_us(I2C_DELAY_US);
    SCL_HIGH(); delay_us(I2C_DELAY_US);
    SCL_LOW();  delay_us(I2C_DELAY_US);
}

unsigned char sccb_bus_write_byte(unsigned char data) {
    SDA_OUT();
    for (int i = 0; i < 8; ++i) {
        if (data & 0x80) SDA_HIGH(); else SDA_LOW();
        delay_us(I2C_DELAY_US);
        SCL_HIGH(); delay_us(I2C_DELAY_US);
        SCL_LOW();  delay_us(I2C_DELAY_US);
        data <<= 1;
    }
    SDA_IN(); delay_us(I2C_DELAY_US);
    SCL_HIGH(); delay_us(I2C_DELAY_US);
    unsigned char ack = SDA_READ() ? 0 : 1;
    SCL_LOW();  delay_us(I2C_DELAY_US);
    SDA_OUT();
    return ack;
}

unsigned char sccb_bus_read_byte(void) {
    unsigned char data = 0;
    SDA_IN();
    for (int i = 0; i < 8; ++i) {
        data <<= 1;
        SCL_HIGH(); delay_us(I2C_DELAY_US);
        if (SDA_READ()) data |= 0x01;
        SCL_LOW();  delay_us(I2C_DELAY_US);
    }
    SDA_OUT();
    return data;
}
