#   a123_apple_1.py
import turtle as trtl
import random
#list for what button to click later
thewholealphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#-----setup-----
doneorno = 5
rand1ap = random.choice(thewholealphabet)
rand2ap = random.choice(thewholealphabet)
rand3ap = random.choice(thewholealphabet)
rand4ap = random.choice(thewholealphabet)
rand5ap = random.choice(thewholealphabet)

#while input so then two apples dont have the same letter because there is a bug when both apples have the same input
while rand1ap == rand2ap or rand1ap == rand3ap or rand1ap == rand4ap or rand1ap == rand5ap:
  rand1ap = random.choice(thewholealphabet)

while rand2ap == rand1ap or rand2ap == rand3ap or rand2ap == rand4ap or rand2ap == rand5ap:
  rand2ap = random.choice(thewholealphabet)

while rand3ap == rand2ap or rand3ap == rand1ap or rand3ap == rand4ap or rand3ap == rand5ap:
  rand3ap = random.choice(thewholealphabet)

while rand4ap == rand2ap or rand4ap == rand3ap or rand4ap == rand1ap or rand4ap == rand5ap:
  rand4ap = random.choice(thewholealphabet)

while rand5ap == rand2ap or rand5ap == rand3ap or rand5ap == rand4ap or rand5ap == rand1ap:
  rand5ap = random.choice(thewholealphabet)

apoley = 0
apoley2 = 0
apoley3 = 0
apoley4 = 0
apoley5 = 0

#these are all my different apple images that generate, go to their positions and write the letter needed to be pressed
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
apple.setpos(-50,0)
apple.color("blue")
apple.write(rand1ap, font=("Arial", 50, "bold"))

apple2_image = "apple.gif"
wn.addshape(apple2_image)
apple2 = trtl.Turtle()
apple2.penup()
apple2.setpos(-150,0)
apple2.color("red")
apple2.write(rand2ap, font=("Arial", 50, "bold"))

apple3_image = "apple.gif"
wn.addshape(apple3_image)
apple3 = trtl.Turtle()
apple3.penup()
apple3.setpos(50,0)
apple3.color("green")
apple3.write(rand3ap, font=("Arial", 50, "bold"))

apple4_image = "apple.gif"
wn.addshape(apple4_image)
apple4 = trtl.Turtle()
apple4.penup()
apple4.setpos(150,10)
apple4.color("purple")
apple4.write(rand4ap, font=("Arial", 50, "bold"))

apple5_image = "apple.gif"
wn.addshape(apple5_image)
apple5 = trtl.Turtle()
apple5.penup()
apple5.setpos(0,100)
apple5.color("pink")
apple5.write(rand5ap, font=("Arial", 50, "bold"))

#-----functions-----
def appole_fall1_lol():
  global apoley, doneorno
  if apoley == 0:
    apple.right(90)
    while apoley != 100:  
      apple.forward(2)
      apoley = apoley + 1
    apple.left(90)
  doneorno = doneorno - 1
  if doneorno == 0:
    wn = trtl.Screen()
    donezo = trtl.Turtle()
    donezo.hideturtle()
    donezo.penup()
    donezo.setpos(-350,0)
    donezo.color("gold")
    donezo.write("YOU WIN!!", font=("Arial", 100, "bold"))

def appole_fall2_lol():
  global apoley2, doneorno
  if apoley2 == 0:
    apple2.right(90)
    while apoley2 != 100:  
      apple2.forward(2)
      apoley2 = apoley2 + 1
    apple2.left(90)
  doneorno = doneorno - 1
  if doneorno == 0:
    wn = trtl.Screen()
    donezo = trtl.Turtle()
    donezo.hideturtle()
    donezo.penup()
    donezo.setpos(-350,0)
    donezo.color("gold")
    donezo.write("YOU WIN!!", font=("Arial", 100, "bold"))

def appole_fall3_lol():
  global apoley3, doneorno
  if apoley3 == 0:
    apple3.right(90)
    while apoley3 != 100:  
      apple3.forward(2)
      apoley3 = apoley3 + 1
    apple3.left(90)
  doneorno = doneorno - 1
  if doneorno == 0:
    wn = trtl.Screen()
    donezo = trtl.Turtle()
    donezo.hideturtle()
    donezo.penup()
    donezo.setpos(-350,0)
    donezo.color("gold")
    donezo.write("YOU WIN!!", font=("Arial", 100, "bold"))
  
def appole_fall4_lol():
  global apoley4, doneorno
  if apoley4 == 0:
    apple4.right(90)
    while apoley4 != 105:  
      apple4.forward(2)
      apoley4 = apoley4 + 1
    apple4.left(90)
  doneorno = doneorno - 1
  if doneorno == 0:
    wn = trtl.Screen()
    donezo = trtl.Turtle()
    donezo.hideturtle()
    donezo.penup()
    donezo.setpos(-350,0)
    donezo.color("gold")
    donezo.write("YOU WIN!!", font=("Arial", 100, "bold"))
  
def appole_fall5_lol():
  global apoley5, doneorno
  if apoley5 == 0:
    apple5.right(90)
    while apoley5 != 150:  
      apple5.forward(2)
      apoley5 = apoley5 + 1
    apple5.left(90)
  doneorno = doneorno - 1
  if doneorno == 0:
    wn = trtl.Screen()
    donezo = trtl.Turtle()
    donezo.hideturtle()
    donezo.penup()
    donezo.setpos(-350,0)
    donezo.color("gold")
    donezo.write("YOU WIN!!", font=("Arial", 100, "bold"))
    
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_apple2(active2_apple):
  active2_apple.shape(apple2_image)
  wn.update()

def draw_apple3(active3_apple):
  active3_apple.shape(apple3_image)
  wn.update()

def draw_apple4(active4_apple):
  active4_apple.shape(apple4_image)
  wn.update()

def draw_apple5(active5_apple):
  active5_apple.shape(apple5_image)
  wn.update()

#-----function calls-----
#draws the apples textures and makes sure to make the apple fall when the certain key is pressed
draw_apple(apple)
draw_apple2(apple2)
draw_apple3(apple3)
draw_apple4(apple4)
draw_apple5(apple5)
wn.onkeypress(appole_fall1_lol, rand1ap)
wn.listen()

wn.onkeypress(appole_fall2_lol, rand2ap)
wn.listen()

wn.onkeypress(appole_fall3_lol, rand3ap)
wn.listen()

wn.onkeypress(appole_fall4_lol, rand4ap)
wn.listen()

wn.onkeypress(appole_fall5_lol, rand5ap)
wn.listen()

wn.mainloop()