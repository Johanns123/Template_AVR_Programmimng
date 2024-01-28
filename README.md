## Template for progamming AVR microcontrollers without any framework

This repository has a makefile to build, flash and see the size of your application. The folder .vscode is not necessary for projects, it is only used to facilitate  working with VSCode using intellisense

### How to use it:
1. Write your .c files on src folder
2. Write your header files on include folder
3. To build your application open a terminal on this path and type `make`
4. `make` will execute `build_and_size`, building the application and showing the memory consumption
5. If you use an AVR microcontroller that is not atmega328p, please change on makefile the target `MCU`
6. To upload your code type `make flash`. But pay attention because the upload rules are for atmega328p, with 115200bps and that is in COM3. If your device has another BAUD RATE and is in another port (in linux OS is different. i.e., devtty/USBx) just change in makefile
7. This makefile was developed for Windows OS. To use `make size_info` and `make clean` is necessary to put the correct commands of your linux distro os MAC OS
