# MAF-GLU-Alpha-Software
Software written for MAF GLU 2017, automated lighting system controlled via a DMX controller. Written in python by Gui Ming Jiang and Yang Chun Wei from the 44th HCSC.

Updated by Guan Peng from the 45th HCSC. Special thanks to him for writing the README as well.

![IMG_8856](https://user-images.githubusercontent.com/12895754/118540144-df01ca00-b782-11eb-9f3d-2c6e1c579429.JPG)

# Installation Guide

hondmx is a library, run buggy.py for actual set up

Debug_backup.py is for trying without the DMX box

--------------------------------------------------------------------------

To begin: Install python IDLE for python 2 and 3 from python.org

Install dependencies needed via command prompt
For windows, Enter:
py -2.7 -m pip install (*module name here*)

For Mac, Enter:

python -2.7 -m pip install (*module name here*)

---------------------------------------------------------------------------

The Debug_backup.py is used where the coordinates for lines and positions are entered
manually based on calculations on a 1000 by 1000 pixel canvas.
This helps you to visualize the formation of the lights and can try out your instructions
here to see how it will look like.

Delete the hashtags at the front of code part of the mydmx functions to test with the DMX box.
Can enable print as well to debug if there's any problems. If not disable the prints so there
will be no delay in the response.

-----------------------------------------------------------------------------

To make your life easier, after identifying the significant beats/ timings to change the lighting,
record the time accurate to milliseconds in the form of 
MM.SS.XX  (where M is minutes, S is seconds X is milliseconds)

Run the glu timing generator.py in python 3 IDLE to help you convert the time to a format that the program
can read. This sets the default state of all 16*(this can be changed) channels to 1* (can be changed to 0 for off)
which means all on.

The program should auto generate instructions.txt . 
A tip would be to run this outside of the folder with all the other programmes so you avoid messing up the
actual instructions and only copy the file over to replace if you are sure of the changes.

-------------------------------------------------------------------------------------
The code itself is quite simple to understand (as its hardcoded and is iterative) but
if any questions can direct to me.

Feel free to make amendments to the code to make it better and easier to use as well!
