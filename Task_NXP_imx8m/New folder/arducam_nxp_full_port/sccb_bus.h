#ifndef _SCCB_BUS_H_
#define _SCCB_BUS_H_

#include <stdint.h>

struct sensor_reg {
    uint16_t reg;
    uint8_t val;
};

void sccb_bus_init(void);
void sccb_bus_start(void);
void sccb_bus_stop(void);
void sccb_bus_send_ack(void);
void sccb_bus_send_noack(void);
unsigned char sccb_bus_write_byte(unsigned char data);
unsigned char sccb_bus_read_byte(void);
int wrSensorRegs16_8(const struct sensor_reg* reglist);

#endif

