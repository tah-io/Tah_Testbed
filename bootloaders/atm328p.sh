sudo avrdude -c linuxspi -p atmega328p -P /dev/spidev0.0 -U flash:w:ShrimpUSB_rev1_atmega328p_16MHz.hex
sudo avrdude -c linuxspi -p atmega328p -P /dev/spidev0.0 -U lfuse:w:0xD7:m -U hfuse:w:0xD0:m -U efuse:w:0x04:m
