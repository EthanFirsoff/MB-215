import turtle

def draw_geometric_art():
    # Import Turtle graphics library
    screen = turtle.Screen()
    pattern_turtle = turtle.Turtle()

    # Set up your drawing parameters
    ITERATIONS = 36  # The number of times to repeat the pattern
    ANGLE = 10       # The angle to turn after each shape is drawn
    SIZE = 100       # The size parameter for the shapes

    # Loop to draw the pattern
    for _ in range(ITERATIONS):
        # Draw a square
        for _ in range(4):
            pattern_turtle.forward(SIZE)
            pattern_turtle.right(90)  # Right angle for a square

        # Rotate the turtle to prepare for the next shape
        pattern_turtle.right(ANGLE)

    # Complete the program with a command to keep the window open
    turtle.done()

# Call the function to draw the pattern
draw_geometric_art()