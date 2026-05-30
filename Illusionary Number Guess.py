import turtle
import random

screen = turtle.Screen()
screen.bgcolor("gray")
t = turtle.Turtle()
t.speed(0)
turtle.tracer(0)

def circular_illusion():
    t.pencolor("black")
    for i in range(250):     
        t.circle(150)
        t.left(2)

def show_hidden_number():
    number = random.randint(100, 999)
    t.penup()
    x = random.randint(-120, 120)
    y = random.randint(-120, 120)
    t.goto(x, y)
    t.pendown()
    camouflage_colors = ["lightgray"]
    t.write(number, align="center", font=("Arial", 12))  
    return number

circular_illusion()
answer = show_hidden_number()

choices = [answer, random.randint(100,999), random.randint(100,999)]
random.shuffle(choices)

print("A hidden number is camouflaged inside the circular illusion.")
print("Options:", choices)

guess = int(input("Enter the illusionary Number: "))
if guess == answer:
    print("✅ Correct!")
else:
    print("❌ Wrong! The answer was", answer)

turtle.done()
