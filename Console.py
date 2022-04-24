import constant

hello_string = """ 
******* Hello, welcome to this COVID-19 Cellular Automata Simulation! *******
The simulation is run on a 200*200 grid. Before we start, we need some parameters!
"""

enter_parameters = "Press ENTER if you wish to continue with our pre-chosen parameters, or press SPACE+ENTER to choose your own. "
enter_N = "Please type the value of N, the number of creatures. N must be a natural number between 0 and 40,000. "
enter_D = "Please type the value of D, the percentage of infected at start time. D must be a number between 0 and 100. "
enter_R = "Please type the value of R, the percentage of creatures that move faster. R must be a natural number between 0 and 100. "
enter_X = "Please type the value of X, the number of generations. X must be a natural number greater than 1. "
enter_P_1 = "Please type the value of P_1, the high probability of infection. P_1 must be between 0 and 1. "
enter_P_2 = "Please type the value of P_2, the low probability of infection. P_2 must be between 0 and 1. "
enter_T = "Please type the value of T, the threshold for changing probability of infection. T must must be a natural number between 0 and 100. "


def start_console():
    print(hello_string)
    space_or_enter = input(enter_parameters)
    while space_or_enter != "" and space_or_enter != " ":
        print("Wrong input.")
        space_or_enter = input(enter_parameters)
    if space_or_enter == "":
        return
    print("Ok, choose your parameters!\n")

    N = input(enter_N)
    while (not N.isdigit()) or int(N) > 40000:
        print("Wrong input.")
        N = input(enter_N)
    constant.N = int(N)

    D = input(enter_D)
    while True:
        try:
            D = float(D)
        except ValueError:
            print("Wrong input.")
            D = input(enter_D)
            continue
        else:
            if D < 0 or D > 100:
                print("Wrong input.")
                D = input(enter_D)
                continue
            else:
                break
    constant.D = D

    R = input(enter_R)
    while (not R.isdigit()) or int(R) > 100:
        print("Wrong input.")
        R = input(enter_R)
    constant.R = int(R)

    X = input(enter_X)
    while (not X.isdigit()) or int(X) == 0:
        print("Wrong input.")
        X = input(enter_X)
    constant.X = int(X)

    P_1 = input(enter_P_1)
    while True:
        try:
            P_1 = float(P_1)
        except ValueError:
            print("Wrong input.")
            P_1 = input(enter_P_1)
            continue
        else:
            if P_1 < 0 or P_1 > 1:
                print("Wrong input.")
                P_1 = input(enter_P_1)
                continue
            else:
                break
    constant.P_1 = P_1

    P_2 = input(enter_P_2)
    while True:
        try:
            P_2 = float(P_2)
        except ValueError:
            print("Wrong input.")
            P_2 = input(enter_P_2)
            continue
        else:
            if P_2 < 0 or P_2 > 1:
                print("Wrong input.")
                P_2 = input(enter_P_2)
                continue
            else:
                break
    constant.P_2 = P_2

    T = input(enter_T)
    while (not T.isdigit()) or int(T) > 100:
        print("Wrong input.")
        T = input(enter_T)
    constant.T = int(T)
