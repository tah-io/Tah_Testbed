sudo avrdude -c linuxspi -p atmega32u4 -P /dev/spidev0.0 -U flash:w:setAnalogHigh.hex
