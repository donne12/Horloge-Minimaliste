
from tkinter import*
from math import*
from time import*

x, y, ang, a, b, res, flag, e, x2, y2, ang2, f, x3, y3, ang3 = 150., 30., pi, 150., 30., pi, 0, 0, 150., 30., pi, 0, 150., 30., pi
seconde, minute, heure = "", "", ""
def trace_horloge():
    global x, y, ang, e, flag, seconde, minute, heure
    if flag == 0:
        flag = 1
        can.create_oval(27, 27, 273, 273, fill='#eeeeee', width=2)
        can.create_text(150, 18, text='12', fill='black')
        can.create_line(150, 30, 150, 45, fill='black', width=2)
        can.create_text(280, 150, text='3', fill='black')
        can.create_line(270, 150, 255, 150, fill='black', width=2)
        can.create_text(150, 280, text='6', fill='black')
        can.create_line(150, 270, 150, 255, fill='black', width=2)
        can.create_text(20, 150, text='9', fill='black')
        can.create_text(220, 40, text='1', fill='red')
        can.create_text(265, 90, text='2', fill='red')
        can.create_text(265, 210, text='4', fill='red')
        can.create_text(220, 260, text='5', fill='red')
        can.create_text(80, 260, text='7', fill='red')
        can.create_text(30, 210, text='8', fill='red')
        can.create_text(30, 90, text='10', fill='red')
        can.create_text(80, 40, text='11', fill='red')
        can.create_line(30, 150, 45, 150, fill='black', width=2)
        can.create_oval(145, 145, 155, 155, fill='#999999')
        traits()    
        seconde = can.create_line(10, 10, 10, 10, fill='red', arrow=LAST)
        minute = can.create_line(10, 10, 10, 10, fill='black', arrow=LAST)
        heure = can.create_line(10, 10, 10, 10, fill='#00cc00', arrow=LAST)
        aff_heure()
    ang = ang + 2*pi/60
    x, y = sin(ang), cos(ang)
    x, y = x*120 + 150, y*120 + 150
    if e < 60:
        if e == 59 or e == 14 or e == 29 or e == 44:
            can.create_oval(x-3, y-3, x+3, y+3, fill='black')
        e += 1
        root.after(25, trace_horloge)
        

def traits():
    global x2, y2, ang2, f, x3, y3
    ang2 = ang2 + 2*pi/60
    x2, y2 = sin(ang2), cos(ang2)
    x2, y2 = x2*120 + 150, y2*120 + 150
    x3, y3 = sin(ang2), cos(ang2)
    x3, y3 = x3*110 + 150, y3*110 + 150
    if f < 60:
        can.create_line(x2, y2, x3, y3, fill='black', width=1)
        if f == 4 or f == 9 or f == 19 or f == 24 or f == 34 or f == 39 or f == 49 or f == 54:
            can.create_line(x2, y2, x3, y3, fill='red', width=1)
        f += 1
        root.after(25, traits)

def aff_heure():
    global a, b , res, plusdeure
    he = localtime()
    ts = he[5]+0.0
    tm = he[4]+ts/60
    th = he[3]+tm/60
    res = -(ts-30)*2*pi/60
    rem = -(tm-30)*2*pi/60
    reh = -(th-30)*2*pi/12
    a, b = sin(res), cos(res)
    c, d = sin(rem), cos(rem)
    e, f = sin(reh), cos(reh)
    a, b = a*120 + 150, b*120 + 150
    c, d = c*100 + 150, d*100 + 150
    e, f = e*80 + 150, f*80 + 150
    txte.configure(text=str(he[3])+str(strftime(":%M:%S", gmtime())))
    can.coords(seconde, 150, 150, a, b)
    can.coords(minute, 150, 150, c, d)
    can.coords(heure, 150, 150, e, f)
    root.after(1000, aff_heure)
	
                                       ############ Programme principal #############
root = Tk()
root.title("L'horloge")
can = Canvas(root, width=300, height=300, bg='white', relief=SUNKEN)
can.pack()
txte = Label(root, text='', bg='white', width=30)
txte.pack()
trace_horloge()
root.mainloop()
