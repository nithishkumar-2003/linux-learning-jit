CC ?= gcc
CFLAGS ?= -Wall -O2 -g -I"src" 
LDFLAGS = -Wl,--hash-style=gnu
LIBS = -lgpiod -lpthread
OUTDIR ?= build

SRC_DIRS = src
C_SRCS = $(foreach dir, $(SRC_DIRS), $(wildcard $(dir)/*.c)) src/main.c
OBJS = $(C_SRCS:.c=.o)
TARGET = $(OUTDIR)/arducam_app

$(shell mkdir -p $(OUTDIR))

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^ $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OUTDIR) *.o $(foreach dir,$(SRC_DIRS),$(dir)/*.o)

