"""
antenna.py is a program designed to draw a fractal antenna with differing levels and lengths as defined by user input.
The program checks user input as to ensure function, and then uses two different functions to recursively create the shape.

author: Max Klot
"""
import turtle
import math
def main():
    """
    Main function; prompts user, checks input, sets up turtle, calls drawing functions.
    :return: None
    """
    length = 0.0
    val = 0
    while True:
        try:
            x = input("Please enter the length of the antenna in pixels: ")
            length = float(x)
            break
        except ValueError:
            print("Oops!  Value must be a float. You entered " + x)
    while True:
        try:
            x = input("Please enter the number of levels: ")
            val = int(x)
            break
        except ValueError:
            print("Oops!  Value must be an integer. You entered " + x)
    turtle.left(45)
    turtle.speed(0)
    print("Strategy 1- Antenna's length is " + str(strategy1(length, val)) + " units")
    enter = False
    while not enter:
        enter = "" == input("Hit enter to continue")
    turtle.reset()
    turtle.speed(0)
    turtle.left(45)
    print("Strategy 2- Antenna's length is " + str(strategy2(length, val)) + " units")
    print("Bye!")


def strategy2(n: float, levels: int) -> float:
    """
    Strategy 2 draws the antenna by drawing each of the individual squares as the base case and then recursively calling
    itself to continue the pattern.
    :param n: the total length of one side of the fractal antenna
    :param levels: number of levels in antenna drawing
    :return: float, the total length turtle travelled to draw the antenna shape
    """
    total = 0.0
    if levels == 1:
        total1 = 0.0
        turtle.penup()
        turtle.forward(n / 2)
        turtle.left(90)
        turtle.forward(n / 2)
        turtle.left(90)
        turtle.pendown()
        for i in range(4):
            turtle.forward(n)
            turtle.left(90)
            total1 += n
        turtle.penup()
        turtle.right(90)
        turtle.back(n / 2)
        turtle.right(90)
        turtle.back(n / 2)
        return total1
    elif levels > 1:
        total += strategy2(n / 3, levels - 1)
        turtle.forward(n / 3)
        turtle.right(90)
        turtle.forward(n / 3)
        total += strategy2(n / 3, levels - 1)
        turtle.back(n / 3)
        turtle.left(90)
        turtle.back(n / 3)
        turtle.forward(n / 3)
        turtle.left(90)
        turtle.forward(n / 3)
        total += strategy2(n / 3, levels - 1)
        turtle.back(n / 3)
        turtle.right(90)
        turtle.back(n / 3)
        turtle.right(180)
        turtle.forward(n / 3)
        turtle.right(90)
        turtle.forward(n / 3)
        total += strategy2(n / 3, levels - 1)
        turtle.back(n / 3)
        turtle.left(90)
        turtle.back(n / 3)
        turtle.left(180)
        turtle.right(180)
        turtle.forward(n / 3)
        turtle.left(90)
        turtle.forward(n / 3)
        total += strategy2(n / 3, levels - 1)
        turtle.back(n / 3)
        turtle.right(90)
        turtle.backward(n / 3)
        turtle.left(180)

    return total


def strategy1(n: float, levels: int) -> float:
    """
    strategy1 draws the antenna by recursively using a pattern that helps create the antenna.
    In every case it will iterate four times (in draws base case, a single line is drawn, so outside of draw,
    a square is made)
    :param n: the total length of one side of the fractal antenna
    :param levels: the number of levels of the fractal antenna
    :return: float, the total length turtle travelled to draw the antenna shape
    """
    total1 = 0.0
    def draw(n1: float, levels1: int) -> float:
        """
        draw will draw the pattern that is iteratively and recursively called to create the antenna. In its
        base case draw will make as single line
        :param n1:
        :param levels1:
        :return: will return the length of one quarter of the defined antennas total length
        """
        if levels1 == 1:
            turtle.forward(n1)
            return n1

        elif levels1 > 1:
            total = 0
            total += draw(n1 / 3, levels1 - 1)
            turtle.left(90)
            total += draw(n1 / 3, levels1 - 1)
            turtle.right(90)
            total += draw(n1 / 3, levels1 - 1)
            turtle.right(90)
            total += draw(n1 / 3, levels1 - 1)
            turtle.left(90)
            total += draw(n1 / 3, levels1 - 1)
            return total
        else:
            pass

    turtle.up()
    distTrav = (n / 2) * math.sqrt(2)
    turtle.right(135)
    turtle.forward(distTrav)
    turtle.left(135)
    turtle.down()

    for i in range(0, 4):
        total1 += draw(n, levels)
        turtle.left(90)
    return total1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
