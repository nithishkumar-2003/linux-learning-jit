
CC = gcc
CFLAGS = -Wall -O2

SRC = \
    platform_nxp_gpio.c \
    platform_nxp_spi.c \
    sccb_bus.c \
    ArduCAM.c \
    capture_image.c

OBJ = $(SRC:.c=.o)
BIN = capture_image

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) -o $@ $^

clean:
	rm -f $(OBJ) $(BIN)
