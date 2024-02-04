# Josh was here


# Sophie was here

h = float(10000)
hInit = float(10000)
vInit = float(-1000)
vInit = 0
a = float(0.1)
t = 0

def updatePosition(h, hInit, vInit, t, a):
    h = hInit + vInit*t + 0.5*a*(t)**2
    return h

def main(h, hInit, vInit, t, a):
    while True:
        t += 1
        h = updatePosition(h, hInit, vInit, t, a)
        print(h)


main(h, hInit, vInit, t, a)