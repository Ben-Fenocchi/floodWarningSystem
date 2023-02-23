import matplotlib.pyplot as plt
import matplotlib.dates
import math
import numpy as np

def plot_water_levels(station, dates, levels):

    #plot
    plt.plot(dates,levels)
    plt.axhline(y= station.typical_range[1],color ="r")
    plt.axhline(y= station.typical_range[0],color ="g")
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    
    
def plot_water_level_with_fit(station, dates, levels, p):
        #plot
    plt.plot(dates,levels)
    plt.axhline(y= station.typical_range[1],color ="r")
    plt.axhline(y= station.typical_range[0],color ="g")
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    x = matplotlib.dates.date2num(dates) # dates as floats
    y = levels
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
