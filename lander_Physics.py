# Josh was here


# Sophie was here

h = 100000
hInit = 100000
vInit = -100
v = vInit
a = 0
t = 0
g = 3.72076 # m/s^2 Mars OLD
A = 0



G_moon = 6.67430*10^(-11) # Moon (m^3/(kg*s^2))
m_moon = 7.34767309*10^22 # Moon kg
r_moon = 1740000 # Moon (m)
m_lander = 1

dt = 1 # (sec)

# Gravitational Acceleration
def getGravitationalAcceleration(G_moon, r_moon, h):
    g_moon = G_moon / ((r_moon + h)^2)
    return g_moon


# get current acceleration
def getCurrentAcceleration():
    # Net Force= Force of thrust - Force of gravity
    F_Thrust = 1 # Get proper Value 
    g_moon = getGravitationalAcceleration() # Get proper Value (t)
    m_lander = 1 # Get proper Value (t-1)
    m_fuel = 1 # Get this proper Value

    F_g = g_moon * m_lander
    Force_Net = F_Thrust - F_g

    a_t = Force_Net / (m_lander - 0.5* m_fuel) 
    return a_t


# Current Lander Velocity
def getCurrentLanderVelocity():
    F_Thrust = 1 # Get proper Value 
    g_moon = 1 # Get proper Value (t)
    v_t_old = 1 # Get this proper Value

    a_t = getCurrentAcceleration()

    v_t = v_t_old + a_t * dt
    return v_t


# Current Altitude
def getCurrentAltitude():
    h_old = 1 # Get proper value
    v_old = 1# Get proper value
    a_t = getCurrentAcceleration()
    
    h_t_after_thrust = h_old - (v_old * dt) - (0.5 * a_t * dt^2)
    
    return h_t_after_thrust




def main():
    while True:
        t += 1
        
        # get Altitude
        h = getCurrentAltitude()
        
        # get Fuel
        
        # get Weight
        
        # get Velocity
        v = getCurrentLanderVelocity()

        # get Time till Impace
        # get Displacement


        print(h)


main()

# Altitude, Fuel, Weight, Velocity, Impact till Time, Displacement