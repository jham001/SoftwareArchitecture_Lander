import lander_Backend
import math

# Gravitational Acceleration
def getGravitationalAcceleration():
    G_moon = 6.67430*10**(-11) # Moon (m^3/(kg*s^2))
    m_moon = 7.34767309*10**22 # Moon kg
    r_moon = 1740000.0 # Moon (m)
    h = lander_Backend.getAltitude() # (m)
    g_moon = G_moon * m_moon / ((r_moon + h)**2) # (m/s^2)
    
    return g_moon


# get current acceleration
def getCurrentAcceleration(thrusterToggle):
    # Net Force= Force of thrust - Force of gravity
    F_Thrust = 16000 * thrusterToggle # (N) 
    g_moon = getGravitationalAcceleration() # (m/s^2)
    m_lander = lander_Backend.getLanderMass() # (kg)
    m_fuel = lander_Backend.getFuelMass() # (kg)

    total_mass = m_lander + m_fuel # (kg)
    consumption = 10 # (kg/s)

    return (F_Thrust/(total_mass - 0.5 * consumption)) - g_moon # (m/s^2)


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

    h_t_after_thrust = h_old + (v_old * dt) + (0.5 * a_t * dt**2)
    
    return h_t_after_thrust


def getFuel():
    F_Thrust = 1000 # (N)
    consumption = 10 # (kg)
    fuel = lander_Backend.getFuelMass() - consumption
    return fuel

def getMass():
    return lander_Backend.getLanderMass()

def getImpactTime():
    altitude = lander_Backend.getAltitude() # (m)
    velocity = lander_Backend.getVelocity() # (m/s)
    gravitational_acceleration = getGravitationalAcceleration() # (m/s^2)

    discriminant = velocity ** 2 + 2 * gravitational_acceleration * altitude
    if discriminant < 0:
        return 999  # No real solution (lander will never hit the surface)
    else:
        time = (velocity + math.sqrt(discriminant)) / gravitational_acceleration
        return time

def getDisplacement(thrusterToggle):
    h_old = lander_Backend.getAltitude() # (m)

    # get Altitude
    h = getCurrentAltitude(thrusterToggle)
       
    # get Displacement
    displacement = h - h_old # (m)
    return displacement

def newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime):
    lander_Backend.newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime)
    
def addRow(time_elapsed, h, v, m_fuel, m_lander, displacement, acceleration, impactTime):
    lander_Backend.addRow(time_elapsed, h, v, m_fuel, m_lander, displacement, acceleration, impactTime)