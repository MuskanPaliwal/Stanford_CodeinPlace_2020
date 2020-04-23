from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""
def main():

  turn_left()
  while front_is_clear():
     build_column()
     descend_column()
     """next_column()"""
     """if front_is_blocked():
        check_beeper()"""
        
"""build column function makes the karel to build a column.
   pre-condition: beeper is facing towards east and turned left before building.
   post-condition: front is clear, beeper build the column and front is blocked as beeper is facing towards north."""
def build_column():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
        check_beeper()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_beeper():
    if no_beepers_present():
        put_beeper()

"""moves the karel downwards.
   pre-condition: Front is blocked. Beeper is facing towards north. 
   post-condition: Beeper is at the first row moving to the next column, 4 columns away from the first one. And take a left turn.""" 

def descend_column():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    """while right_is_blocked():"""
    if front_is_clear():
         for i in range(4):
            move()
                
         turn_left()
        


  # There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
