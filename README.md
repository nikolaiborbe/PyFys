<p align="center">
  <img src="https://github.com/nikolaiborbe/PyFys/blob/main/assets/logo.png" width="180" alt="PyFys Logo" />
</p>

<h1 align="center">PyFys</h1>

<p align="center">An opinionated physics library.</p>
<p align="center">
<code>pip install pyfys</code>
</p>
<br />

PyFys is a Python library designed to simplify physics calculations and visualizations. It provides tools for computing common physics quantities and creating graphs.

The philosophy of the project is speed and simplicity. Physics is challenging enough as it is, so PyFys aims to make the programming side of things as easy as possible.

---

## Features
- Calculate physical quantities like kinetic energy, force, and relativistic momentum. (More equations coming soon!)
- Generate and visualize graphs for functions and data.
- Supports scalar and vector inputs for maximum flexibility and speed.

---

## Installation

To install PyFys, run the following command:

```bash
pip install pyfys
```

---

## Quickstart

### Import the Library
Here's an example of how to use PyFys to calculate kinetic energy:

```python
import pyfys

# Example: Calculate kinetic energy
fys = pyfys.fys()
mass = 10
velocity = [5, 10, 15]
energy = fys.kinetic_energy(mass=mass, velocity=velocity)
print(energy)  # Output: [125.0, 500.0, 1125.0]
```

### Generate a Graph
This example demonstrates how to plot multiple functions:

```python
fys.graph((math.sin, math.cos), stop=5)
```

### Plot Data
This example demonstrates how to plot data:

```python
mass = 10
velocity = [5, 10, 15]

fys.plot(fys.kinetic_energy(mass, velocity), velocity)
```

### Bar Chart
This example demonstrates how to create a bar chart from a list of data:

```python
data = ["cat", "dog", "bird", "cat", "dog", "fish", "dog"]
fys.bar(data)
```

---

## Documentation
TODO: Add documentation
"For detailed usage and examples, visit the [official documentation](https://github.com/your-repo-link)."

---

## Contributing

Contributions are welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## TODO
- [ ] Add more equations
- [ ] Add more constants
- [ ] Add more unit conversions
- [ ] Create documentation
- [ ] Create a documentation website, where you can search for equations (like the Tailwind documentation)
- [ ] Add integralcalculations for e.g. inertia
