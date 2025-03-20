#!/usr/bin/env python3
"""
turtle_race.py - A simple turtle race simulation.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/20
License: MIT
Dependencies: turtle, random

Description:
This script simulates a race between multiple turtles moving at random speeds.
Each turtle is assigned a unique color and starts from the same position.
The race continues until one of the turtles reaches the finish line.

Usage:
Run the script and watch the race:
    python turtle_race.py

Example Output:
    The turtle red won the race!
"""
import turtle
import random

# Set up the race track and turtles
def setup_race(num_turtles):
    screen = turtle.Screen()
    screen.setup(width=800, height=500)

    turtles = []
    colors = ["red", "blue", "green", "purple", "orange", "pink", "yellow", "brown"]
    start_x, start_y = -350, 150

    for i in range(num_turtles):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(colors[i % len(colors)])  # Assign different colors
        t.penup()
        t.goto(start_x, start_y - (i * 50))  # Initial position
        t.pendown()
        turtles.append(t)

    return turtles

# Start the race and move turtles randomly
def start_race(turtles):
    finished = False
    while not finished:
        for t in turtles:
            move = random.randint(1, 10)  # Random speed
            t.forward(move)

            if t.xcor() >= 350:  # Finish line
                finished = True
                print(f"The turtle {t.pencolor()} won the race!")
                break

# Main function to initialize and run the race
def main():
    num_turtles = 5  # Number of turtles in the race
    turtles = setup_race(num_turtles)
    start_race(turtles)
    turtle.done()

if __name__ == "__main__":
    main()