import turtle
from math import *

koch_size = 600
koch_step = 0
message = """
마우스를 클릭할 때마다 코흐의 눈송이 곡선을 더 자세히 그립니다.

주의 : 그림이 모두 그려지기 전에 마우스를 클릭하면 오류가 발생합니다.

마우스 클릭으로 시작 : 빠른 그림 그리기





                                                             - 유한주 - 
"""

square = float()
pos_list = []
width_list = []
turtle.title('코흐의 곡선 그리기')
turtle.bgcolor('black')
turtle.color('sky blue', 'white')
turtle.hideturtle()


def koch_draw(length, step):
    global pos_list

    if step > 0:
        length = length/3
        for angle in [60, -120, 60, 0]:
            koch_draw(length, step-1)
            turtle.left(angle)
    else:
        turtle.forward(length)
        pos_list.append(turtle.pos())
        


# 코흐의 눈송이의 중심이 원점에 오도록 위치를 설정
turtle.penup()
turtle.goto(0, -100)
turtle.write(message, False, 'center', ('',15))
turtle.home()
turtle.backward(koch_size/sqrt(3))
turtle.left(30)
turtle.pendown()
turtle.color('red', 'white')

# 코흐 눈송이 그리는 코드
def draw_koch(x, y):
    global koch_step, square, pos_list

    pos_list = [turtle.pos()]

    turtle.clear()
    turtle.tracer(100)  
    turtle.begin_fill()  
    for i in range(3):
        koch_draw(koch_size, koch_step)
        turtle.left(-120)
    turtle.end_fill()  
    turtle.update()

    f = open("pos_%d.txt"%koch_step, mode='wt', encoding='utf-8')
    for i in pos_list:
        f.write('%s\n' %str(i))
    f.close()

    triangle_a = abs(sqrt((pos_list[1][0]-pos_list[0][0])**2 + (pos_list[1][1]- pos_list[0][1])**2))

    # 첫번째 삼각형의 한 변의 길이를 '600'이라고했으니 첫번째 삼각형의 넓이는 'sqrt(3)/4 * 600^2'.
    if koch_step == 0:
        square = (sqrt(3) / 4) * (triangle_a**2)

        width_list.append(square)

    elif koch_step > 0 :

        square = (sqrt(3)/4) * (3*(4**(koch_step-1))) * (triangle_a**2)

        width_list.append(square)
    
    square = sum(width_list)
        
    # 한 선분의 길이 = triangle_a
    length = float(triangle_a * 3 * (4**koch_step))

    value = """
    한 변의 길이 : %f
    넓이 : %f
    둘레 : %f
    """ %(float(triangle_a), square, length)

    turtle.color("orange")
    turtle.penup()
    turtle.right(40)
    turtle.forward(325)
    turtle.write(value, False, 'center', ('', 15, 'bold'))
    turtle.color("red", "white")
    turtle.backward(325)
    turtle.left(40)
    turtle.pendown()
    

    koch_step += 1

turtle.onscreenclick(draw_koch)
turtle.listen()
turtle.done()
