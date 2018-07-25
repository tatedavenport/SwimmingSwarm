# Installing the Operating System
You can either download an base install of [raspbian][1] or copy a disk image from one of the other working raspberry pi's.
To copy the disk image put the sd card in a linux computer, unmount the partitions, and run 

```
dd if=mmcblk0p2 of=RaspberryPiImage.img bs=1M
```
Then you can use dd or some other software (like [Etcher][2])
to copy that image to another sd card.

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
Follow the build guide [here][5]. 
This didn't work on raspberry pi due to the repository not supporting it. 
Instead, build Limesuite by following [this guide][6].


[1]: https://www.raspberrypi.org/downloads/raspbian/
[2]: https://etcher.io/
[3]: https://github.com/pothosware/SoapySDR/wiki/BuildGuide
[4]: https://osmocom.org/projects/gr-osmosdr/wiki#Build-process
[5]: https://wiki.myriadrf.org/Lime_Suite#Ubuntu
[6]: https://wiki.myriadrf.org/Lime_Suite#Unix_makefiles
