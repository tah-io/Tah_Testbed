sudo avrdude -c linuxspi -p atmega32u4 -P /dev/spidev0.0 -U flash:w:blink.hex
sudo avrdude -c linuxspi -p atmega32u4 -P /dev/spidev0.0 -U lfuse:w:0xff:m -U hfuse:w:0xff:m -U efuse:w:0xff:m



