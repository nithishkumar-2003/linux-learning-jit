NAME=run_Arducam_Demo
CC ?= $(CROSS_COMPILE)gcc
CFLAGS = -Wall -pthread
LDFLAGS = -Wl,--hash-style=gnu       # Add this line

ODIR = obj
SDIR = src

_DEPS = ArduCAM.h bcm283x_board_driver.h sccb_bus.h ov2640_regs.h ov5640_regs.h ov5642_regs.h
DEPS = $(patsubst %,$(SDIR)/%,$(_DEPS))

_OBJ = ArducamDemo.o ArduCAM.o bcm283x_board_driver.o sccb_bus.o
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))

$(ODIR)/%.o: src/%.c $(DEPS)
	@mkdir -p $(@D)
	$(CC) -c -o $@ $< $(CFLAGS)

$(NAME): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)   # add LDFLAGS here

.PHONY: run
run: $(NAME)
	sudo ./$(NAME)

.PHONY: clean
clean:
	rm -f $(NAME) $(ODIR)/*.o

