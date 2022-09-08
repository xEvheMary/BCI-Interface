"""Shows / Check LSL Streams info"""
import pylsl
from typing import List
import numpy as np
import math
import pyqtgraph as pg
import g_var
# import preproc

# VARIABLES
plot_len = g_var.plot_duration # Max Buffer length of data in seconds

# Base LSL Inlet Class
class Inlet:
    """Base class to represent an LSL inlet"""
    def __init__(self, info: pylsl.StreamInfo):
        # create an inlet and connect it to the outlet we found earlier.
        # max_buflen is set so data older the plot_duration is discarded
        # automatically and we only pull data new enough to show it

        # Also, perform online clock synchronization so all streams are in the
        # same time domain as the local lsl_clock()
        # (see https://labstreaminglayer.readthedocs.io/projects/liblsl/ref/enums.html#_CPPv414proc_clocksync)
        # and dejitter timestamps
        self.inlet = pylsl.StreamInlet(info)
        # store the name and channel count
        self.name = info.name()
        self.type = info.type()
        self.channel_count = info.channel_count()
        #self.channel_list = self.get_channel()
        self.channel_list = []
        self.get_channel()
    
    # Unnecessary except for checking [Each stream might have different descritions template]
    def get_info(self):
        y = self.inlet.info().as_xml()
        return y
    
    # Pull channel list from description
    def get_channel(self):
        ch = self.inlet.info().desc().child("channels").child("channel")
        for _ in range(self.channel_count):
            #print("  " + ch.child_value("label"))
            self.channel_list.append(ch.child_value("label"))
            ch = ch.next_sibling()

# Marker Specific Inlet
class MarkerInlet(Inlet):
    """A MarkerInlet shows events that happen sporadically"""
    def __init__(self, info: pylsl.StreamInfo):
        super().__init__(info)
        self.marks = []
    
    def pull_data(self):
        self.marks = []
        strings, timestamps = self.inlet.pull_chunk(0)
        if timestamps:
            for string, ts in zip(strings, timestamps):
                self.marks.append(pg.InfiniteLine(ts, angle=90, movable=False, label=str(string[0])))

# Data Specific Inlet
class DataInlet(Inlet):
    """A DataInlet represents an inlet with continuous, multi-channel data."""
    dtypes = [[], np.float32, np.float64, None, np.int32, np.int16, np.int8, np.int64]

    def __init__(self, info: pylsl.StreamInfo):
        super().__init__(info)
        # calculate the size for the buffer, i.e. two times the displayed data
        self.ts_len = info.nominal_srate() * plot_len                       # Amount of sample : Sampling rate * length
        self.bufsize = (2 * math.ceil(self.ts_len), info.channel_count())   # [Multiplier * Samples] x Channels
        self.buffer = np.empty(self.bufsize, dtype=self.dtypes[info.channel_format()])
        empty = np.array([])
        # Data related
        self.x_data = empty         # [Timestamps]
        self.y_data = self.buffer   # [time x channels]
        # Plot related
        self.curves = [pg.PlotCurveItem(x=empty, y=empty, autoDownsample=True) for _ in range(self.channel_count)]
    
    def pull_data(self):
        # Pull data as much as
        x,ts = self.inlet.pull_chunk(timeout=0.0,
                                      max_samples=self.buffer.shape[0])
        # Prepare x axis [Time stamps]
        this_x = np.hstack((self.x_data, ts))
        if len(this_x) > self.bufsize[0]:
            self.x_data = this_x[:-(self.bufsize[0])]
        # Prepare y axis [Data (value x channels)]
        this_y = np.vstack((self.buffer, x))
        self.y_data = this_y[:-(self.bufsize[0]), :]

    def plot_data(self):
        for ch_ix in range(self.channel_count):
            x = self.x_data
            y = self.y_data[:,ch_ix]
            self.curves[ch_ix].setData(x, y)

    def proc_data(self):
        pass

def main():
    # firstly resolve all streams that could be shown
    inlets: List[Inlet] = []
    print("looking for streams")
    #time.sleep(wait_time)
    # Check all streams
    streams = pylsl.resolve_streams()
    # Counter 
    c = 0
    # Initialize inlet [Specialized for data, just for testng]
    ins = None
    # Create preprocessor object
    # prep = preproc.preprocess()

    # Create inlet for all streams
    for i, info in enumerate(streams):
        # Create Different Inlets for every type of stream
        if info.type() == 'Markers':
            inlets.append(MarkerInlet(info))
        elif info.nominal_srate() > 0 :
            inlets.append(DataInlet(info))
        else : 
            print('Unknown type of stream : ', info.name())
        # Check for infos
        # print(inlets[i].get_info())
        # Check for channels
        # print(inlets[i].channel_list)
        if info.nominal_srate() > 0:
            ins = inlets[i]

    ########################################
    # From here is for testing stream
    st = pylsl.local_clock()

    # Turn off if no stream
    while ins:
        x, _ = ins.inlet.pull_sample()
        # Do preproc on the data [Optional]
        #prep.run(x)
        c += 1
        if pylsl.local_clock() - st >= 1.0:
            print('sample per second : ', c)
            st = pylsl.local_clock()
            c = 0

if __name__ == '__main__':
    main()