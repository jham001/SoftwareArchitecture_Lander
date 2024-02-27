from pickle import FALSE
import lander_Backend


t = 0

dt = 1 # (sec)

# Gravitational Acceleration
def getGravitationalAcceleration():
    G_moon = 6.67430*10**(-11) # Moon (m^3/(kg*s^2))
    m_moon = 7.34767309*10**22 # Moon kg
    r_moon = 1740000.0 # Moon (m)
    h = lander_Backend.getAltitude() # (m)
    g_moon = G_moon * m_moon / ((r_moon + h)**2)
    return g_moon


# get current acceleration
def getCurrentAcceleration(thrusterToggle):
    # Net Force= Force of thrust - Force of gravity
    F_Thrust = 16000 * thrusterToggle # (N)
    g_moon = getGravitationalAcceleration() # (t)
    m_lander = lander_Backend.getLanderMass() # (kg)
    m_fuel = lander_Backend.getFuelMass() # (kg)

    F_g = g_moon * m_lander
    Force_Net = F_Thrust - F_g


    if (m_lander - 0.5* m_fuel) != 0:
        a_t = Force_Net / (m_lander - 0.5* m_fuel) 
        return a_t


# Current Lander Velocity
def getCurrentLanderVelocity(thrusterToggle):
    dt = 1 # (sec)

    g_moon = getGravitationalAcceleration() # (t)
    v_old = lander_Backend.getVelocity() # (m/s)

    a_t = getCurrentAcceleration(thrusterToggle)

    v_t = v_old + a_t * dt
    return v_t


# Current Altitude
def getCurrentAltitude(thrusterToggle):
    dt = 1 # (sec)

    h_old = lander_Backend.getAltitude() # (m)
    v_old = lander_Backend.getVelocity() # (m/s)
    a_t = getCurrentAcceleration(thrusterToggle) # (m/s^2)
    
    h_t_after_thrust = h_old - (v_old * dt) - (0.5 * a_t * dt**2)
    
    return h_t_after_thrust




def main(t):
    while True:
        t += 1
        thrusterToggle = FALSE
        
        # Used later for displacement
        h_old = lander_Backend.getAltitude() # (m)

        # get Altitude
        h = getCurrentAltitude(thrusterToggle)
       
        # get Displacement
        displacement = h - h_old # (m)
        
        # get Fuel
        m_fuel = lander_Backend.getFuel() # (kg)
        
        # get Weight
        m_lander = lander_Backend.getMass() # (kg)
        
        # get Velocity
        v = getCurrentLanderVelocity(thrusterToggle)

        # get Time till Impact
        t_minus = 1 # Get Actual Value Later

        # Save all new data to DB
        lander_Backend.AddRow(h, m_fuel, m_lander, v, t_minus, displacement)

        #print(h)


#main(t)

# Altitude, Fuel, Weight, Velocity, Impact till Time, Displacement

def getFuel():
    return lander_Backend.getFuelMass()

def getMass():
    return lander_Backend.getLanderMass()

def getImpactTime():
    return 1

def getDisplacement(thrusterToggle):
    h_old = lander_Backend.getAltitude() # (m)

    # get Altitude
    h = getCurrentAltitude(thrusterToggle)
       
    # get Displacement
    displacement = h - h_old # (m)
    return displacement

def newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange):
    lander_Backend.newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange)
    
def addRow(time_elapsed, h, v, m_fuel, m_lander, displacement):
    lander_Backend.addRow(time_elapsed, h, v, m_fuel, m_lander, displacement)