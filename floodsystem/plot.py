import matplotlib.pyplot as plt
import math


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
