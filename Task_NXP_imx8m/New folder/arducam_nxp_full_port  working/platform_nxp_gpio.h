
#ifndef PLATFORM_NXP_GPIO_H
#define PLATFORM_NXP_GPIO_H

void gpio_set_output(int pin);
void gpio_set_input(int pin);
void gpio_write(int pin, int value);
int gpio_read(int pin);
void gpio_init(void);

#endif
