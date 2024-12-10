import matplotlib.pyplot as plt
import math
import numpy
import collections

class pyfys:

    def plot(self, func, start=0, stop=100, xvalues=[], title="", xlabel="", ylabel="", grid=True):
        """
        Plot a graph of a given mathematical function over a specified range.

        Parameters
        ----------
        func : callable
            The function to be plotted. Should accept a single argument (x) and return a numeric value.
        start : float, optional
            The starting value of the x-axis range (default is 0).
        stop : float, optional
            The ending value of the x-axis range (default is 100).
        xvalues : list, optional
            A list of specific x values to plot, will replace start-stop.
        title : str, optional
            The title of the graph (default is an empty string).
        xlabel : str, optional
            Label for the x-axis (default is 'x').
        ylabel : str, optional
            Label for the y-axis (default is 'y').
        grid : bool, optional
            Whether to display a grid on the graph (default is True).

        Returns
        -------
        None
            Displays the graph using matplotlib.
        """
        xvalues = list(xvalues)
        if xvalues != []:
            x = xvalues
        else:
            x = numpy.linspace(start, stop) 
        y = [func(i) for i in x]
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)
        plt.legend()
        plt.show()


    def bar(self, values):
        """
        Plot a bar graph for a list of data values and return their frequency count.

        Parameters
        ----------
        values : list
            A list of data values (can be strings, integers, etc.) for which the bar graph is to be plotted.

        Returns
        -------
        dict
            A dictionary where the keys are unique elements from the input list, and the values are their counts.

        Displays
        -------
        A bar graph of the data values using matplotlib.
        """
        values = collections.Counter(values)
        names = [key for key in values]
        counts = [values[key] for key in values]
        matplotlib_named_colors = ['red', 'blue', 'orange', 'green', 'purple', 'yellow', 'brown', 'pink', 'cyan', 'gray', 'magenta', 'teal', 'gold', 'lime', 'darkblue', 'coral', 'olive']
        colors = matplotlib_named_colors[:len(names)+1]

        print(values)

        plt.bar(names, counts, color=colors)
        plt.show()

        return values


    def quadratic_formula(self, a, b, c):
        """
        Solve a quadratic equation of the form ax^2 + bx + c = 0.

        Parameters
        ----------
        a : float
            Coefficient of x^2 (must not be 0).
        b : float
            Coefficient of x.
        c : float
            Constant term.

        Returns
        -------
        tuple or str
            A tuple containing the two roots (real or complex) of the equation,
            or a string if the equation is invalid (e.g., a = 0).

        Raises
        ------
        ValueError
            If the discriminant is negative and real solutions are expected.
        """
        if a == 0:
            return "Coefficient 'a' cannot be zero. This is not a quadratic equation."

        discriminant = b**2 - 4*a*c

        # Case: Real roots
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2

        # Case: Complex roots
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            return root1, root2


    def kmh_to_ms(self, speed):
        """
        Convert from km/h to m/s.
        
        Parameters
        ----------
        speed : float
            Speed in kilometers per hour.

        Returns
        -------
        float
            Speed in meters per second.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """
        
        try:
            speed = speed / 3.6
        except ValueError:
            return "Invalid input. Please enter a number."
        return speed 


    def celcius_to_kelvin(self, temp):
        """
        Convert from degrees Celsius to Kelvin.
        
        Parameters
        ----------
        temp : float
            Temperature in degrees Celsius.

        Returns
        -------
        float
            Temperature in Kelvin.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """
        
        try:
            temp = temp + 273.15
        except ValueError:
            return "Invalid input. Please enter a number."
        return temp
    

    def fahrenheit_to_celsius(self, temp):
        """
        Convert from degrees Fahrenheit to Celsius.
        
        Parameters
        ----------
        temp : float
            Temperature in degrees Fahrenheit.

        Returns
        -------
        float
            Temperature in degrees Celsius.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """
        
        try:
            temp = (temp - 32) * 5/9
        except ValueError:
            return "Invalid input. Please enter a number."
        return temp
    

    def degrees_to_radians(self, degrees):
        """
        Convert from degrees to radians.
        
        Parameters
        ----------
        degrees : float
            Angle in degrees.

        Returns
        -------
        float
            Angle in radians.
        
        Raises
        ------
        ValueError
            If the input is not a number.
        
        """
        
        try:
            degrees = degrees * (math.pi/180)
        except ValueError:
            return "Invalid input. Please enter a number."
        return degrees
    

    def kinetic_energy(self, mass, velocity):
        """
        Calculate the kinetic energy for given mass and velocity.

        Parameters
        ----------
        mass : float or list of floats
            Mass value(s) in kilograms. Can be a single value or a list.
        velocity : float or list of floats
            Velocity value(s) in meters per second. Can be a single value or a list.

        Returns
        -------
        float or list of floats
            Kinetic energy value(s) in joules.
        """
        try:
            if isinstance(mass, (int, float)) and isinstance(velocity, (list)):
                energy = [0.5 * mass * v**2 for v in velocity]
            elif isinstance(velocity, (int, float)) and isinstance(mass, (list)):
                energy = [0.5 * m * velocity**2 for m in mass]
            elif isinstance(mass, (list)) and isinstance(velocity, (list)):
                energy = [0.5 * m * v**2 for m, v in zip(mass, velocity)]
            elif isinstance(mass, (int, float)) and isinstance(velocity, (int, float)):
                energy = 0.5 * mass * velocity**2
            else:
                raise TypeError("Inputs must be numbers or lists of numbers.")

            return energy if isinstance(energy, list) else float(energy)
        except (TypeError, ValueError) as e:
            return f"Invalid input: {e}"