CC ?= gcc
CFLAGS ?= -Wall -O2 -g
OUTDIR ?= build
 
INCLUDE_DIRS = \
	-I"src"

SRC_DIRS = \
	src
 
C_SRCS = $(foreach dir, $(SRC_DIRS), $(wildcard $(dir)/*.c)) src/main.c
OBJS = $(C_SRCS:.c=.o)
 
LIBS = -lgpiod -lpthread
 
TARGET = $(OUTDIR)/arducam_app
 
$(shell mkdir -p $(OUTDIR))
 
.PHONY: all clean
 
all: $(TARGET)
 
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LIBS)
 
%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDE_DIRS) -c $< -o $@
 
clean:
	rm -rf $(OUTDIR) *.o $(foreach dir,$(SRC_DIRS),$(dir)/*.o)
