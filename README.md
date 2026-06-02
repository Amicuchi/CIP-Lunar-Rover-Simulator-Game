# Lunar Rover Simulator

<img src="./images/thumbnail.png" alt="Lunar Rover Simulator Thumbnail" width="500">

A terminal-based Python simulator created as the final project for the Stanford Code in Place course.

The Lunar Rover Simulator places the user in the role of a remote pilot tasked with operating a rover on the moon's surface. The program is driven entirely through terminal inputs and features state-machine validation and 2D grid spatial navigation.

## Technical Features
- **Finite State Machine:** Initialization and shutdown protocols. The user cannot operate the engine without calibrating it, nor shut it down without verifying telemetry.
- **2D Grid Navigation:** A dynamic 5x5 matrix map that updates the rover's `[R]` location in real-time.
- **Collision Detection:** Mathematical boundary checks prevent the rover from driving off the map or crashing into known geological obstacles `[X]`.
- **Clean UI:** Terminal is cleared dynamically between states to provide a continuous, distraction-free "dashboard" experience.

## How to Play
1. Ensure you have Python 3 installed.
2. Clone this repository or download the `LunarRoverSimulator.py` file.
3. Run the script in your terminal:
   
   ```bash
   python LunarRoverSimulator.py
   ```

4. Follow the on-screen prompts. Use the help command during the simulation if you need assistance with the protocols.

## Acknowledgments

This project was developed as the final submission for Stanford University's Code in Place.