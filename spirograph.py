import turtle

t = turtle.Pen()

sides=0
length=0

print('Welcome to the Spirographer!')
print()

while(sides <= 2):
    sides = int(input('How many sides do you want the polygon to have? '))
    if(sides <= 2):
        print('Your polygon must have at least three sides.')
while(length <= 0):
    length = int(input('What do you want the length of each side of the polygon to be? '))
    if(sides <= 0):
        print('The length of each side of your polygon must be more than 0.')
angleSum = (sides - 2) * 180
angle = abs((angleSum / sides) - 180)

while True:
    for i in range(0, sides):
        t.forward(length)
        t.left(angle)
    t.left(1)

