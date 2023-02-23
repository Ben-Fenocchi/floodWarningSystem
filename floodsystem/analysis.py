import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates) # dates as floats
    y = levels
    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))

    # Display plot
    plt.show()

