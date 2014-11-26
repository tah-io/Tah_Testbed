sudo avrdude -c linuxspi -p atmega32u4 -P /dev/spidev0.0 -U flash:w:Tah.hex
sudo avrdude -c linuxspi -p atmega32u4 -P /dev/spidev0.0 -U lfuse:w:0xff:m -U hfuse:w:0xd8:m -U efuse:w:0xcb:m



