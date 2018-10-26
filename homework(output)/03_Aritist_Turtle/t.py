import turtle as t

t.bgcolor('black')
t.speed()

for i in range(200):
    if i % 3 == 0:
        t.color('red')
    if i % 3 == 1:
        t.color('yellow')
    if i % 3 == 2:
        t.color('blue')

    t.forward(i * 2)
    t.left(119)

