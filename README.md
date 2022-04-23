# COVID-19 Cellular Automata Simulation

This paper presents a simulation of the spread of the contemporary COVID-19 disease. The simulation is built using a cellular automata model, of which cells can either be healthy, infected, or recovered. Besides presenting a means to simulate, visualize, and research the virus spread, this project has one specific goal. A phenomenon witnessed during the pandemic was the outcome of "waves" of infections. We define a wave as a rapid increase of the number of infected, which culminates in some maxima, and descends afterward. The objective of this project is to research which parameters lead to the creation of such waves.

## Technologies used
The whole project is written in python.
The cellular automata is represented by a `numpy` array. The simulation and the graphs are animated troughout the simulation using the `matplolib` library.

## Running the program

## Parameters
There are various parameters included in this project. You can read about them in the report.pdf included in the directory. Shortly, they are:
```
N  # number of creatures                                                              0 <= N <= 40,000
D  # percentage of infected at start time                                             0 <= D <= 100
R  # percentage of creatures that move faster                                         0 <= R <= 100
X  # number of generations until recovery
P_1  # probability of infection during low infections (high)
P_2  # probability of infection during high infections (low)
T  # threshold value for the change of P as a function of the disease state           0 <= T <= 100
```

When starting the program, you will be prompt with a console. There you can choose wether to enter your parameters or continue with our pre-chosen ones.
Follow the instructions in the console strictly, and input only legal values.

