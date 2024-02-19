# Josh was here


# Sophie was here

h = 100000
hInit = 100000
vInit = -100
v = vInit
a = 0
t = 0
g = 3.72076 # m/s^2 Mars
A = 0

def updatePosition(h, hInit, vInit, t, a):
    h = hInit + vInit*t + 0.5*a*(t)**2
    return h

def updateAcceleration(A, g):
    a = A-g
    return a

def updateVelocity(v, a):
    
    return v



def main(h, hInit, vInit, v, t, a, g, A):
    while True:
        t += 1
        a = updateAcceleration(A, g)
        h = updatePosition(h, hInit, vInit, t, a)
        print(h)


main(h, hInit, vInit, v, t, a, g, A)

# Altitude, Fuel, Weight, Velocity, Impact till Time, Displacement