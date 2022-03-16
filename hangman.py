from random import choice
import turtle
from math import cos, radians

def ifContains(letter):
	if letter in picked_word:
		return True
	else:
		return False

def switch(error):
	match error:
		case 1:
			turtle.penup()
			turtle.right(90)
			turtle.forward(20)
			turtle.left(90)
			turtle.forward(20)
			turtle.pendown()
			turtle.circle(20)
		case 2:
			turtle.left(90)
			turtle.penup()
			turtle.forward(20)
			turtle.right(90)
			turtle.forward(20)
			turtle.pendown()
			turtle.forward(40)
			turtle.backward(40)
		case 3:
			turtle.right(45)
			turtle.forward(20)
			turtle.backward(20)
			turtle.left(45)
		case 4:
			turtle.left(45)
			turtle.forward(20)
			turtle.backward(20)
			turtle.right(45)
			turtle.forward(40)

		case 5:
			turtle.right(45)
			turtle.forward(20)
			turtle.backward(20)
			turtle.left(45)

		case 6:
			turtle.left(45)
			turtle.forward(20)
			turtle.backward(20)
			turtle.right(45)

def ifContains2(letter):
	if letter in tl:
		return True
	else:
		return False

def fill_word(letter):
	for i in range(len(picked_word)):
		if picked_word[i] == letter:
			tl[i] = picked_word[i]
	return tl

def draw_platform(counter):
	if counter<1:
		turtle.begin_fill()
		turtle.pendown()
		turtle.left(180)
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(250)
		turtle.left(90)
		turtle.forward(10)
		turtle.left(90)
		turtle.forward(250)
		turtle.right(90)
		turtle.forward(40)
		turtle.right(90)
		turtle.forward(50)

def eye(col, rad):
    pen.down()
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.up()

def draw_smile_face():
    # draw face
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(200)
    pen.end_fill()
    pen.up()
     
    # draw eyes
    pen.goto(-60, 75)
    eye('white', 15)
    pen.goto(-60, 75)
    eye('black', 5)
    pen.goto(60, 75)
    eye('white', 15)
    pen.goto(60, 75)
    eye('black', 5)
     
    # draw nose
    pen.goto(0, 20)
    eye('black', 8)
     
    # draw mouth
    pen.goto(-60, -40)
    pen.down()
    pen.right(90)
    pen.circle(60, 180)
    pen.up()
     
    # draw tongue
    pen.goto(-10, -100)
    pen.down()
    pen.right(180)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(10, 180)
    pen.end_fill()
    pen.hideturtle()

words = ["fadi","alaa","lozan","abdalla","osnat"]
picked_word = choice(words)
till_now_word = ''
# turtle object
pen = turtle.Turtle()
 
for i in range(len(picked_word)):
	till_now_word += '_'

tl = list(till_now_word)
num_of_errors = 0

turtle.bgcolor("white")
x = 1
hue = 0
angle = 1
turtle.color("black")
X = 50
Y = 50

pen.right(90)
pen.forward(250)
pen.left(90)
counter = 0
while True:

	draw_platform(counter)	
	counter+=1
	print("Hangman game:\n"
		+ "the word is a name of a family member"
		+"\nand you got 6 tries")
	picked_char = input("Enter a letter\n")

	turtle.color("red")
	turtle.width(2)
	if ifContains(picked_char):
		t = "".join(fill_word(picked_char))
		print(t)
		
		result = ifContains2("_")

		if result == False:
			turtle.penup()
			draw_smile_face()
			input("sadf")
			exit("Congratz! finished the word")

	else:
		num_of_errors += 1
		switch(num_of_errors)
		if num_of_errors == 6:
			input("reached max num of errors : 6 \nbetter luck next time\npress any key to exit")
			exit()

		print("the word doesnt contain " + picked_char + "\n")
turtle.end_fill()