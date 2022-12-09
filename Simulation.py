import numpy as np
import copy
from Particle import Particle
SolMass = 1988500e24     # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
SolRadius = 696000e03  # https://ssd.jpl.nasa.gov/horizons/app.html#/
Sol = Particle(
    position=np.array([-1.270041465788883E+09, 5.334143525690233E+08, 2.531627852186497E+07], dtype = float), #As taken on the 6th of December 2021
    velocity=np.array([-6.334338567034989e00, -1.449049777597427E01, 2.632041873513674E-01], dtype = float), #As taken on the 6th of December 2021
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Sol",
    mass=SolMass
)
MercuryMass = 3.302e23     # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
MercuryRadius = 2440e03 # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
Mercury = Particle(
    position=np.array([-6.580492635624038E+09, -6.869762798898374E+10, -5.144983675359946E+09], dtype = float), #As taken on the 6th of December 2021
    velocity=np.array([3.879383805008622E+04, -1.252218948726321E+03, -3.659922407730150E+03], dtype = float), #As taken on the 6th of December 2021
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Mercury",
    mass=MercuryMass
)
VenusMass = 48.685e23 # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
VenusRadius = 6051.84  # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
Venus = Particle(
    position=np.array([6.294918549658331E+10, 8.739856131218165E+10, -2.488224438820872E+09], dtype = float), #As taken on the 6th of December 2021
    velocity=np.array([-2.827601533057489E+04, 2.065168258304866E+04, 1.915208151111990E+04], dtype = float), #As taken on the 6th of December 2021
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Venus",
    mass=VenusMass
)
EarthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
EarthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([3.992132592995688E+10, 1.420764459662853E+11, 1.856070576681942E+07], dtype = float),#As taken on the 6th of December 2021
    velocity=np.array([2.910586535078599E+04, 8.195794592725187E+03, 9.772944202688372E-01], dtype = float),#As taken on the 6th of December 2021
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Earth",
    mass=EarthMass
)
MarsMass = 6.4171e23  # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
MarsRadius = 3389.92  # https://ssd.jpl.nasa.gov/horizons/app.html#/ 
Mars = Particle(
    position=np.array([-1.740218558356142E+11, -1.583747536814650E+11, 9.325376879528835E+08], dtype = float), #As taken on the 6th of December 2021
    velocity=np.array([1.730328919306531E+04, -1.577337967515575E+04, -7.546107323744922E02], dtype = float), #As taken on the 6th of December 2021
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Mars",
    mass=MarsMass
)



bodies=[Sol, Mercury, Venus, Earth, Mars] #This is the lsit of the bodies that are being affected by the gravtstional pull of one another

for body in bodies: #This just prints the Start energy and Momentum. It was helpful in checking that all my calculations were accurate through checking it against what I got.
    StartMomentum=0
    StartEnergy=0
    StartMomentum+=body.Momentum(bodies)
    StartEnergy+=body.GravitaionPotentialEnergy(bodies) + body.KineticEnergy(bodies)
print('Total Momentum in the System=', StartMomentum, 'Total Energy in the System=', StartEnergy)


Data = [] #This is a list that I am going to save my bodies into
time = 0 #Time at the start of the simulation
D = 0 #This is a dump data Varible to help me to deep save my results so I can plot them
for i in range (0, 672, 168): #This doesn't mean we are looking over x seconds, it means we are looking over x steps of time (see body.update(n)) where n is is the number in the brackets
  t = 100000 #This is the time step, Delta T (in seconds), that will be fed into the paticle class' numerical method we are looking at and update the position and velocity using this time step
  time +=t 
  for body in bodies:
     body.updateGravitationalAcceleration(bodies)
     body.EulerCromer(t) #This is where I choose Euler or Euler-Cromer Method to update all bodies' position and velocity using the specifies numerical method
  print('x=', Earth.position, 'v=', Earth.velocity)
  print('y=', Venus.position, 'u=', Venus.velocity)












  if i == D:
    for body in bodies:
        Data.append([time, copy.deepcopy(body)]) #This is saving the list data 
    D+=1
np.save("Bodies", Data, allow_pickle=True) #This saves data to an .npy file which will be used in my Plotter.py file to plot a graph of the modles system, as well as be the data that I use to test the simulation

