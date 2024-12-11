import matplotlib.pyplot as plt
import math
import numpy
import collections
from pyfys.constants import Constants

class fys:
    
    def __init__(self):
        plt.style.use("bmh")
    
    def plot(self, x, y):
        """
        Plot a graph of a given mathematical function.

        Parameters
        ----------
        x : list.
            A list of x values.
        y : list.
            A list of y values.

        Returns
        -------
        None
            Displays the graph using matplotlib.
        """
        plt.plot(x, y)
        plt.show()

    def graph(self, func, stop=25, xvalues=[]):
        """
        Plot a graph of a given mathematical function.

        Parameters
        ----------
        func : callable or list/tuple of callables.
            The function to be plotted. Should accept a single argument (x) and return a numeric value.
        stop : float, optional.
            The ending value of the x-axis range (default is 25).
        xvalues : list, optional.
            A list of specific x values to plot, will replace start-stop.

        Returns
        -------
        None
            Displays the graph using matplotlib.
        """

        try:
            # make x values
            xvalues = list(xvalues)
            if xvalues != []:
                x = xvalues
            else:
                x = numpy.linspace(0, stop, 500) 

            # plot function for function in input: func
            if isinstance(func, (list, tuple)):
                for function in func:
                    y = [function(i) for i in x]
                    plt.plot(x, y)
            else:
                y = [func(i) for i in x]
                plt.plot(x, y)

            plt.show()
        except Exception as e:
            return f"Invalid input: {e}"
                    

    def bar(self, values):
        """
        Plot a bar graph for a list of data values and return their frequency count.

        Parameters
        ----------
        values : list
            A list of data values (can be strings, integers, etc.) for which the bar graph is to be plotted.


        Displays
        -------
        A bar graph of the data values using matplotlib.
        """
        values = collections.Counter(values)
        names = [str(key) for key in values]
        counts = [values[key] for key in values]
        distinct_colors = [
            '#1F77B4',  # Medium Blue
            '#2CA02C',  # Green
            '#17BECF',  # Cyan
            '#FF7F0E',  # Orange (contrast)
            '#8C564B',  # Brownish Gray
            '#9467BD',  # Purple
            '#D62728',  # Red (contrast)
            '#7F7F7F',  # Neutral Gray
            '#BCBD22',  # Olive
            '#E377C2'   # Pink
        ]
        colors = distinct_colors[:len(names)+1]

        print(values)

        plt.bar(names, counts, color=colors)
        plt.show()


    def kmh_to_ms(self, speed):
        """
        Convert from km/h to m/s.
        
        Parameters
        ----------
        speed : number or a list of numbers.
            Speed in kilometers per hour.

        Returns
        -------
        float or list of floats.
            Speed in meters per second.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """
        if isinstance(speed, (int, float)):
            return speed * 1000 / 3600
        elif isinstance(speed, (list, tuple)):
            return [s * 1000 / 3600 for s in speed]
        else:
            raise ValueError("Input must be a number or a list of numbers.")


    def celcius_to_kelvin(self, temp):
        """
        Convert from degrees Celsius to Kelvin.
        
        Parameters
        ----------
        temp : number or list of numbers.
            Temperature in degrees Celsius.

        Returns
        -------
        float or list of floats.
            Temperature in Kelvin.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """

        if isinstance(temp, (list, tuple)):
            return [t + 273.15 for t in temp]
        elif isinstance(temp, (int, float)):
            return temp + 273.15
        else:
            raise ValueError("Input must be a number or a list of numbers.")
    

    def fahrenheit_to_celsius(self, temp):
        """
        Convert from degrees Fahrenheit to Celsius.
        
        Parameters
        ----------
        temp : number or list numbers.
            Temperature in degrees Fahrenheit.

        Returns
        -------
        float or list of floats.
            Temperature in degrees Celsius.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """

        if isinstance(temp, (list, tuple)):
            return [(t - 32) * 5/9 for t in temp]
        elif isinstance(temp, (int, float)):
            return (temp - 32) * 5/9
        else:
            raise ValueError("Input must be a number or a list of numbers.")
    

    def degrees_to_radians(self, degrees):
        """
        Convert from degrees to radians.
        
        Parameters
        ----------
        degrees : number or list of numbers.
            Angle in degrees.

        Returns
        -------
        float : Angle in radians.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """
        if isinstance(degrees, (int, float)):
            return degrees * (math.pi/180)
        elif isinstance(degrees, (list, tuple)):
            return [d * (math.pi/180) for d in degrees]
        else:
            raise ValueError("Input must be a number or a list of numbers.")
    

    def kinetic_energy(self, mass, velocity):
        """
        KE = 0.5 * m * v^2

        Calculate the kinetic energy for given mass and velocity.

        Parameters
        ----------
        mass : number, or list of numbers
            Mass value(s) in kilograms. Can be a single value or a list.
        velocity : float or list of floats
            Velocity value(s) in meters per second. Can be a single value or a list.

        Returns
        -------
        float or list of floats
            Kinetic energy value(s) in joules.
        """

        if isinstance(mass, (int, float)) and isinstance(velocity, (list, tuple)):
            energy = [0.5 * mass * v**2 for v in velocity]
        elif isinstance(velocity, (int, float)) and isinstance(mass, (list, tuple)):
            energy = [0.5 * m * velocity**2 for m in mass]
        elif isinstance(mass, (list, tuple)) and isinstance(velocity, (list, tuple)):
            energy = [0.5 * m * v**2 for m, v in zip(mass, velocity)]
        elif isinstance(mass, (int, float)) and isinstance(velocity, (int, float)):
            energy = 0.5 * mass * velocity**2
        else:
            raise TypeError("Inputs must be numbers or lists of numbers.")

        return energy if isinstance(energy, list) else float(energy)
    
    
    def potential_energy(self, mass, height):
        """
        U = mgh
        
        Calculate the potential energy on earth for given mass and height.

        Parameters
        ----------
        mass : number, or list of numbers.
            Mass value(s) in kilograms. Can be a single value or a list.
        height : number, or list of numbers.
            Height value(s) in meters. Can be a single value or a list.

        Returns
        -------
        float or list of floats
            Potential energy value(s) in joules.
        """
        if isinstance(mass, (int, float)) and isinstance(height, (tuple, list)):
            energy = [9.81 * mass * h for h in height]
        elif isinstance(height, (int, float)) and isinstance(mass, (tuple, list)):
            energy = [9.81 * m * height for m in mass]
        elif isinstance(mass, (list, tuple)) and isinstance(height, (list, tuple)):
            energy = [9.81 * m * h for m, h in zip(mass, height)]
        elif isinstance(mass, (int, float)) and isinstance(height, (int, float)):
            energy = 9.81 * mass * height
        else:
            raise TypeError("Inputs must be numbers or lists of numbers.")

        return energy if isinstance(energy, list) else float(energy)

        
    def relativistic_momentum(self, mass, velocity):
        """
        p = m * v / sqrt(1 - v^2 / c^2)
        
        Calculate the relativistic momentum for given mass and velocity.

        Parameters
        ----------
        mass : number, or list of numbers.
            Mass value(s) in kilograms. Can be a single value or a list.
        velocity : number, or list of numbers.
            Velocity value(s) in meters per second. Can be a single value or a list.

        Returns
        -------
        float or list of floats
            Relativistic momentum value(s) in kg m/s.

        Raises
        ------
        ValueError
            If the velocity is greater or equal to than the speed of light.
        """

        c = Constants.SPEED_OF_LIGHT
        
        if velocity > c:
            raise ValueError("Velocity cannot be greater than the speed of light.")
        elif velocity == c:
            raise ValueError("Velocity cannot be equal to the speed of light.")

        if isinstance(mass, (int, float)) and isinstance(velocity, (tuple, list)):
            momentum = [mass * v / math.sqrt(1 - v**2 / c**2) for v in velocity]
        elif isinstance(velocity, (int, float)) and isinstance(mass, (tuple, list)):
            momentum = [m * velocity / math.sqrt(1 - velocity**2 / c**2) for m in mass]
        elif isinstance(mass, (list, tuple)) and isinstance(velocity, (list, tuple)):
            momentum = [m * v / math.sqrt(1 - v**2 / c**2) for m, v in zip(mass, velocity)]
        elif isinstance(mass, (int, float)) and isinstance(velocity, (int, float)):
            momentum = mass * velocity / math.sqrt(1 - velocity**2 / c**2)
        else:
            raise TypeError("Inputs must be numbers or lists of numbers.")

        return momentum if isinstance(momentum, list) else float(momentum)
        

    def gravitational_force(self, mass1, mass2, distance):
        """
        F = G * m1 * m2 / r^2
        
        Calculate the gravitational force between two masses.

        Parameters
        ----------
        mass1 : number, or list of numbers.
            Mass value(s) in kilograms. Can be a single value or a list.
        mass2 : number, or list of numbers.
            Mass value(s) in kilograms. Can be a single value or a list.
        distance : number, or list of numbers.
            Distance value(s) in meters. Can be a single value or a list.

        Returns
        -------
        float or list of floats
            Gravitational force value(s) in newtons.
        """
        G = Constants.GRAVITATIONAL_CONSTANT
        
        if isinstance(mass1, (int, float)) and isinstance(mass2, (tuple, list)) and isinstance(distance, (tuple, list)):
            force = [G * mass1 * m2 / d**2 for m2, d in zip(mass2, distance)]
        elif isinstance(mass2, (int, float)) and isinstance(mass1, (tuple, list)) and isinstance(distance, (tuple, list)):
            force = [G * m1 * mass2 / d**2 for m1, d in zip(mass1, distance)]
        elif isinstance(distance, (int, float)) and isinstance(mass1, (tuple, list)) and isinstance(mass2, (tuple, list)):
            force = [G * m1 * m2 / distance**2 for m1, m2 in zip(mass1, mass2)]
        elif isinstance(mass1, (int, float)) and isinstance(mass2, (int, float)) and isinstance(distance, (int, float)):
            force = G * mass1 * mass2 / distance**2
        elif isinstance(mass1, (int, float)) and isinstance(mass2, (int, float)) and isinstance(distance, (tuple, list)):
            force = [G * mass1 * mass2 / d**2 for d in distance]
        elif isinstance(mass1, (int, float)) and isinstance(mass2, (tuple, list)) and isinstance(distance, (int, float)):
            force = [G * mass1 * m2 / distance**2 for m2 in mass2]
        elif isinstance(mass1, (tuple, list)) and isinstance(mass2, (int, float)) and isinstance(distance, (int, float)):
            force = [G * m1 * mass2 / distance**2 for m1 in mass1]
        else:
            raise TypeError("Inputs must be numbers or lists of numbers.")

        return force if isinstance(force, list) else float(force)

        
    def escape_velocity(self, mass, radius):
        """
        v = sqrt(2 * G * m / r)
        
        Calculate the escape velocity for a given mass and radius.
        
        Parameters
        ----------
        mass : number, or list of numbers.
            Mass value(s) in kilograms. Can be a single value or a list.
        radius : number, or list of numbers.
            Radius value(s) in meters. Can be a single value or a list.
        
        Returns
        -------
        float or list of floats
            Escape velocity value(s) in meters per second.
        """

        if isinstance(mass, (int, float)) and isinstance(radius, (tuple, list)):
            velocity = [math.sqrt(2 * Constants.GRAVITATIONAL_CONSTANT * mass / r) for r in radius]
        elif isinstance(radius, (int, float)) and isinstance(mass, (tuple, list)):
            velocity = [math.sqrt(2 * Constants.GRAVITATIONAL_CONSTANT * m / radius) for m in mass]
        elif isinstance(mass, (list, tuple)) and isinstance(radius, (list, tuple)):
            velocity = [math.sqrt(2 * Constants.GRAVITATIONAL_CONSTANT * m / r) for m, r in zip(mass, radius)]
        elif isinstance(mass, (int, float)) and isinstance(radius, (int, float)):
            velocity = math.sqrt(2 * Constants.GRAVITATIONAL_CONSTANT * mass / radius)
        else:
            raise TypeError("Inputs must be numbers or lists of numbers.")
        
        return velocity if isinstance(velocity, list) else float(velocity)

        
    def lorentz_factor(self, velocity):
        """
        gamma = 1 / sqrt(1 - v^2 / c^2)
        
        Calculate the Lorentz factor for a given velocity.
        
        Parameters
        ----------
        velocity : number, or list of numbers.
            Velocity value(s) in meters per second. Can be a single value or a list.
        
        Returns
        -------
        float or list of floats
            Lorentz factor value(s).
        
        Raises
        ------
        ValueError
            If the velocity is greater or equal to than the speed of light.
        """

        c = Constants.SPEED_OF_LIGHT
        
        if velocity >= c:
            raise ValueError("Velocity cannot be greater than or equal to the speed of light.")
        
        if isinstance(velocity, (int, float)):
            gamma = 1 / math.sqrt(1 - velocity**2 / c**2)
        elif isinstance(velocity, (list, tuple)):
            gamma = [1 / math.sqrt(1 - v**2 / c**2) for v in velocity]
        else:
            raise TypeError("Input must be a number or a list of numbers.")
        
        return gamma if isinstance(gamma, list) else float(gamma)