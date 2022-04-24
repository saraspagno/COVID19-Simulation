# COVID-19 Cellular Automata Simulation

This paper presents a simulation of the spread of the contemporary COVID-19 disease. The simulation is built using a cellular automata model, of which cells can either be healthy, infected, or recovered. Besides presenting a means to simulate, visualize, and research the virus spread, this project has one specific goal. A phenomenon witnessed during the pandemic was the outcome of "waves" of infections. We define a wave as a rapid increase of the number of infected, which culminates in some maxima, and descends afterward. The objective of this project is to research which parameters lead to the creation of such waves.

## Technologies used
The whole project is written in python.
The cellular automata is represented by a `numpy` array. The simulation and the graphs are animated troughout the simulation using the `matplolib` library.

## Running the program
You can run this program as any python file in your pc. As follows:

1. Download this repository into a folder in your pc.
2. Enter the folder, and type: `pip install -r requirements.txt`
3. Now, simply run: `python main.py` within the project folder, no args required.

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

When starting the program, you will be prompt with a console. All the parameteres will be provided as text input. The instructions on which parameters are needed and how are provided during the program. There is also an option to run the program with pre-chosen parameters.
**Follow the instructions in the console strictly, and input only legal values.**

The pre-chosen parameters are:
```
N = 8000
D = 0.1
R = 10
X = 8
P_1 = 0.2
P_2 = 0.1
T = 8
```

