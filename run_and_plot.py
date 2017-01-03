import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
from freebot import *

import matplotlib.pyplot as plt
import numpy as np
import time


if __name__ == '__main__':

    #matplotlib settings to plot eeg waves graph
    my_dpi = 80
    plt.style.use("dark_background")
    fig = plt.figure(figsize=(1366/my_dpi, 768/my_dpi), dpi=my_dpi)
    plt.xlabel('Time (s)', fontsize=14, color='yellow')
    plt.ylabel('Attention, Meditation (%)', fontsize=14, color='yellow')
    plt.title("NeuroSky Mindwave Mobile ~ Brain Waves", fontsize=16, color="green")
    plt.figtext(0.92, 0.04, 'Attention', color='green', weight='roman',
                fontsize=13)
    plt.figtext(0.92, 0.01, 'Meditation',
                color='blue', weight='roman', fontsize=13)
    fig.canvas.set_window_title(" ")
    ax = fig.add_subplot(111)

    # some X and Y data
    x = np.arange(100)
    y = np.random.rand(100)
    z = np.random.rand(100)
    li1, = ax.plot(x, y, color="b", linewidth=2.0)
    li2, = ax.plot(x, z, color="g")

    # draw and show it
    fig.canvas.draw()
    plt.show(block=False)

    # threshold value
    threshold = 100

    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    b = generate_bot()

    if (mindwaveDataPointReader.isConnected()):
        while(True):

            dataPoint = mindwaveDataPointReader.readNextDataPoint()
            if (not dataPoint.__class__ is RawDataPoint):
                print dataPoint
                # print(dataPoint.__class__)
            if dataPoint.__class__.__name__ == "AttentionDataPoint":
                # print(dataPoint.__class__)
                if dataPoint.attentionValue > threshol:
                    print('Threshold exceeed!')
                    time.sleep(0.2) ## Wait
                    move_forward(b, 100, 100)
                else:
                    move_forward(b, 0, 0)
            y[:-10] = y[10:]
            y[-10:] = np.random.rand(10)

            z[:-10] = z[10:]
            z[-10:] = np.random.rand(10)

            # set the new data
            li1.set_ydata(y)
            li2.set_ydata(z)
            fig.canvas.draw()

    else:
        exit()
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))
