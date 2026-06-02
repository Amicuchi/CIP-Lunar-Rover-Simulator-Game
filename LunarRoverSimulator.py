import os

# Author: Anderson Amicuchi Machado
# Description:
"""
    The Lunar Rover Simulator is an interactive, terminal-based application.
    The system is divided into phases that utilize a finite state machine
    to ensure the user follows the correct engine initialization and
    shutdown protocols.
    The core of the project is a grid navigation system that uses
    two-dimensional matrices to draw the lunar map and process coordinates
    in real-time, implementing mathematical collision logic to prevent the
    rover from exiting the safe boundaries or colliding with geological obstacles.
"""

def clear_screen():
    # Identifies the operating system and clears the terminal correctly
    os.system('cls' if os.name == 'nt' else 'clear')

def briefing_phase():
    clear_screen()
    print("======================================================")
    print("\nWelcome, future Astronaut.")
    print("\nAs you were informed in your summons, thanks to the")
    print("success of the Artemis mission and counting on the success")
    print("of future missions, NASA is preparing to establish the")
    print("first human colony on the moon starting in 2032.")
    print("\nFor this, we need to form a team of rover pilots")
    print("who will operate the vehicles remotely.")
    print("\nYour training begins now.")
    print("\nGood luck!")
    print("======================================================\n")
    input("\nPress ENTER to start the system...")

def debriefing_phase():
    clear_screen()
    print("\n=============================================================")
    print("Congratulations on your impeccable work, future astronaut.")
    print("This was just your initial training.")
    print("We still have many skills to develop by 2032.")
    print("Thank you for your participation in the program, and remember:")
    print("\nThis is just the beginning of this journey.")
    print("\n=============================================================\n")

def main():
    briefing_phase()
    debriefing_phase()

if __name__ == "__main__":
    main()