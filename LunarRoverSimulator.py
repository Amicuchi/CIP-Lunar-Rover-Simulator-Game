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

def navigation_phase():
    clear_screen()
    print("\n=== GRID NAVIGATION CONTROL ===")
    
    # 1. GAME STATE (Coordinates [row, column])
    rows = 5
    cols = 5
    rover_position = [0, 0]    # Rover starts in the top-left corner
    target_position = [4, 4]   # Target is in the bottom-right corner
    
    # List of obstacles (craters, rocks, etc.)
    obstacles = [[0, 3], [1, 1], [2, 3], [3, 0], [4, 2]] 
    
    rover_reached_destination = False
    
    while not rover_reached_destination:
        clear_screen()
        
        print("\nLunar Sector Map:")
        
        # 2. DRAWING THE MAP
        # This loop scans all rows and columns
        for r in range(rows):
            drawn_row = ""
            for c in range(cols):
                current_coord = [r, c]
                
                if current_coord == rover_position:
                    drawn_row += "[R]"
                elif current_coord == target_position:
                    drawn_row += "[O]"
                elif current_coord in obstacles:
                    drawn_row += "[X]"
                else:
                    drawn_row += "[ ]" # Empty terrain
            
            print(drawn_row)
            
        # 3. WIN CONDITION
        if rover_position == target_position:
            print("\nTarget reached!")
            print("Navigation mission completed.\n")
            rover_reached_destination = True
            break
        
        # 4. RECEIVING THE COMMAND
        command = input("\nNavigation command (w/a/s/d or 'help'): ").lower()
        
        if command == "help":
            print("\nCommands:")
            print("- w : UP")
            print("- s : DOWN")
            print("- a : LEFT")
            print("- d : RIGHT")
            input("\nPress ENTER to return to the map...")
            continue # Skips the rest of the code and goes back to the start of the 'while'
            
        # 5. CALCULATING THE NEXT POSITION (without moving yet)
        new_row = rover_position[0]
        new_col = rover_position[1]
        
        if command == "w":
            new_row -= 1   # Moves up one row
        elif command == "s":
            new_row += 1   # Moves down one row
        elif command == "a":
            new_col -= 1   # Moves left one column
        elif command == "d":
            new_col += 1   # Moves right one column
        else:
            print("\n[ERROR] Invalid navigation command.")
            input("Press ENTER to try again...")
            continue
            
        # 6. COLLISION AND LIMITS SYSTEM
        new_position = [new_row, new_col]
        
        # Checks if the new position is outside the map (less than 0 or greater than the limit)
        hit_wall = (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols)
        
        # Checks if the exact new position is in the list of obstacles
        hit_obstacle = new_position in obstacles
        
        if hit_wall:
            print("\n[SYSTEM ALERT] Movement blocked: Lunar sector limit reached.")
            input("Press ENTER to recalculate route...")
        elif hit_obstacle:
            print("\n[SYSTEM ALERT] Collision risk: Crater/Obstacle detected on the route.")
            input("Press ENTER to recalculate route...")
        else:
            # If it didn't hit a wall and didn't hit an obstacle, the movement is approved!
            rover_position = new_position
            
    input("Press ENTER to proceed to the shutdown procedure...")

def shutdown_phase():
    clear_screen()
    print("\n=== SHUTDOWN PROCEDURE ===")
    engine_running = True
    status_verified = False
    
    while engine_running:
        command = input("\nEnter a command ('status' or 'shutdown_engine'): ").lower()
        
        if command == "status":
            print("\nChecking telemetry...")
            print("Engine rotation: Idle.")
            print("Temperature: Stable.")
            print("\n[ SAFE FOR SHUTDOWN ]")
            status_verified = True
            
        elif command == "shutdown_engine":
            if status_verified:
                print("\nShutting down engine... ")
                print("System static.")
                print("\nOperation completed safely.")
                engine_running = False
            else:
                print("\n[ PROTOCOL ERROR ]")
                print("\nIt is mandatory to verify the engine 'status' before authorizing shutdown.")
                print("Always remember this because it will be vital when the rover is on the moon.")
        else:
            print("\n[ INVALID COMMAND ]")
            print("\nThe engine continues to operate.")
            
    print("\n[ SYSTEM SHUTDOWN ]\n")
    input("Press ENTER to read the final mission report...")

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
    preparation_phase()
    navigation_phase()
    shutdown_phase()
    debriefing_phase()

if __name__ == "__main__":
    main()