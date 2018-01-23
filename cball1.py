# Input the simulation parameters: angle, velocity, height, interval.
# Calculate the initial position of the cannonball: xpos, ypos
# Calculate the initial velocities of the cannonball: xvel, yvel
# While the cannonball is still flying:
#   update the values of xpos, ypos, and yvel for interval seconds
#   further into the flight
# Output the distance traveled as xpos
from math import pi, sin, cos

def main():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))

    # Convert angle to radians
    theta = (angle * pi) / 180.0

    # set the initial position and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground
    while ypos >= 0:
        # calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = ypos + time * (yvel + yvel1)/ 2.0
        yvel = yvel1

    print("\n Distance traveled: %0.1f meters." % xpos)


if __name__ == '__main__':
    main()