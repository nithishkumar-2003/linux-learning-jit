#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>
#include <string.h>
#include <signal.h>
#include <time.h>

#include "Camera.h"  // Your SPI + OV5642 camera interface

#define IMAGE_FILE_NAME_TEMPLATE "capture(%d).jpg"
#define VIDEO_FRAME_TEMPLATE "frame_%04d.jpg"
#define FRAME_RATE 10  // FPS
#define FRAME_DELAY_US (1000000 / FRAME_RATE)

volatile sig_atomic_t interrupted = 0;

void handle_sigint(int sig) {
    interrupted = 1;
}

static void set_terminal_mode(int enable);
static char getch_nonblock();
static void wait_for_enter();
static void record_video();
static void show_main_menu();

int main() {
    signal(SIGINT, handle_sigint);
    Camera_init(2, 1, 0);

    while (1) {
        if (interrupted) {
            printf("\nInterrupt received. Returning to menu...\n");
            interrupted = 0;
        }

        show_main_menu();

        int choice;
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar(); // consume newline

        if (choice == 3) {
            printf("Exiting...\n");
            break;
        }

        if (choice < 1 || choice > 3) {
            printf("Invalid choice. Try again.\n");
            continue;
        }

        printf("Choose a resolution:\n");
        printf("1: 320x240\n2: 640x480\n3: 1024x768\n4: 1280x960\n");
        printf("5: 1600x1200\n6: 2048x1536\n7: 2592x1944\n");
        printf("Enter resolution choice: ");
        int res_choice;
        scanf("%d", &res_choice);
        getchar(); // consume newline

        switch (res_choice) {
            case 1: Camera_set_resolution(RES_320x240); break;
            case 2: Camera_set_resolution(RES_640x480); break;
            case 3: Camera_set_resolution(RES_1024x768); break;
            case 4: Camera_set_resolution(RES_1280x960); break;
            case 5: Camera_set_resolution(RES_1600x1200); break;
            case 6: Camera_set_resolution(RES_2048x1536); break;
            case 7: Camera_set_resolution(RES_2592x1944); break;
            default: printf("Invalid resolution.\n"); continue;
        }

        if (choice == 1) {
            int count = 1;
            while (1) {
                printf("Press ENTER to capture image or Ctrl+C to go back to menu...\n");
                wait_for_enter();
                if (interrupted) break;

                Camera_single_capture();
                char filename[256];
                snprintf(filename, sizeof(filename), IMAGE_FILE_NAME_TEMPLATE, count++);
                Camera_save_capture_to_file(filename);
                printf("Image saved as '%s'\n", filename);
            }
        } else if (choice == 2) {
            printf("Press 's' to start video recording and 'e' to end recording...\n");
            set_terminal_mode(1);  // non-canonical mode
            while (1) {
                if (interrupted) break;
                char ch = getch_nonblock();
                if (ch == 's') {
                    record_video();
                    break;
                } else if (ch == 'e') {
                    printf("You haven't started recording yet.\n");
                }
                usleep(100000);  // poll delay
            }
            set_terminal_mode(0);  // reset terminal
        }
    }

    Camera_shutdown();
    return 0;
}

static void show_main_menu() {
    printf("\n===== Camera Menu =====\n");
    printf("1: Capture Image\n");
    printf("2: Capture Video\n");
    printf("3: Exit\n");
}

static void wait_for_enter() {
    while (getchar() != '\n');
}

static char getch_nonblock() {
    struct termios oldt, newt;
    int oldf;
    char ch;

    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

    ch = getchar();

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);

    return ch;
}

static void set_terminal_mode(int enable) {
    static struct termios oldt;
    struct termios newt;

    if (enable) {
        tcgetattr(STDIN_FILENO, &oldt);
        newt = oldt;
        newt.c_lflag &= ~(ICANON | ECHO);
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    } else {
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    }
}

static void record_video() {
    int frame_index = 0;
    struct timespec start, now;

    printf("Recording started. Press 'e' to stop...\n");

    while (1) {
        clock_gettime(CLOCK_MONOTONIC, &start);

        Camera_single_capture();
        char filename[256];
        snprintf(filename, sizeof(filename), VIDEO_FRAME_TEMPLATE, frame_index++);
        Camera_save_capture_to_file(filename);
        printf("Captured frame %d -> %s\n", frame_index, filename);

        // Frame rate control
        do {
            usleep(1000);  // check every 1ms
            clock_gettime(CLOCK_MONOTONIC, &now);
        } while (((now.tv_sec - start.tv_sec) * 1000000 + (now.tv_nsec - start.tv_nsec) / 1000) < FRAME_DELAY_US);

        char ch = getch_nonblock();
        if (ch == 'e' || interrupted) {
            break;
        }
    }

    printf("Recording stopped. Creating video...\n");

    int ret = system("ffmpeg -y -framerate 10 -i frame_%04d.jpg -c:v libx264 -crf 18 -preset slow -pix_fmt yuv444p output_high.mp4");

    if (ret == 0) {
        printf("Video created: output_high.mp4\n");

        // Clean up
        for (int i = 0; i < frame_index; ++i) {
            char filename[256];
            snprintf(filename, sizeof(filename), VIDEO_FRAME_TEMPLATE, i);
            remove(filename);
        }
    } else {
        fprintf(stderr, "Failed to create video. Check ffmpeg installation.\n");
    }
}



