# RaspberryPi_RS485
This reposity is used to read RS485 sensor with Raspberry Pi

=========================================
        1. Set 485 serial port
=========================================

sudo raspi-config  -> Interfacing Options -> Serial -> login shell(no) -> port hardware(yes)

Then:   sudo vim /boot/config.txt   ->  Enable_uart=1   ->  sudo reboot
The /dev/ttyS0 is the RS485 serial port

Connect the sensor:
    ![image](https://github.com/Hep-dog/RaspberryPi_RS485/raw/master/images/Connection.jpg)


=========================================
        2.  Read the RS485 data
=========================================

read the data with the request-response scheme:

The  request code can be found in the sensor instructions:
    ![image](https://github.com/Hep-dog/RaspberryPi_RS485/raw/master/images/RequestCode.jpg)

Read the data using the following code:
    ![image](https://github.com/Hep-dog/RaspberryPi_RS485/raw/master/images/Code.jpg)


Then using influxdb + grafana + telegraf to display the data online:
    ![image](https://github.com/Hep-dog/RaspberryPi_RS485/raw/master/images/Grafana.jpg)



