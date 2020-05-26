import turtle
from turtle import bye
import time
import random

posponer = 0.1
score = 0
high_score = 0

# Config ventana
wn = turtle.Screen()
wn.title("----Snake----")
wn.bgcolor("black")
wn.setup(width=620, height=620)
wn.tracer(0)

# cabeza serpiente

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(50, 20)

# cuerpo

segmento = []

# texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0		High Score: 0", align = "center", font=("Courier", 20, "normal"))


# funciones movimiento

def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def derecha():
    cabeza.direction = "right"


def izquierda():
    cabeza.direction = "left"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    # colision borde
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        # borrar segmentos
        for cuerpo in segmento:
            cuerpo.hideturtle()

        segmento.clear()

        #reset marcador
        score = 0
        texto.clear()
        texto.write("Score: {}		High Score: {}".format(score,high_score),
                    align="center", font=("Courier", 20, "normal"))


    # colision comida

    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        cuerpo = turtle.Turtle()
        cuerpo.speed(0)
        cuerpo.shape("square")
        cuerpo.color("green")
        cuerpo.penup()
        segmento.append(cuerpo)

        #aumentar marcador
        score +=10

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}		High Score: {}".format(score,high_score),
                    align="center", font=("Courier", 20, "normal"))

    # Mover cuerpo
    totalCuerpo = len(segmento)
    for index in range(totalCuerpo - 1, 0, -1):
        x = segmento[index - 1].xcor()
        y = segmento[index - 1].ycor()
        segmento[index].goto(x, y)
    if totalCuerpo > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmento[0].goto(x, y)

    mov()

    #colision Cuerpo
    for cuerpo in segmento:
        if cuerpo.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            # borrar segmentos
            for cuerpo in segmento:
                cuerpo.hideturtle()

            segmento.clear()
            score = 0
            texto.clear()
            texto.write("Score: {}		High Score: {}".format(score, high_score),
                        align="center", font=("Courier", 20, "normal"))


    time.sleep(posponer)
    turtle.onkeypress(bye,"q")



