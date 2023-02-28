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
    d0 = x[0]
    return poly, d0
