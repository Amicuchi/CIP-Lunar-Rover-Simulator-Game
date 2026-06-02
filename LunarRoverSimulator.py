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

def preparation_phase():
    clear_screen()
    print("\n=== ROVER INITIALIZATION SYSTEM ===")
    status = "OFF"
    
    while status != "READY_TO_MOVE":
        print(f"\n[Status: {status}]")
        command = input(f"Enter a command ('help' to list): ").lower()
        
        if command == "help":
            print("\nAvailable commands:")
            print("- calibrate    : Initiates the calibration of the rover's steering systems.")
            print("- start_engine : Starts the main engine (requires prior calibration).")
            print("- help         : Displays this list of commands.")
            
        elif command == "calibrate":
            print("\nCalibrating steering systems... 100%")
            status = "CALIBRATED"
            
        elif command == "start_engine":
            if status == "CALIBRATED":
                print("\nEngine started successfully! Systems online.")
                status = "READY_TO_MOVE"
            else:
                print("\nSECURITY ERROR")
                print("You must calibrate the systems before starting the engine.")
                
        else:
            print("Command not recognized by the system. Type 'help' for assistance.")
            
    print("\n[ SYSTEM READY ]")
    print("Transitioning to navigation control...\n")
    input("Press ENTER to continue...")

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