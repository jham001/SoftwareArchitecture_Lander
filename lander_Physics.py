from os import access
import lander_Backend
import math

#FILE NAME: lander_Physics.py
#DESCRIPTION: This file creates classes and stores some static physics that are 
#             considered in program calculations. These functions contain methods 
#             that handle calculations, getter methods, and methods that handle 
#             database table creation, tuple insertion, and closing.
#
#IMPORTS: !FIXME: ASK GROUP ABOUT THIS

#Planet class stores the gravity, mass, and radius of the planet
class Planet:
    #Planet constructor
    def __init__(self, G: float, m: float, r: float):
        self.G = G
        self.m = m
        self.r = r
        
    #getter for gravitational pull of the planet
    def get_g(self, h):
        return self.G * self.m / ((self.r + h)**2)

#Lander class stores the initial information being used in calculating second by second information
class Lander:
    #Lander constructor
    def __init__(self, altitude: float, velocity: float, mass_fuel: float, mass_lander: float, F_thrust: int, fuel_consumption: int, planet: Planet):
        self.altitude = altitude
        self.velocity = velocity
        self.acceleration = 0
        self.mass_fuel = mass_fuel
        self.mass_lander = mass_lander
        self.F_thrust = F_thrust
        self.fuel_consumption = fuel_consumption
        self.planet = planet

    #getter for current lander acceleration
    def getCurrentAcceleration(self, thrusterToggle):
        #!NOTE: net force = force of thrust - force of gravity
        f_thrust = self.F_thrust * thrusterToggle # (N) 
        g_moon = self.planet.get_g(self.altitude) # (m/s^2)
        m_lander = lander_Backend.getLanderMass() # (kg)
        m_fuel = lander_Backend.getFuelMass() # (kg)
        #calculate the total mass of the lander and use this in the acceleration calculation
        total_mass = m_lander + m_fuel # (kg)
        #set the local acceleration member to a calculated acceleration
        self.acceleration = (f_thrust/(total_mass - 0.5 * self.fuel_consumption)) - g_moon # (m/s^2)
        #return newly calculated acceleration variable
        return self.acceleration

    #getter for current lander velocity
    def getCurrentLanderVelocity(self):
        #!FIXME: what is this? (sec)
        dt = 1
        #store current velocity from database in new variable to differentiate in the calculation
        v_old = lander_Backend.getVelocity() # (m/s)
        #calculate new velocity and store in Lander
        self.velocity = v_old + (self.acceleration) * dt
        #return newly calculated current velocity
        return self.velocity

    #getter for current lander altitude
    def getCurrentAltitude(self):
        dt = 1 # (sec)
        #get current altitude (m) from database and store in new variable to distinguish in the calculation
        h_old = lander_Backend.getAltitude()
        #get current velocity (m/s) from database and store in new variable to distinguish in the calculation
        v_old = lander_Backend.getVelocity()
        #get current acceleration (m/s^2) from database and store in new variable to distinguish in the calculation
        a_t = self.acceleration
        #calculate new current altitude and store in Lander
        self.altitude = h_old + (v_old * dt) + (0.5 * a_t * dt**2)
        #return newly calculated current altitude
        return self.altitude

    #getter for the current mass of fuel
    def getFuel(self):
        #calculate a single iteration of fuel consumption and store it in the Lander
        self.mass_fuel = lander_Backend.getFuelMass() - self.fuel_consumption
        #return newly calculated fuel mass
        return self.mass_fuel

    #getter for Lander mass
    def getMass(self):
        #set the current Lander mass to that stored in the database
        self.mass_lander = lander_Backend.getLanderMass()
        #return the mass of the Lander
        return self.mass_lander

    #getter for impact time
    def getImpactTime(self):
        #store the current altitude (m) from the database in a variable
        altitude = lander_Backend.getAltitude()
        #store the current velocity (m/s) from the database in a variable
        velocity = lander_Backend.getVelocity()
        #store the gravitational acceleration (m/s^2) from the Planet class
        gravitational_acceleration = self.planet.get_g(altitude)
        #!FIXME: double check with the group
        #calculate the discriminant which gives us the point at which the Lander goes below 0 altitude
        discriminant = velocity ** 2 + 2 * gravitational_acceleration * altitude
        #if the discriminant goes below 0
        if discriminant < 0:
            #no real solution (lander will never hit the surface)
            return 999  
        #otherwise calculate the current impact time
        else:
            self.impactTime = (velocity + math.sqrt(discriminant)) / gravitational_acceleration
            return self.impactTime

    #getter for the displacement of the Lander
    def getDisplacement(self):
        #get last altitude (m) from database and store in new variable to distinguish in the calculation
        h_old = lander_Backend.getAltitude() # (m)
        #get the current altitude from the Lander
        h = self.altitude
        #calculate the displacement using the initial altitude
        displacement = h - h_old
        #return newly calculate displacement
        return displacement

    #function creates a new table
    def newTable(self, time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime):
        #new table is created in the lander_Backend file
        lander_Backend.newTable(time_elapsed, altitude, velocity, m_fuel, m_lander, positionChange, acceleration, impactTime)
    #function adds tuple to table
    def addRow(self, time_elapsed):
        #new row is added to the table in the lander_Backend file
        lander_Backend.addRow(time_elapsed, self.altitude, self.velocity, self.mass_fuel, self.mass_lander, self.getDisplacement(), self.acceleration, self.impactTime)
    #function closes the database in the lander_Backend file
    def close(self):
        lander_Backend.close()