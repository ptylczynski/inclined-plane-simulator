# Inclined Plane Simulator
Numerical simulator for movement on funciton described slopes.
Additional properties such as friction and gravity can be described as time position function

## Usage
```
    s = Simulator(0.01, 3000, 90, 200)
    s.set_friction_expression('0.01')
    s.set_gravity_expression('10')
    s.set_plane_expression('-1/10000 * (t-100)**3')
    s.simulate()
```
- Constructor takes *time step*, *iterations number*, *left boundary*, *right boundary*
- Input for each `set_*` function is string, which could be wether constant or function
- Result of above commands are 5 plots showing different aspects of move

## Allowded funcitons
Function parsing is based on SymPy, so clearly everything what is understandable by standard Python is proper

## Architecture
- `function.py` - is abstract class for each function
- `inputMonoFunction.py` - is function which should be injected by user, example is *friction*
- `functions.py` - contains all functions definitions needed for simulation
    - `Angle` - first order derivative
    - `Acceleration` - net acceleration of object, could be negative
    - `Plane` - function of slope
    - `Friction` - function of friction in given place on slope
    - `Gravity` - place specific gravity value
- `simulator.py` - contains buissnes logic of simulator
