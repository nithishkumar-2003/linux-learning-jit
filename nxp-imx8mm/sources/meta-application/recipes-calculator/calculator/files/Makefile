APP_NAME = calculator
CC = $(CROSS_COMPILE)gcc
CFLAGS = -Wall -O2

all: $(APP_NAME)

$(APP_NAME): calculator.c
	$(CC) $(CFLAGS) -o $(APP_NAME) calculator.c

install:
	install -D -m 0755 $(APP_NAME) $(DESTDIR)/usr/bin/$(APP_NAME)

clean:
	rm -f $(APP_NAME)

