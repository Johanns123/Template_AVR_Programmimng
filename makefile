# Makefile para compilar código C para Atmega e gravar no microcontrolador em ambiente Windows

# Nome do projeto
PROJECT_NAME = main

# Diretórios
SRC_DIR = src
INCLUDE_DIR = include
BUILD_DIR = build

# Arquivos fonte C
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)

# Flags do compilador
CFLAGS = -std=c11 -mmcu=$(MCU) -Wall -Wextra -Os -Iinclude

# Nome do arquivo de saída (.hex)
OUTPUT_HEX = $(BUILD_DIR)/$(PROJECT_NAME).hex

# Nome do microcontrolador
MCU = atmega328p

# Programador para avrdude
PROGRAMMER = arduino
PORT = COM3
BAUD = 115200

# Comandos
CC = avr-gcc
OBJCOPY = avr-objcopy
AVRDUDE = avrdude
SIZE = avr-size

# Alvos
all: build_and_size

build:
	$(CC) $(CFLAGS) -I$(INCLUDE_DIR) $(SRC_FILES) -o $(BUILD_DIR)/$(PROJECT_NAME).elf
	$(OBJCOPY) -j .text -j .data -O ihex $(BUILD_DIR)/$(PROJECT_NAME).elf $(OUTPUT_HEX)

flash:
	$(AVRDUDE) -p $(MCU) -c $(PROGRAMMER) -P $(PORT) -U flash:w:$(OUTPUT_HEX) -b $(BAUD)

build_and_flash: build flash

build_and_size: build size_info

clean:
	rm -f $(BUILD_DIR)/*
size_info:
	@echo "MCU: $(MCU)"
	@python3 mem.py $(MCU)

	
.PHONY: all build flash build_and_flash clean size_info