#include <stdio.h>
#include "ArduCAM.h"
#include "bcm283x_board_driver.h"
#include "sccb_bus.h"
#include "ov5642_regs.h"

// Basic version to capture JPEG and save it
int main(void) {
    printf("Initializing camera...\n");
    arducam_init();  // SPI + GPIO
    arducam_reset();

    printf("Capturing image...\n");
    if (arducam_capture_jpeg("image.jpg") != 0) {
        fprintf(stderr, "Image capture failed!\n");
        return 1;
    }

    printf("Image saved to image.jpg\n");
    return 0;
}

