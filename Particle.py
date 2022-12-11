import numpy as np





class Particle:
    
    """In this script we are creating a single class precisely called Particle. T
    his will be the partcicle we are testing the garvitational simulation on

    This class needs to have clear variables: 
    Position (representing the position as a vector);
    Velocity (representing the velocity as a vector); 
    and acceleration (representaion of the acceleration as a vector)
    as well as mass which is  ascalar quantity
    """
    def __init__(
        self,
        position = np.array([0.0, 0.0, 0.0], dtype = float), 
        velocity = np.array([0.0, 0.0, 0.0], dtype = float), 
        acceleration = np.array([0.0, 0.0, 0.0], dtype = float), 
        name = 'Ball', #name of the object, duhh
        mass = 1.0, #Currently in Kilograms (Kg)
        G = 6.67408e-11
        ):
        
        
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float) 
        self.name = name
        self.mass = mass
        self.G = G

    """Defining the names and other variables of the Particle"""
    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format( 
            self.name, self.mass, self.position, self.velocity, self.acceleration
            )

    """This updates the position of any bodie passed through this class using using the Euler-Cromer Numerical method"""
    def Euler (self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT
 
    """This updates the position of any bodie passed through this class using using the Euler-Cromer Numerical method"""
    def EulerCromer (self, deltaT):
       self.velocity = self.velocity + self.acceleration * deltaT 
       self.position = self.position + self.velocity * deltaT


    """This is the Update Gravitation acceleration function. This is the most important function in my class. 
    It will run through all the bodies in my list and calculate the Gravitation acceleration acting on it due to the other body's presence.
    This is using Newtons laws of usniversal gravitation and laws of motion to update the acceleration that will be fed into the Euler and Euler-Cromer Method"""
    def updateGravitationalAcceleration(self, bodies): #This is Going to define the gravitational acceleration
        gravacc = 0

        for body in bodies: # This for loop runs through all the bodies in my Simulation file, and will calculate the Gravitation acceleration on each body due to the other bodies in my system
            if body == self:
                continue
            seperation = self.position - body.position #This is going to make a new varible that is an array called seperation. This is r_1-r_2 which if you remeber we have been using a lot in Electromagnetism calculations
            gravacc += (-self.G * body.mass * seperation) / (np.linalg.norm(seperation))**3 #This is the acceleration due to gravity.
        
        self.acceleration = gravacc #This will update the acceleration with the gravitational acceleration depending on where the particle is 
    
   
   
    """This is defining the Kinetic energy of all the particles in the system. 
    This will be used further on to test if energy is conserved in the simulation"""
    def KineticEnergy(self, bodies):
     KE = 0
     for body in bodies:
         KE = 1/2 * body.mass * (np.linalg.norm(body.velocity))**2
     return KE


    """This is defining the Kinetic energy of all the particles in the system. 
    This will be used further on to test if energy is conserved in the simulation"""
    def GravitaionPotentialEnergy(self, bodies):
        GPE = 0
        for body in bodies:
            if body == self:
                continue
            seperation = self.position - body.position
            GPE += (-self.G * body.mass * self.mass)/np.linalg.norm(body.velocity)
        return GPE


    """This is defining the Momentum of all the particles in the system. 
    This is used to test if Momentum is conserved by this simulation"""
    def Momentum (self, bodies):
        momentum = 0
        for body in bodies:
            momentum = np.linalg.norm(body.velocity) * body.mass
        return momentum
   
   
    """This is defining the external angular momentum of each of the particles in the system. 
   This is used to test whether angular momentum is conserved in the simulation"""
    def Angular_Momentum (self, bodies):
        Angualar_Momentum = 0
        for body in bodies :
            Angualar_Momentum = np.cross(self.position, self.velocity)
        return Angualar_Momentum