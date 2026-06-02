#include <stdio.h>
#include "ArduCAM.h"
#include "sccb_bus.h"

int main(void) {
    printf("Initializing camera...\n");
    gpio_init();
    sccb_bus_init();
    ArduCAM_CS_init(CAM_CS1, -1, -1, -1);
    ArduCAM_Init(OV5642);

    printf("Capturing image...\n");
    flush_fifo(CAM_CS1);
    clear_fifo_flag(CAM_CS1);
    start_capture(CAM_CS1);

    while (!(read_reg(0x41, CAM_CS1) & 0x08)) {
        usleep(10000);
    }

    length = read_fifo_length(CAM_CS1);
    FILE *fp = fopen("image.jpg", "wb");
    for (unsigned int i = 0; i < length; i++) {
        readbuf[i] = read_fifo(CAM_CS1);
    }
    fwrite(readbuf, 1, length, fp);
    fclose(fp);
    printf("Image saved to image.jpg\n");
    return 0;
}
