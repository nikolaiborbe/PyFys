# PyFys

PyFys is a Python library designed to simplify physics calculations and visualizations. It provides tools for computing common physics quantities and creating graphs.

The philosophy of the project is speed and simplicity. Physics is challenging enough as it is, so PyFys aims to make the programming side of things as easy as possible.

### Example Use Case

Imagine you have a list of masses and want to calculate their kinetic energy, given a constant velocity. With PyFys, you can compute this in a single line and visualize the results with a bar plot:

```python
import pyfys
fys = pyfys()

masses = [1, 2, 3, 4, 5]
velocity = 10

fys.bar(fys.kinetic_energy(masses, velocity))
```

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
fys = pyfys()
mass = 10
energy = [5, 10, 15]
energy = fys.kinetic_energy(mass, energy)
print(energy)  # Output: [125.0, 500.0, 1125.0]
```

### Generate a Graph
This example demonstrates how to plot a simple graph of a quadratic function:

```python
fys.graph(lambda x: x**2, start=0, stop=10, title="Quadratic Function")
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
- [ ] Update functions to work with both lists and single values
