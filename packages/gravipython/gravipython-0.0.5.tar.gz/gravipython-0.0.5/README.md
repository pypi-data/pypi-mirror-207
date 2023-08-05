#gravipython



README.md

This python module is a basic module that can be used for small simulations.

v 0.0.5

---
``class SolarSystem(width, height, **kwargs)``:  

``**kwargs``
- collisions=True (Set this to False if you want to deactivate collisions)  

Used to create a solar system to add stars in your simulation.  

``SolarSystem.main()``:
Method that does all the work, don't forget otherwise nothing is going to appear.  
* Click on A to spawn an asteroid of 0.000001 solar masses.  
* Click on D to spawn a red dwarf of 0.35 solar masses.  
* Click on B to spawn a brown dwarf of 0.07 solar masses.  
* Click on S to spawn a star of 1 solar mass.  
* Click on P to spawn a planet of 0.0001 solar masses.  
* Click on M to spawn a moon of 0.00001 solar masses.  
* Click on C to spawn a comet of 0.000001 solar masses.  
* Click on W to spawn a white dwarf of 0.9 solar masses.  
* Click on R to reset and remove all stars from the screen.  

---

``class SolarSystemBody(solar_system, mass, position=(0, 0), velocity=(0, 0), color=(255, 255, 255))``
This class allows you to create your own stars.
From this class are created the classes :
- Sun  
- RedDwarf  
- BrownDwarf  
- Asteroid  
- Planet  
- Moon  
- Comet  
- WhiteDwarf  
Each of these classes can be instantiated with the same parameters as SolarSystemBody, except that they have a default value for the mass and a   
different one for the color.

---

---

###Official examples :  


#####Simple system :
```python
import gravipython as gp   
# v 0.0.3 and before, use 'import gravitypython as gp'


ss = gp.SolarSystem(width=500, height=500, collisions=True)
# collisions is set by default to True

planet1 = gp.Planet(ss, mass=1, position=(0, 70), velocity=(5, 0), color=(0, 0, 255))
# color for planets is by default set to (0, 0, 255)
sun = gp.Sun(ss, mass=10000, position=(0, 0))
# you could use just sun = gp.Sun() because every arguments are set by default

ss.main() # runs the simulation
```
---

#####Binary system :
```python
import gravipython as gp  

ss = gp.SolarSystem(500, 500)

sun1 = gp.Sun(ss, mass=10000, position=(-20, 0), velocity=(0, 5))
sun2 = gp.Sun(ss, mass=10000, position=(20, 0), velocity=(0, -5))

ss.main()
```

---

---


###Credits
A part of this code has been made thanks to [Stephen Gruppetta](https://thepythoncodingbook.com/2021/09/29/simulating-orbiting-planets-in-a-solar-system-using-python-orbiting-planets-series-1/) on [ThePythonCodingBook](https://thepythoncodingbook.com/)

---

---

If you found any error, bug, or idea, you can send it by mail at <latomateultime@gmail.com>