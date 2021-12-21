from tkinter import *
from tkinter import PhotoImage
import PIL
from PIL import Image
import PIL.ImageTk
import math
root=Tk()

#img=Image.open("1.ico")
#img=img.resize((64,64),Image.ANTIALIAS)
#root.iconphoto(True,PhotoImage(file=img))
#root.iconbitmap('calculator.ico')'''

root.title("CALCULATOR")
root.geometry("480x217")
root.resizable(0,0)


result=StringVar()
def Radian():
    E1.insert("end","radians(")  #convert degree to radian
def degree():
    E1.insert("end","degrees(") #convert radian to degree
def factorial():
    E1.insert("end","factorial(")
def leftbracket():
    E1.insert("end","(")
def rightbracket():
    E1.insert("end",")")
def percentage():
    E1.insert("end","%")
def AC():
    E1.delete(0,"end")
def inverse():
    
    Button(f3, text="sin",width=5,command=sin).destroy
    Button(f4, text="cos",width=5,command=cos).destroy
    Button(f5, text="tan",width=5,command=tan).destroy
    
    Button(f3, text="sin-1",width=5,command=Invsin).grid(row=3,column=2)
    Button(f4, text="cos-1",width=5,command=Invcos).grid(row=4,column=2)
    Button(f5, text="tan-1",width=5,command=Invtan).grid(row=5,column=2)


def Invtan():
    E1.insert("end","atan(")
def Invsin():
    E1.insert("end","asin(")
def Invcos():
    E1.insert("end","acos(")
   
    
def sin():
    E1.insert("end","sin(")
def ln():
    E1.insert("end","ln(")
def num7():
    E1.insert("end",7)
def num8():
    E1.insert("end",8)
def num9():
    E1.insert("end",9)
def divide():
    E1.insert("end","/")
def pie():
    E1.insert("end",3.14)
def cos():
    E1.insert("end","cos(")
def log():
    E1.insert("end","log(")
def num4():
    E1.insert("end",4)
def num5():
    E1.insert("end",5)
def num6():
    E1.insert("end",6)
def multiply():
    E1.insert("end","*")
def e_val():
    E1.insert("end","e")
def tan():
    E1.insert("end","tan(")
def squareroot():
    E1.insert("end","√(")
def num1():
    
    E1.insert("end",1)
    
    
def num2():

    E1.insert("end",2)
    
def num3():

    E1.insert("end",3)
    
def subtract():
    E1.insert("end","-")
def answer():
    
    print(answer)

def exponential():
    E1.insert("end","exp(")
def power():
    E1.insert("end","^")
def num0():
    E1.insert("end",0)
def point():
    E1.insert("end",".")
def plus():
    E1.insert("end","+")

def equal():
    x=E1.get()  
    func=["log10","sin","radians","degrees","factorial","cos","tan","asin","acos","atan","exp","e","log","sqrt"]
    func1={"log":"math.log10","sin":"math.sin","radians":"math.radians","degrees":"math.degrees","factorial":"math.factorial","cos":"math.cos","tan":"math.tan","asin":"math.asin","acos":"math.acos","atan":"math.atan","exp":"math.exp","e":"math.e","ln":"math.log","√":"math.sqrt","%":"*0.01","^":"**"}
   
    for i, j in func1.items():    
        x = x.replace(i, j)
    print(x)
    ans=eval(x)
    result.set(ans)

    global answer
    answer=ans
    E1.update()

result=StringVar()

#FRAMES
f1=Frame(root,width=15,height=50,borderwidth=2,relief=SUNKEN,bg="skyblue")
f1.grid(row=1)
f2=Frame(root,height=10,borderwidth=2,relief=SUNKEN,bg="skyblue")
f2.grid(row=2)
f3=Frame(root,height=10,borderwidth=2,relief=SUNKEN,bg="skyblue")
f3.grid(row=3)
f4=Frame(root,height=10,borderwidth=2,relief=SUNKEN,bg="skyblue")
f4.grid(row=4)
f5=Frame(root,height=10,borderwidth=2,relief=SUNKEN,bg="skyblue")
f5.grid(row=5)
f6=Frame(root,height=10,borderwidth=2,relief=SUNKEN,bg="skyblue")
f6.grid(row=6)

E1=Entry(f1,textvariable=result,width=36,font="timesnewroman 20 bold")
E1.grid(column=0,row=1)
#BUTTONS:



Button(f2, text="Rad",width=5,command=Radian).grid(row=2,column=1)
Button(f2, text="Deg",width=5,command=degree).grid(row=2,column=2)
Button(f2, text="x!",width=5,command=factorial).grid(row=2,column=3)
Button(f2, text="(",width=5,command=leftbracket).grid(row=2,column=4)
Button(f2, text=")",width=5,command=rightbracket).grid(row=2,column=5)
Button(f2, text="%",width=5,command=percentage).grid(row=2,column=6)
Button(f2, text="AC",width=5,command=AC).grid(row=2,column=7)


Button(f3, text="Inv",width=5,command=inverse).grid(row=3,column=1)
Button(f3, text="sin",width=5,command=sin).grid(row=3,column=2)
Button(f3, text="ln",width=5,command=ln).grid(row=3,column=3)
Button(f3, text=7,width=5,command=num7).grid(row=3,column=4)
Button(f3, text=8,width=5,command=num8).grid(row=3,column=5)
Button(f3, text=9,width=5,command=num9).grid(row=3,column=6)
Button(f3, text="÷",width=5,command=divide).grid(row=3,column=7)


Button(f4, text="π",width=5,command=pie).grid(row=4,column=1)
Button(f4, text="cos",width=5,command=cos).grid(row=4,column=2)
Button(f4, text="log",width=5,command=log).grid(row=4,column=3)
Button(f4, text=4,width=5,command=num4).grid(row=4,column=4)
Button(f4, text=5,width=5,command=num5).grid(row=4,column=5)
Button(f4, text=6,width=5,command=num6).grid(row=4,column=6)
Button(f4, text="x",width=5,command=multiply).grid(row=4,column=7)

Button(f5, text="e",width=5,command=e_val).grid(row=5,column=1)
Button(f5, text="tan",width=5,command=tan).grid(row=5,column=2)
Button(f5, text="√",width=5,command=squareroot).grid(row=5,column=3)
Button(f5, text=1,width=5,command=num1).grid(row=5,column=4)
Button(f5, text=2,width=5,command=num2).grid(row=5,column=5)
Button(f5, text=3,width=5,command=num3).grid(row=5,column=6)
Button(f5, text="-",width=5,command=subtract).grid(row=5,column=7)

Button(f6, text="Ans",width=5,command=answer).grid(row=6,column=1)
Button(f6, text="EXP",width=5,command=exponential).grid(row=6,column=2)
Button(f6, text="x^y",width=5,command=power).grid(row=6,column=3)
Button(f6, text=0,width=5,command=num0).grid(row=6,column=4)
Button(f6, text=".",width=5,command=point).grid(row=6,column=5)
Button(f6, text="=",width=5,command=equal).grid(row=6,column=6)
Button(f6, text="+",width=5,command=plus).grid(row=6,column=7)











root.mainloop()