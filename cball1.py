# Input the simulation parameters: angle, velocity, height, interval.
# Calculate the initial position of the cannonball: xpos, ypos
# Calculate the initial velocities of the cannonball: xvel, yvel
# While the cannonball is still flying:
#   update the values of xpos, ypos, and yvel for interval seconds
#   further into the flight
# Output the distance traveled as xpos
import math

class Projectile:

    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = math.pi * angle / 180.0
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    # Update the state of the projectile to account for the passage of time.
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1


def getInputs():
    angle = eval(input("Enter the launch angle (in degrees): "))
    velocity = eval(input("Enter the initial velocity (in meters/sec): "))
    height = eval(input("Enter the initial height (in meters): "))
    timeInt = eval(input("Enter the time interval between position calculations: "))
    return angle,velocity,height,timeInt


def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle,vel,h0)
    while cball.getY() >= 0:
        cball.update(time)
    print "\nDistance traveled: %0.1f meters." % (cball.getX())


if __name__ == '__main__':
    main()