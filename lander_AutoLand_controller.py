def autoLand(velocity, altitude, screenHeight):       
            
            if (velocity < (-1200 * ((altitude+2000)/screenHeight))*0.60):
                return True
            elif ((altitude < 100) & (velocity < -5)):
                return True
            else:
                return False