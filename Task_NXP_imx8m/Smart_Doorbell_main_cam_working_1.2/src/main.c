#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
#include <string.h>
 
#include <Camera.h>  // Your SPI + OV5642 camera interface
 
#define IMAGE_FILE_NAME_TEMPLATE "capture(%d).jpg"
#define VIDEO_FRAME_TEMPLATE "frame_%04d.jpg"
// #define MAX_FRAMES 100
#define FRAME_DELAY_US 100000  // 10 FPS (in microseconds)
 
static void wait_for_keypress(const char *message);
static void record_video(int frame_count, useconds_t delay_us);
 
int main() {
    printf("Smart Camera Capture - IMX8MM Version\n");
 
    printf("Choose a resolution:\n");
    printf("1: 320x240\n");
    printf("2: 640x480\n");
    printf("3: 1024x768\n");
    printf("4: 1280x960\n");
    printf("5: 1600x1200\n");
    printf("6: 2048x1536\n");
    printf("7: 2592x1944\n");
    printf("Enter the number corresponding to your choice: ");
 
    int choice;
    scanf("%d", &choice);
    getchar();  // consume newline
 
    int frames;
    printf("Enter the number of frames to capture: ");
    scanf("%d",&frames);
    getchar();  // consume newline
 
    switch(choice)
    {
        case 1:
            Camera_set_resolution(RES_320x240);
            break;
        case 2:
            Camera_set_resolution(RES_640x480);
            break;
        case 3:
            Camera_set_resolution(RES_1024x768);
            break;
        case 4:
            Camera_set_resolution(RES_1280x960);
            break;
        case 5:
            Camera_set_resolution(RES_1600x1200);
            break;
        case 6:
            Camera_set_resolution(RES_2048x1536);
            break;
        case 7:
            Camera_set_resolution(RES_2592x1944);
            break;
        default:
            printf("Invalid choice. Exiting.\n");
            return 1;
    }
 
    Camera_init(2, 1, 0);
 
    printf("\nSelect mode:\n");
    printf("1: Capture Image\n");
    printf("2: Record Video (%d frames at 10 FPS)\n", frames);
    printf("Enter your choice: ");
 
    int mode;
    scanf("%d", &mode);
    getchar(); // consume newline
 
    if (mode == 1) {
        int capture_count = 1;
 
        while (1) {
            wait_for_keypress(">> Press ENTER to capture image (CTRL+C to exit): ");
            Camera_single_capture();
 
            char image_filename[256];
            snprintf(image_filename, sizeof(image_filename), IMAGE_FILE_NAME_TEMPLATE, capture_count);
 
            Camera_save_capture_to_file(image_filename);
 
            printf("Image captured and saved as '%s'\n", image_filename);
            capture_count++;
        }
    } else if (mode == 2) {
        record_video(frames, FRAME_DELAY_US);
    } else {
        printf("Invalid mode. Exiting.\n");
    }
 
    Camera_shutdown();
    return 0;
}
 
static void wait_for_keypress(const char *message)
{
    printf("%s", message);
    fflush(stdout);
    while (getchar() != '\n');
}
 
static void record_video(int frame_count, useconds_t delay_us) {
    printf("Recording video...\n");
    for (int i = 0; i < frame_count; i++) {
        Camera_single_capture();
 
        char frame_filename[256];
        snprintf(frame_filename, sizeof(frame_filename), VIDEO_FRAME_TEMPLATE, i);
 
        Camera_save_capture_to_file(frame_filename);
        printf("Saved frame %d -> %s\n", i, frame_filename);
        usleep(delay_us);
    }
 
    printf("Generating video from %d frame(s)...\n",frame_count);
    int ret = system("ffmpeg -y -framerate 10 -i frame_%04d.jpg -c:v libx264 -crf 18 -preset slow -pix_fmt yuv444p output_high.mp4");
 
    if (ret == 0) {
        printf("Video created successfully as 'output.mp4'\n");
 
          // Cleanup: delete the individual frame files
        for (int i = 0; i < frame_count; i++) {
            char frame_filename[256];
            snprintf(frame_filename, sizeof(frame_filename), VIDEO_FRAME_TEMPLATE, i);
            if (remove(frame_filename) == 0) {
                printf("Deleted frame file: %s\n", frame_filename);
            } else {
                perror("Error deleting frame file");
            }
        }
    } else {
        fprintf(stderr, "Failed to generate video. Make sure ffmpeg is installed.\n");
    }
 
}
