#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include "ArduCAM.h"
#include "sccb_bus.h"
#include "platform_nxp_spi.h"

//#define CAM_CS1 0  // update with your chip select GPIO number or macro
#define MAX_BUFFER_SIZE (2*1024*1024)  // 2MB max image size

int main(void) {
    printf("Initializing camera...\n");

//  spi_init(8000000, 0);
    spiInit(8000000, 0);

    uint8_t cmd = 0x00;
    uint8_t val = 0x00;
    spi_transfer(&cmd, &val, 1);  // Expect val to be 0x55
    printf("SPI test result: 0x%02X\n", val);

    gpio_init();
    sccb_bus_init();
    ArduCAM_CS_init(CAM_CS1, -1, -1, -1);
    ArduCAM_Init(OV5642);  // Confirm OV5642 is correct model

    uint8_t test = read_reg(0x00, CAM_CS1);
    printf("SPI test reg: 0x%02X (expect 0x55)\n", test);

    printf("Capturing image...\n");

    flush_fifo(CAM_CS1);
    clear_fifo_flag(CAM_CS1);
    start_capture(CAM_CS1);

    int timeout = 1000;
    while (!(read_reg(0x41, CAM_CS1) & 0x08) && timeout--) {
        usleep(10000);
    }

    if (timeout == 0) {
        printf("Capture timeout.\n");
        return -1;
    }

    unsigned int length = read_fifo_length(CAM_CS1);
    printf("Capture done, FIFO length = %u bytes\n", length);

    if (length == 0 || length > MAX_BUFFER_SIZE) {
        printf("Invalid image length.\n");
        return -1;
    }

    FILE *fp = fopen("image.jpg", "wb");
    if (!fp) {
        perror("fopen failed");
        return -1;
    }

    const int chunk_size = 4096;
    uint8_t buf[chunk_size];
    unsigned int bytes_read = 0;

    while (bytes_read < length) {
        int to_read = (length - bytes_read > chunk_size) ? chunk_size : (length - bytes_read);
        for (int i = 0; i < to_read; i++) {
            buf[i] = read_fifo(CAM_CS1);
        }
        fwrite(buf, 1, to_read, fp);
        bytes_read += to_read;
    }

    fclose(fp);
    printf("Image saved to image.jpg\n");
    return 0;
}

