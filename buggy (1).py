# this program is hereby blessed by our lord and saviour, his exellency Dr Hon

# i'm working with this buggy dmx module named pysimpledmx so i copied
# the source file and renamed it hondmx before fixing some of the bugs inside

import pyaudio
import wave
import sys
import hondmx
import time
mydmx = hondmx.DMXConnection('COM4') # connect to COM(2+1) = COM3
mydmx.render()


CHUNK = 512
OFFSET = 0 # time offset in milliseconds, positive means program thinks elapsed time is larger than it is
STARTAT = 0 # offset to start music at in milliseconds

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

# a function to set dmx channel to value
# don't forget to call mydmx.render() after all the setChannel()s are done
def channelWrite(channel, value):
    mydmx.setChannel(channel+1, value) # need to add 1 to the channel value because the module is buggy
    #print ("Channel", channel, value)  # prints values to console

def playMusic():
    global mydmx
    data = wf.readframes(CHUNK)
    starttime = int(round(stream.get_time()*1000)) # set starttime offset in milliseconds because get_time() gives some weird big number

    # Open the instruction file (with all the lighting cues) and load data into a matrix
    lights =  open("instructions lol.txt")
    lines = lights.readlines()
    lightseq = [[int(val) for val in line.split()] for line in lines[0:]] # python magic i took from stackoverflow
    # now lightseq is a 2d array with all the values

    # jump forward
    n_frames = int(float(STARTAT)/1000 * wf.getframerate())
    wf.setpos(n_frames)
    cue = 0 # 0-indexed position when going through the list of cues (lightseq)

    update = False

    # loop to pass in music
    while len(data) > 0:
        # get elapsed time in milliseconds
        elapsedtime = int(round(stream.get_time()*1000)) - starttime + OFFSET + STARTAT
        # run through instruction set and operate all instructions that are relevant
        while (cue < len(lightseq) and lightseq[cue][0] <= elapsedtime):
            channelWrite(lightseq[cue][1], 255 if lightseq[cue][2] else 0)
            #print (elapsedtime)
            #print (lightseq[cue][0])
            #print ("-------------")
            cue+=1
            update = True
        if(update == True):
            mydmx.render()

        stream.write(data)
        data = wf.readframes(CHUNK)
    # stop stream (4)
    stream.stop_stream()
    stream.close()
    p.terminate()

def stopMusic():
    stream.stop_stream()
    stream.close()
    p.terminate()

try:
    playMusic()
except KeyboardInterrupt:   # to stop playing, press "ctrl-c"
    stopMusic()
    mydmx.clear(0)
    print ("\nPlay Stopped by user")
except Exception as e:
    print (e)
