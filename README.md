# micropython
Micro Python

### MicroPython on ESP Using Jupyter Notebook on Ubnutu 18.04 LTS

#### 1. Installing MicroPython:

The first thing to be done with a fresh NodeMCU (or ESP32), is to erase what is loaded in its memory, “flashing” a new firmware, that will be the MicroPython interpreter.

A. Getting the new FW:

Go to the site: [MicroPython downloads](http://micropython.org/download#esp8266) and download the appropriated FW for your device:

For example, for ESP8266, the latest version is:

```
esp8266-20180511-v1.9.4.bin (Latest 01Jun18)
```

(you can find details how to install the FW [here](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware))

Then yu can replace the binary with new one you download por example:

```
esp8266-20180511-v1.9.4.bin` to `esp8266-20180511-v2.10.1.bin`
```

B. The ideal is to create a directory where you will work with MicroPython. For example, in case of a mac, starting from your root directory then git clones this repository:

```
cd Devel
mkdir MicroPython
cd MicroPython
git clone git@github.com:marobo/micropython.git
```

C. Create micropython virtualenv with python3
```
pyenv virtualenv 3.5.6 micropython
```

Set micropython to local version python to activate micropython
```
pyenv local micropython
```

> At this point: Connect the NodeMCU or ESP32 to your PC using the serial USB cable.

D. Check where is the serial port that is being used by your device using the command, this is on ubuntu:

```
ls /dev/tty.*
```

E. Install *esptool* (tool used to flash/erase FW on devices)

```
pip install esptool
```

Erase the NodeMCU flash:

```
esptool.py --port /dev/ttyUSB0 erase_flash
```

if got a permission denied, please give the a permission like:

```
sudo chmod a+rw /dev/ttyUSB0
```

then run it again:

```
esptool.py --port /dev/ttyUSB0 erase_flash
```

Flash the new FW:

```
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 binary/esp8266-20180511-v1.9.4.bin
```

Once you have the Firmware installed, you can play with REPL* on Terminal using the command "Screen":

```
screen  /dev/ttyUSB0 115200
>>> print ("hello ESP8266")
>>> hello ESP8266
```

If you are at REPL, use:

[Ctrl+C] to break a pgm and

[Ctrl+A] [K] [Y] to quit and return to the terminal.

\* REPL stands for “*Read Evaluate Print Loop”*, and is the name given to the interactive MicroPython prompt that you can access on the ESP8266. You can learn more about REPL [here](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html).



#### 3. Installing Jupyter MicroPython Kernel

To interact with a MicroPython ESP8266 or ESP32 over its serial REPL, we will need to install a specific Jupyter Kernel.

> This is necessary to be done only once.

From [Jupyter Documentation website](http://jupyter.org/documentation), we can list all “ Community-maintained kernels”. There, we will be sent to :

[Jupyter MicroPython Kernel](https://github.com/goatchurchprime/jupyter_micropython_kernel/)

Once we have Python 3 installed on our machine, Next, install the library  `jupyter_micropython_kernel` (in editable mode) into Python3 using the shell command:

```
pip install -e jupyter_micropython_kernel
```

This creates a small file pointing to this directory in the python/../site-packages directory and makes it possible to “git update” the library later as it gets improved.

> Things can go wrong here, and you might need “pip3” or “sudo pip” if you have numerous different versions of python installed.

Install the kernel into Jupyter itself using the shell command:

```
pip install jupyter-client
```

This creates the small file “.local/share/jupyter/kernels/micropython/kernel.json” that jupyter uses to reference it’s kernels.

To find out where your kernelspecs are stored, you can type:

```
jupyter kernelspec list
```

The Terminal PrintScreen show you the list of kernels that I have installed on my machine. Note that in my case I installed the MicroPython kernel using PIP3 command and so, the Kernel is not in the same directory that the other ones (I got an error when trying to install my kernel using PIP).

Now run Jupyter notebooks:

```
jupyter notebook
```

In the notebook click the "New" Notebook button in the upper right, you should see the kernel display name listed: "MicroPython — USB".

On the first cell, you will need to define the port and baud rate that will be used (115200 works fine):

```
%serialconnect to --port=/dev/ttyUSB0 --baud=115200
```

As a response, the cell will return:

```
Connecting to --port=/dev/ttyUSBO --baud=115200
Ready.
```

And that’s it! When “Ready” appears, you should be able to execute MicroPython commands by running the cells.

Let’s try:

```
print ('hello esp8266')
```

print ('hello esp8266')
You should receive the response of your ESP8266 as on output on the cell:

```
hello esp8266
```