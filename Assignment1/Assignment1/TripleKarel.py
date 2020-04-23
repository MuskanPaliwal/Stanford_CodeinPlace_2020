from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.


    
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one."""
    
    
def main():

    paint()

"""All the three bildings follow same phenomena that initially beeper will take two times left turn and print the three sides of a building. In order to switch between buildings, beeper has to take a right turn."""

def paint():
    for i in range (3):
        for i in range (2):
            paint_rectangle()
            turn_left()
            move()
        paint_rectangle()
        turn_right()

""" As we observe that during painting the walls the beeper's left would be always blocked so we can use this as a condition in our program.
    pre-condition: beeper is facing towards west and left is blocked.
    post condition: one side of the building would be printed."""

def paint_rectangle():
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    for i in range (3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
