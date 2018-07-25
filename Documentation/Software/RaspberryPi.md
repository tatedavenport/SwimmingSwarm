# Installing the Operating System
You can either download a base install of [Raspbian][1] or copy a disk image from one of the other working raspberry pi's.
To copy the disk image put the sd card in a linux computer, unmount the partitions, and run 

```
dd if=mmcblk0p2 of=RaspberryPiImage.img bs=1M
```
Then you can use dd or some other software (like [Etcher][2])
to copy that image to another sd card.

When you first boot up the new install it will most likely resize itself to the size of your SD Card and reboot, this is normal.
The root password should be `raspberry`

# Installing Dependencies for Joystick Control over Wifi
## Dronekit
Make sure you install dronekit first as it will overwrite the MavLink install with an older version that wil not work.

To install Dronekit run `sudo pip3 install dronekit`
## MavLink
To install MavLink run `sudo pip3 install -U pymavlink`

After installing MavLink and Dronekit the MavLink version should be at least 2.2.10


# Installing LimeSDR and other Dependencies
## Install GNURadio
To install GNURadio run `sudo apt-get install gnuradio`
## Install SoapySDR
Follow the build guide [here][3]
## Install Osmocom
Follow the build guide [here][4]
## Install Limesuite
You can attemt to follow the install guide [here][5] but
this didn't work on Raspberry Pi due to the repository not supporting it. 
Instead, install some graphics dependencies by running 
`sudo apt-get install libwxgtk3.0-dev freeglut3-dev` 
Then build Limesuite by following [this guide][6].


[1]: https://www.raspberrypi.org/downloads/raspbian/
[2]: https://etcher.io/
[3]: https://github.com/pothosware/SoapySDR/wiki/BuildGuide
[4]: https://osmocom.org/projects/gr-osmosdr/wiki#Build-process
[5]: https://wiki.myriadrf.org/Lime_Suite#Ubuntu
[6]: https://wiki.myriadrf.org/Lime_Suite#Unix_makefiles
