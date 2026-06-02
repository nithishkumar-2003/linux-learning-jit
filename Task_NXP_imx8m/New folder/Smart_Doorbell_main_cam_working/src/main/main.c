#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>

#include <Camera.h>  // Your SPI + OV5642 camera interface

#define IMAGE_FILE_NAME "capture.jpg"

static void wait_for_keypress(const char *message);

int main() {
    printf("Smart Camera Capture - IMX8MM Version\n");

    // 1. Initialize camera (SPI + I2C + GPIO must be set inside Camera_init)
    Camera_init(2, 1, 0);
    printf("Init successfully");
    

    printf("Camera initialized. Press ENTER to capture an image.\n");

    
    while (1) {
        wait_for_keypress(">> Press ENTER to capture image (CTRL+C to exit): ");

        // 2. Capture image
        Camera_single_capture();
        printf("Image captured successfully");
        // 3. Save image
        Camera_save_capture_to_file(IMAGE_FILE_NAME);
        printf("Image saved successfully");
   
        }

        printf("Image captured and saved as '%s'\n", IMAGE_FILE_NAME);

    Camera_shutdown();
    return 0;
}

// Simple blocking wait for ENTER key press
static void wait_for_keypress(const char *message) {
    printf("%s", message);
    fflush(stdout);
    while (getchar() != '\n');
}

