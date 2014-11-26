sudo avrdude -c linuxspi -p atmega8 -P /dev/spidev0.0 -U flash:w:ShrimpUSB_rev1_atmega8_16MHz.hex
sudo avrdude -c linuxspi -p atmega8 -P /dev/spidev0.0 -U lfuse:w:0x1F:m -U hfuse:w:0xC0:m -U efuse:w:0xFF:m
