import time
import bluetooth
from mindwavemobile.MindwaveDataPoints import RawDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader
import textwrap
from freebot import *

if __name__ == '__main__':
    threshold = 40
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
                if dataPoint.attentionValue > threshold:
                    print('Threshold exceeed!')
                    time.sleep(0.2) ## Wait
                    move_forward(b, 100, 100)
                else:
                    move_forward(b, 0, 0)
    else:
        exit()
        print(textwrap.dedent("""\
            Exiting because the program could not connect
            to the Mindwave Mobile device.""").replace("\n", " "))
