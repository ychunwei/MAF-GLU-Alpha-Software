# this program is hereby blessed by our lord and saviour, his exellency Dr Hon
# i'm working with this buggy dmx module named pysimpledmx so i copied
# the source file and renamed it hondmx before fixing some of the bugs inside

import pyaudio
import wave
import sys
import hondmx
import time, dmxlib
#mydmx = dmxlib.DMXConnection('COM4')
#mydmx.render()
from Tkinter import *
#main config stuff
root = Tk()

#width and height vars

w = 1000
h = 1000

elapsedtime = 0
CHUNK = 512
OFFSET = 0 # time offset in milliseconds, positive means program thinks elapsed time is larger than it is
STARTAT =0 # offset to start music at in milliseconds

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
grp=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
txt=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
canvas = Canvas(root, width = w, height = h)
canvas.pack()

lines=[(490,100,100,234),(100,254,100,746),(100,766,480,900),(510,900,900,766),(900,766,900,254),(900,234,510,100),(490,285,300,350),(300,350,300,490),(300,510,300,650),(300,650,490,715),(510,715,700,650),(700,650,700,510),(700,490,700,350),(700,350,510,285),(490,415,400,446),(400,446,400,554),(400,554,490,585),(510,585,600,554),(600,554,600,446),(600,446,510,415)]
for l in lines:
    canvas.create_line(l[0],l[1],l[2],l[3])

positions=[[180,180,220,220],[80,480,120,520],[180,780,220,820],[280,330,320,370],[280,630,320,670],[380,480,420,520],[780,180,820,220],[880,480,920,520],[780,780,820,820],[680,330,720,370],[680,630,720,670],[580,480,620,520],[460,460,540,540],[480,480,520,520],[440,490,460,510],[540,490,560,510]]
i = 0
for p in positions:
    grp[i]=canvas.create_oval(p[0],p[1],p[2],p[3],fill = "white")
    i+=1
coords=[(200,200,'1'),(100,500,'2'),(200,800,'3'),(300,350,'4'),(300,650,'5'),(400,500,'6'),(800,200,'7'),(900,500,'8'),(800,800,'9'),(700,350,'10'),(700,650,'11'),(600,500,'12'),(500,500,'13'),(500,500,'14'),(450,500,'15'),(550,500,'16')]
i=0
for c in coords:
    txt[i] = canvas.create_text(c[0],c[1], text=c[2])
    i+=1


#----------------VAR SETTING ENDS-------------------

root.update()
# this program is hereby blessed by our lord and saviour, his exellency Dr Hon

# i'm working with this buggy dmx module named pysimpledmx so i copied
# the source file and renamed it hondmx before fixing some of the bugs inside




# a function to set dmx channel to value
# don't forget to call mydmx.render() after all the setChannel()s are done
def editGUI(channel,state):
    for i in range (0,16):
        if channel == i+1 and state == 1:
           canvas.itemconfig(grp[i],fill="yellow")
        elif channel ==i+1 and state == 0:
           canvas.itemconfig(grp[i],fill="white")
        i += 1
    #print ("Channel", channel, state)
    


#def channelWrite(channel, value):
    #mydmx.setChannel(channel+1, value) # need to add 1 to the channel value because the module is buggy
    #print ("Channel", channel, value)  # prints values to console
    
def playMusic():
    #global mydmx
    data = wf.readframes(CHUNK)

    # Open the instruction file (with all the lighting cues) and load data into a matrix
    lights =  open("instructions.txt")
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
            #channelWrite(lightseq[cue][1], 255 if lightseq[cue][2] else 0)
            editGUI(lightseq[cue][1],lightseq[cue][2])
            #print ("elapsed:  ", elapsedtime)
            #print ("cue    :  ", lightseq[cue][0])
            #print ("-------------")
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
    time.sleep(5) # buffer to allow me to start recording
    playMusic()
except KeyboardInterrupt:   # to stop playing, press "ctrl-c"
    stopMusic()
    #mydmx.clear(0)
    print ("\nPlay Stopped by user")
    print (elapsedtime)
except Exception as e:
    print (e)
