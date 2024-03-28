from os import access
import lander_Backend
import math

class Planet:
    def __init__(self, G: float, m: float, r: float):
        self.G = G
        self.m = m
        self.r = r
        
    def get_g(self, h):
        return self.G * self.m / ((self.r + h)**2)
    

class Lander:
    def __init__(self, altitude: float, velocity: float, mass_fuel: float, mass_lander: float, F_thrust: int, fuel_consumption: int, planet: Planet):
        self.altitude = altitude
        self.velocity = velocity
        self.acceleration = 0
        self.mass_fuel = mass_fuel
        self.mass_lander = mass_lander
        self.F_thrust = F_thrust
        self.fuel_consumption = fuel_consumption
        self.planet = planet


    # get current acceleration
    def getCurrentAcceleration(self, thrusterToggle):
        # Net Force= Force of thrust - Force of gravity
        f_thrust = self.F_thrust * thrusterToggle # (N) 
        g_moon = self.planet.get_g(self.altitude) # (m/s^2)
        m_lander = lander_Backend.getLanderMass() # (kg)
        m_fuel = lander_Backend.getFuelMass() # (kg)

        total_mass = m_lander + m_fuel # (kg)

        self.acceleration = (f_thrust/(total_mass - 0.5 * self.fuel_consumption)) - g_moon # (m/s^2)

        return self.acceleration


    # Current Lander Velocity
    def getCurrentLanderVelocity(self, thrusterToggle):
        dt = 1 # (sec)

        v_old = lander_Backend.getVelocity() # (m/s)

        a_t = self.getCurrentAcceleration(thrusterToggle)

        self.velocity = v_old + a_t * dt
    
        return self.velocity


    # Current Altitude
    def getCurrentAltitude(self, thrusterToggle):
        dt = 1 # (sec)

        h_old = lander_Backend.getAltitude() # (m)
        v_old = lander_Backend.getVelocity() # (m/s)
        a_t = self.getCurrentAcceleration(thrusterToggle) # (m/s^2)

        self.altitude = h_old + (v_old * dt) + (0.5 * a_t * dt**2)
    
        return self.altitude


    def getFuel(self):
        self.mass_fuel = lander_Backend.getFuelMass() - self.fuel_consumption
        return self.mass_fuel

    def getMass(self):
        self.mass_lander = lander_Backend.getLanderMass()
        return self.mass_lander

    def getImpactTime(self):
        altitude = lander_Backend.getAltitude() # (m)
        velocity = lander_Backend.getVelocity() # (m/s)
        gravitational_acceleration = self.planet.get_g(altitude) # (m/s^2)

        discriminant = velocity ** 2 + 2 * gravitational_acceleration * altitude
        if discriminant < 0:
            return 999  # No real solution (lander will never hit the surface)
        else:
            self.impactTime = (velocity + math.sqrt(discriminant)) / gravitational_acceleration
            return self.impactTime

    def getDisplacement(self):
        h_old = lander_Backend.getAltitude() # (m)

        # get Altitude
        h = self.altitude
       
        # get Displacement
        displacement = h - h_old # (m)
        return displacement

    def newTable(self, time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime):
        lander_Backend.newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime)
    
    def addRow(self, time_elapsed):
        lander_Backend.addRow(time_elapsed, self.altitude, self.velocity, self.mass_fuel, self.mass_lander, self.getDisplacement(), self.acceleration, self.impactTime)