#! /usr/bin/python3

from tkinter import *
from tkinter import font
import tkinter as tk
import RPi.GPIO as GPIO
import time
from functools import partial
# Hard
GPIO.setmode(GPIO.BOARD)
GPIO.setup (40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
GPIO.setup (18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)

# Top
win = tk.Tk() 
win.title("GUI GPIO")
#win.geometry('600x380') 
#appHighlightFont= font.Font(family='Helvetica', size = 12, weight = 'bold')
myFont = font.Font(family = 'Helvetica', size = 12, weight = 'bold')
font.families()

def ledToggle(pin):
        if GPIO.input(pin) :
                GPIO.output(pin,GPIO.LOW)
                upBtT1("LED OFF",pin) 
                print( str(pin)+ ' LED turned Off')
                #ledButton1["text"] = "LED ON"
        else:
                GPIO.output(pin,GPIO.HIGH)
                upBtT1("LED ON",pin)
                print( str(pin)+ ' LED turned On')
                #ledButton1["text"] = "LED OFF"
def upBtT1(t,pi):
	if pi==40 :
		bt_var1.set(t)
	if pi==18 :
		bt_var2.set(t)
bt_var1=StringVar()
bt_var2=StringVar()
upBtT1("Click !!",18)
upBtT1("Click !!",40)

def exitProgram():
        print("Exit Button pressed")
        GPIO.cleanup()
        win.quit()	
#modif
def blink2(pin):
        for i in range(0,6):  
                blink(pin)
        #blink(40)
        
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(0.2)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(0.1)  
        #return  
# blink GPIO40 & GPIO18 4 Times 
#for i in range(0,3):  
blink(40)
blink(18)
#GPIO.cleanup()



def upBtT():
	bt_var.set("b")
bt_var=StringVar()

	


#layOut


Button(win,textvariable=bt_var1, font = myFont, height = 2, width =8 ,
	command = partial(ledToggle,40)			
	).grid(column=2, row=1) 
Button(win,textvariable=bt_var2, font = myFont, height = 2, width =8 ,
	command = partial(ledToggle,18)			
	).grid(column=2, row=2) 
	

ledButton2 = Button(win, text = "Blink Led 40", font = myFont, height = 2, width =8 , 
	command = partial(blink2,40)	
	).grid(column=2, row=3)

ledButton3 = Button(win, text = "Blink Led 18", font = myFont , height = 2, width =8 ,
	command = partial(blink2,18)
	).grid(column=2, row=4)

exitButton  = Button(win, text = "Exit", 	font = myFont , height =2 , width = 6,
	command = exitProgram
	).grid(column=1, row=5)


Label(win, text="Toggel LED 1 :").grid(column=1, row=1)
Label(win, text="Toggel LED 2 :").grid(column=1, row=2)

Label(win, text="Blink_40 LED 1 :").grid(column=1, row=3)
Label(win, text="Blink_18 LED 2 :").grid(column=1, row=4)

Entry(win, text = "", font = myFont ).grid(column=2, row=5) 


mainloop()
