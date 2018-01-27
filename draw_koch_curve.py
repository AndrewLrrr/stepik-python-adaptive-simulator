import argparse
import turtle
import time

from koch_curve import koch_curve_turns


def turtle_koch_curve(n, delay, line_length=10):
    for move in koch_curve_turns(n):
        turtle.forward(line_length)
        turtle.left(move)
        time.sleep(delay)
    turtle.forward(line_length)
    turtle.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delay', default='0.2')
    parser.add_argument('-n', '--number', default='2')
    args = parser.parse_args()
    turtle_koch_curve(int(args.number), float(args.delay))
