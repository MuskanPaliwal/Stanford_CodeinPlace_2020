from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

def main():

    put_first_extreme_end_beepers() """places beepers at both ends"""
    pick_end_beepers() """picks beepers at each end as Karel "shrinks the world"""
    pick_last_beeper() """picks the last beeper in the middle"""

def put_first_extreme_end_beepers():
    put_beeper()
    while front_is_clear():
        move()
    turn_around()
    put_beeper()


def pick_end_beepers():
    pick_beeper()
    move()
    put_beeper()
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
            turn_around()
            move()
            put_beeper()


def pick_last_beeper():
    turn_around()
    while no_beepers_present():
        move()
        if beepers_present():
            pick_beeper()

def turn_around():
    for i in range(2):
        turn_left()
    




if __name__ == "__main__":
    run_karel_program()
