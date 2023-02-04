# KivyGuiTutorial
* [General info](#general-info)
* [Technologies](#technologies)
* [Giturl](#giturl)
* [Setup](#setup)

## General info
This project is a simple tutorial on GUI development using Python and the Kivy framework.
Finally, it launches the control panel for simple home automation (temperature measurement, lighting control, etc.)

## Technologies
Project is created with:
* PyCharm PyCharm 2022.3.2 (Community Edition)
* Python 3.9
* Kivy 2.1.0

## Giturl
https://github.com/procesorowiec/PythonEmb-KivyTut-Smart-home-panel.git

## Setup
To run the project, you only need a computer with Linux, e.g. Raspberry Pi with OS Raspbian.
Additionally, you need to install the Kivy framework and some dependencies:
```
$ sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
$ python -m pip install kivy[base]

# and just enter to check
$ python -m kivy

# and run in project folder
$ python main.py
```

