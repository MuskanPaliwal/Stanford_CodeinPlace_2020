# Hospital Karel Solution code
# Created during Section 313, Week 1
# SL: MuskanPaliwal
# 2020/04/22

from karel.stanfordkarel import *


def turn_right():
    """
    Preconditions: Karel is in a valid state (not crashed)
    Post-conditions: Karel has made a 270 degree clockwise turn
    :return:
    """
    for i in range(3):
        turn_left()


def put_three_beepers():
    """
    Precondition: Karel is facing in the correct direction, 2 corners in front must be free
    Post-condition: Three beepers get placed (one on the starting corner), and Karel has moved 2 corners forward
    """
    for i in range(2):
        put_beeper()
        move()
    put_beeper()
def build_hospital():
    """
    Precondition: World is valid (beepers are not next to each other, or next to a wall)
    Post-condition: A hospital is built, Karel has moved one corner forward
    """
    pick_beeper()  # Pick up the beeper (the supplies)
    turn_left()
    put_three_beepers()
    turn_right()
    move()
    turn_right()
    put_three_beepers()
    turn_left()


def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()  # Build the hospital
        if front_is_clear():
            move()  # Move towards a beeper


if __name__ == "__main__":
    run_karel_program()
    main()
