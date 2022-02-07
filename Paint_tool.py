from tkinter import * 
from tkinter import messagebox
click_num=0
draw = ""
colour = ""
x1,y1=None,None
def drawing(event):
  global click_num
  global x1,y1
  
  if click_num==0:
    x1=event.x
    y1=event.y
    click_num+=1
  else:
    x2=event.x
    y2=event.y
    click_num = 0
    if draw == "":
      messagebox.showwarning("Error","Select a Shape")
      raise Exception("No shape is selected")
    #Shape outline will still be drawn if a colour is not selected,
    #so I raise an exception which stops this.
    if colour == "":
      messagebox.showwarning("Error","Select a Colour")
      raise Exception("Sorry, click a Colour")
      
    if draw == "line": 
      c.create_line(x1,y1,x2,y2, fill=colour, width=1)
      
      
    if draw == "oval":
      c.create_oval(x1,y1,x2,y2, fill=colour, width=1)
    
    if draw == "rectangle":
      c.create_rectangle(x1,y1,x2,y2, fill=colour, width=1)
      
def red():
  global colour
  colour = "red"
  current_colour_selection.config(text ="Current Colour: " + colour)
def blue():
  global colour
  colour = "blue"
  current_colour_selection.config(text ="Current Colour: " + colour)
def yellow():
  global colour
  colour = "yellow"
  current_colour_selection.config(text ="Current Colour: " + colour)
def line():
  global draw
  draw = "line"
  current_shape_selection.config(text ="Current Shape " + draw)
  
def rec():
  global draw
  draw = "rectangle"
  current_shape_selection.config(text ="Current Shape: " + draw)
 
def oval():
  global draw
  draw = "oval"
  current_shape_selection.config(text ="Current Shape: " + draw)
  
def reset():
  c.delete('all')
root=Tk()
root.title("Paint Application")
root.geometry("750x550")
button1=Button(root, text="Line",command = line)
button1.place(x=10, y=50)
button2=Button(root, text="Oval", command = oval)
button2.place(x=80, y=50)
button3=Button(root, text="Rectangle",command = rec)
button3.place(x=25, y=100)
button4=Button(root, text="Red",bg = "red", activeforeground = "red",activebackground = "pink", command = red)
button4.place(x=10, y=200)
button5=Button(root, text="Yellow",bg = "yellow", activeforeground = "yellow",activebackground = "#FFC300",command = yellow)
button5.place(x=35, y=250)
button6=Button(root, text="Blue",bg = "blue", activeforeground = "#00E7FF",activebackground = "#0046FF",fg = "white",command = blue)
button6.place(x=80, y=200)
button7=Button(root, text="Clear",bg = "Black",fg = "white",command = reset)
button7.place(x=10, y=350)
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.place(x=80, y=350)
current_shape_selection = Label(root, text = "Current Shape:"+draw)
current_shape_selection.place(x =10, y = 420)
current_colour_selection = Label(root, text = "Current Colour:"+colour)
current_colour_selection.place(x =10, y = 450)

c = Canvas(root,bd = 5,bg = "pink", width = root.winfo_screenwidth(), height = root.winfo_screenheight(),relief=GROOVE)
c.place(x = 200, y= 0)
c.bind('<Button-1>', drawing)
root.mainloop()
