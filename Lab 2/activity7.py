# Activity 7: Turtle Drawing
# This program demonstrates basic Turtle graphics functions to draw a simple figure.

import turtle

def main():
    # Set up the window
    window = turtle.Screen()
    window.title("Turtle Drawing")
    
    # Create a turtle
    t = turtle.Turtle()
    
    # Set pen size
    t.pensize(3)
    
    # Set drawing color
    t.color("blue")
    
    # Move the turtle forward by 100 units
    t.forward(100)
    
    # Turn the turtle right by 90 degrees
    t.right(90)
    
    # Move the turtle forward by 50 units
    t.forward(50)
    
    # Turn the turtle left by 90 degrees
    t.left(90)
    
    # Lift the pen up – no drawing when moving
    t.penup()
    
    # Move the turtle to a specific location
    t.goto(-50, -50)
    
    # Put the pen down – drawing when moving
    t.pendown()
    
    # Draw a circle with radius of 25
    t.circle(25)
    
    # Draw a dot with diameter 10
    t.dot(10)
    
    # Set the turtle heading to 0 (East)
    t.setheading(0)
    
    # Change the turtle color
    t.color("red")
    
    # Draw a filled shape
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    # Clear the drawing
    t.clear()
    
    # Reset the turtle's state
    t.reset()
    
    # Hide the turtle
    t.hideturtle()
    
    # Set the animation speed (0:fastest, 1:slowest, 10:normal)
    t.speed(0)
    
    # Display text
    t.write("Turtle Demo Complete", font=("Arial", 16, "normal"))
    
    # Close the window on a click
    window.onclick(lambda x, y: window.bye())
    window.mainloop()

# Call the main function
if __name__ == "__main__":
    main()