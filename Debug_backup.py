# this program is hereby blessed by our lord and saviour, his exellency Dr Hon

# i'm working with this buggy dmx module named pysimpledmx so i copied
# the source file and renamed it hondmx before fixing some of the bugs inside

import pyaudio
import wave
import sys
#import hondmx
import time, dmxlib
#mydmx = dmxlib.DMXConnection("/dev/cu.usbserial-6A09WVRP")
#mydmx.render()
from Tkinter import *
#main config stuff
root = Tk()

#width and height vars
w = 500
h = 500
midx = w/2
midy = h/2
elapsedtime = 0
CHUNK = 512
OFFSET = 0 # time offset in milliseconds, positive means program thinks elapsed time is larger than it is
STARTAT = 000 # offset to start music at in milliseconds

print("-START-")

# instantiate PyAudio (1)
p = pyaudio.PyAudio()
# read data CHANGE PATH HERE
wf = wave.open('wavfile.wav', 'rb')
# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)

canvas = Canvas(root, width = w, height = h)
canvas.pack()

grp15 = canvas.create_oval(midx-20,midy-20,midx+20,midy+20,fill="white")
txt15 = canvas.create_text(midx,midy, text="15")

grp8 = canvas.create_oval(midx-20,midy-200,midx+20,midy-160,fill="white")
txt8 = canvas.create_text(midx,midy-180, text="8")

grp1 = canvas.create_oval(midx-20,midy+200,midx+20,midy+160,fill="white")
txt1 = canvas.create_text(midx,midy+180, text="1")

#group 2 3

grp2 = canvas.create_oval(midx+65,midy+160,midx+105,midy+120,fill="white")
txt2 = canvas.create_text(midx+85,midy+140, text="2")
grp3 = canvas.create_oval(midx+150,midy+120,midx+190,midy+80,fill="white")
txt3 = canvas.create_text(midx+170,midy+100, text="3")

#group 12 13
grp14 = canvas.create_oval(midx-65,midy+160,midx-105,midy+120,fill="white")
txt14 = canvas.create_text(midx-85,midy+140, text="14")
grp13 = canvas.create_oval(midx-150,midy+120,midx-190,midy+80,fill="white")
txt13 = canvas.create_text(midx-170,midy+100, text="13")

#group 9 10 similar to above but sign change
grp9 = canvas.create_oval(midx-65,midy-160,midx-105,midy-120,fill="white")
txt9 = canvas.create_text(midx-85,midy-140, text="9")
grp10 = canvas.create_oval(midx-150,midy-120,midx-190,midy-80,fill="white")
txt10 = canvas.create_text(midx-170,midy-100, text="10")

#similar to above but sign change
grp7 = canvas.create_oval(midx+65,midy-160,midx+105,midy-120,fill="white")
txt7 = canvas.create_text(midx+85,midy-140, text="7")
grp6 = canvas.create_oval(midx+150,midy-120,midx+190,midy-80,fill="white")
txt6 = canvas.create_text(midx+170,midy-100, text="6")

#good for 4 5 11 12
grp5 = canvas.create_oval(midx+180,midy-50,midx+220,midy-10,fill="white")
txt5 = canvas.create_text(midx+200,midy-30, text="5")
grp4 = canvas.create_oval(midx+180,midy+50,midx+220,midy+10,fill="white")
txt4 = canvas.create_text(midx+200,midy+30, text="4")

grp11 = canvas.create_oval(midx-180,midy-50,midx-220,midy-10,fill="white")
txt11 = canvas.create_text(midx-200,midy-30, text="11")
grp12 = canvas.create_oval(midx-180,midy+50,midx-220,midy+10,fill="white")
txt12 = canvas.create_text(midx-200,midy+30, text="12")
#----------------VAR SETTING ENDS-------------------

root.update()
# this program is hereby blessed by our lord and saviour, his exellency Dr Hon

# i'm working with this buggy dmx module named pysimpledmx so i copied
# the source file and renamed it hondmx before fixing some of the bugs inside




# a function to set dmx channel to value
# don't forget to call mydmx.render() after all the setChannel()s are done
def editGUI(channel,state):
    print ("Channel", channel, state)
    if channel == 1 and state == 1:
        canvas.itemconfig(grp1,fill="yellow")
    if channel == 2 and state == 1:
        canvas.itemconfig(grp2,fill="yellow")
    if channel == 3 and state == 1:
        canvas.itemconfig(grp3,fill="yellow")
    if channel == 4 and state == 1:
        canvas.itemconfig(grp4,fill="yellow")
    if channel == 5 and state == 1:
        canvas.itemconfig(grp5,fill="yellow")
    if channel == 6 and state == 1:
        canvas.itemconfig(grp6,fill="yellow")
    if channel == 7 and state == 1:
        canvas.itemconfig(grp7,fill="yellow")
    if channel == 8 and state == 1:
        canvas.itemconfig(grp8,fill="yellow")
    if channel == 9 and state == 1:
        canvas.itemconfig(grp9,fill="yellow")
    if channel == 10 and state == 1:
        canvas.itemconfig(grp10,fill="yellow")
    if channel == 11 and state == 1:
        canvas.itemconfig(grp11,fill="yellow")
    if channel == 12 and state == 1:
        canvas.itemconfig(grp12,fill="yellow")
    if channel == 13 and state == 1:
        canvas.itemconfig(grp13,fill="yellow")
    if channel == 14 and state == 1:
        canvas.itemconfig(grp14,fill="yellow")
    if channel == 15 and state == 1:
        canvas.itemconfig(grp15,fill="yellow")
    if channel == 1 and state == 0:
        canvas.itemconfig(grp1,fill="white")
    if channel == 2 and state == 0:
        canvas.itemconfig(grp2,fill="white")
    if channel == 3 and state == 0:
        canvas.itemconfig(grp3,fill="white")
    if channel == 4 and state == 0:
        canvas.itemconfig(grp4,fill="white")
    if channel == 5 and state == 0:
        canvas.itemconfig(grp5,fill="white")
    if channel == 6 and state == 0:
        canvas.itemconfig(grp6,fill="white")
    if channel == 7 and state == 0:
        canvas.itemconfig(grp7,fill="white")
    if channel == 8 and state == 0:
        canvas.itemconfig(grp8,fill="white")
    if channel == 9 and state == 0:
        canvas.itemconfig(grp9,fill="white")
    if channel == 10 and state == 0:
        canvas.itemconfig(grp10,fill="white")
    if channel == 11 and state == 0:
        canvas.itemconfig(grp11,fill="white")
    if channel == 12 and state == 0:
        canvas.itemconfig(grp12,fill="white")
    if channel == 13 and state == 0:
        canvas.itemconfig(grp13,fill="white")
    if channel == 14 and state == 0:
        canvas.itemconfig(grp14,fill="white")
    if channel == 15 and state == 0:
        canvas.itemconfig(grp15,fill="white")



def channelWrite(channel, value):
    #mydmx.setChannel(channel+1, value) # need to add 1 to the channel value because the module is buggy
    print ("Channel", channel, value)  # prints values to console

def playMusic():
    #global mydmx
    data = wf.readframes(CHUNK)

    # Open the instruction file (with all the lighting cues) and load data into a matrix
    lights =  open("instructions")
    lines = lights.readlines()
    lightseq = [[int(val) for val in line.split()] for line in lines[0:]] # python magic i took from stackoverflow
    # now lightseq is a 2d array with all the values

    # jump forward
    n_frames = int(round(float(STARTAT)/1000 * wf.getframerate()))
    wf.setpos(n_frames)
    cue = 0 # 0-indexed position when going through the list of cues (lightseq)

    update = False

    # loop to pass in music
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)
        # get elapsed time in milliseconds
        global elapsedtime
        elapsedtime = 1000*wf.tell()/wf.getframerate() + OFFSET
        # run through instruction set and operate all instructions that are relevant
        while (cue < len(lightseq) and lightseq[cue][0] <= elapsedtime):
            channelWrite(lightseq[cue][1], 255 if lightseq[cue][2] else 0)
            editGUI(lightseq[cue][1],lightseq[cue][2])
            print ("elapsed:  ", elapsedtime)
            print ("cue    :  ", lightseq[cue][0])
            print ("-------------")
            cue+=1
            update = True
        if(update == True):
            root.update()
            update = False
            #mydmx.render()
    # stop stream (4)
    stream.stop_stream()
    stream.close()
    p.terminate()

def stopMusic():
    stream.stop_stream()
    stream.close()
    p.terminate()

try:
    # time.sleep(5) # buffer to allow me to start recording
    playMusic()
except KeyboardInterrupt:   # to stop playing, press "ctrl-c"
    stopMusic()
    #mydmx.clear(0)
    print ("\nPlay Stopped by user")
    print (elapsedtime)
except Exception as e:
    print (e)
