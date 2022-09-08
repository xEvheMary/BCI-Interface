# Imports
from ast import While
import os
from signal import Signals
import traceback, sys
from typing import List
import numpy as np
import pylsl
# Import The GUI File
from simple_proto import *
from dialog_proto import *
# Import LSL Stream
from LSLStreams import Inlet, DataInlet, MarkerInlet
# Import Qt Utils
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QThread, Signal, Slot, QObject
from simple_utils import load_mat   # for now, only used for display (but isn't it a waste if only used for display) --> making objects so that the data can be used later 
from simple_worker import WorkerSignals, guiSignals
import pyqtgraph as pg
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# Import global variables
import g_var

# VARIABLES
plot_duration = g_var.plot_duration  # how many seconds of data to show
update_interval = g_var.update_interval  # ms between screen updates
pull_interval = g_var.pull_interval  # ms between each pull operation

################################################# Main Window Class #################################################
class MainWindow(QMainWindow):
    """
    Main Window
    """
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)       
        ########################## Threads Signals ##########################
        self.inThreadSignal = guiSignals()      # For Stream In thread (start/stop)

        ########################## JSON StyleSheet ##########################
        loadJsonStyle(self, self.ui)

        ########################## LSL Streams ##########################
        self.inlets: List[Inlet] = []           # Inlets
        self.streamThread = QThread()           # Thread for streamin in LSL Data
        # Init lsl streams list (Initial check on available streams, will call every refresh)
        self.refreshLSLList()

        # Offline directory path setup
        self.data_path = os.path.dirname(os.path.realpath(__file__))
        self.ui.pathBox.setText(self.data_path)

        # Directory Models
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(self.data_path)
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)
        # SetModel
        self.ui.treeView.setModel(self.dirModel)
        self.ui.listView.setModel(self.fileModel)
        self.ui.treeView.setRootIndex(self.dirModel.index(self.data_path))
        self.ui.listView.setRootIndex(self.fileModel.index(self.data_path))
        self.ui.treeView.clicked.connect(self.onFolderClicked)
        self.ui.listView.clicked.connect(self.onFileClicked)

        ########################## Buttons ##########################
        self.ui.cmdBtn1.clicked.connect(self.onDialButtonClicked1)
        self.ui.cmdBtn2.clicked.connect(self.onDialButtonClicked2)
        self.ui.browseBtn.clicked.connect(self.browseFiles)
        self.ui.resetPath.clicked.connect(self.resPath)
        self.ui.refrStreamList.clicked.connect(self.refreshLSLList)
        self.ui.applyStreamList.clicked.connect(self.applyLSLStream)
        self.ui.resContentSelect.clicked.connect(self.resetContentSelection)

        ########################## Dialog ##########################
        self.dlg = DialWindow(self.inlets)
        # Show Window
        # self.show()
    
    ################################################# LSL Streams related #################################################
    def refreshLSLList(self):
        self.ui.AvStreams.setRowCount(0)
        if self.streamThread.isRunning():
            # Stop running streaming thread
            self.stopDataThreads()
        # Find all available / running streams
        self.streams = pylsl.resolve_streams()
        # Create LSL Inlets from the resolved streams
        if len(self.streams) > 0:
            for i, info in enumerate(self.streams):
                self.addStreamRow(i, info)

    # Apply Stream Choices
    def applyLSLStream(self):
        self.inlets = []
        for i in range(self.ui.AvStreams.rowCount()):
            #print(self.tableWidget.rowCount())
            # Column 2 --> Signal
            if self.ui.AvStreams.cellWidget(i, 1).isChecked():
                # Check if stream type is data stream or eeg stream
                if self.streams[i].nominal_srate() > 0:
                    self.inlets.append(DataInlet(self.streams[i]))
                else: print('Wrong Stream Type')
            # Column 3 --> Marker
            elif self.ui.AvStreams.cellWidget(i, 2).isChecked():
                # Check if stream type is markers stream
                if self.streams[i].type() == 'Markers':
                    self.inlets.append(MarkerInlet(self.streams[i]))
                else: print('Wrong Stream Type')
            else:
                pass
        # Refresh channel list
        self.channelList()
        # Run Stream Thread
        self.runStream()     

    # Data Thread related
    def runStream(self):
        if self.streamThread.isRunning():
            # Stop running thread (Refresh it)
            self.stopDataThreads()
        # Re-run the stream in thread
        if not self.streamThread.isRunning():
            self.init_dataThread()
        else:
            print('thread still running')
    
    def init_dataThread(self):
        self.strWorker = dataWorker(self.inlets)            # Create worker instance
        self.strWorker.moveToThread(self.streamThread)      # Move worker from main thread to streaming thread
        # Connect signals
        self.inThreadSignal.stopSig.connect(self.strWorker.stop, Qt.QueuedConnection)   # Stop the timers in thread using signal(essentially, stopping the thread)
        self.strWorker.workSignals.finished.connect(self.killDataThreads)                    # After worker is stopped, quit the thread
        #self.strWorker.plotSignals.connect()                                            # Connect signal to plotter at dialog
        #self.strWorker.procSignals.connect()                                            # Connect signal to classifier
        self.streamThread.started.connect(self.strWorker.start)                         # When the thread is started, run start function in worker
        self.streamThread.start()

    def stopDataThreads(self):
        self.inThreadSignal.stopSig.emit()                  # Stop Timers in thread

    def killDataThreads(self):
        self.streamThread.quit()                            # Quit the thread
        self.streamThread.wait()
    
    # Display channel list [Checkbox not working yet]
    def channelList(self):
        for inl in self.inlets:
            if isinstance(inl, DataInlet):
                ch_list = inl.channel_list
                for i, it in enumerate(ch_list):
                    item = QtWidgets.QListWidgetItem()
                    item.setText(it)
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    self.ui.AvChannels.addItem(item)

    # Create LSL Streams items    
    def addStreamRow(self, RowPos, info):
        # Insert row 
        self.ui.AvStreams.insertRow(RowPos)
        # Row contents
        groupButton = QtWidgets.QButtonGroup(self.ui.AvStreams)
        groupButton.setExclusive(True)
        it1 = QtWidgets.QTableWidgetItem(info.name())
        self.ui.AvStreams.setItem(RowPos, 0, it1)
        ch_bx1 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx1)
        self.ui.AvStreams.setCellWidget(RowPos, 1, ch_bx1)
        ch_bx2 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx2)
        self.ui.AvStreams.setCellWidget(RowPos, 2, ch_bx2)
        it2 = QtWidgets.QTableWidgetItem(info.type())
        self.ui.AvStreams.setItem(RowPos, 3, it2)

    # Create a slot for launching the dialog window
    def onDialButtonClicked1(self):
        """Launch the dialog."""
        if not self.dlg.isVisible():
            self.dlg = DialWindow(self.inlets)
            self.dlg.show()
        self.dlg.to_dial(0)
        if not self.dlg.pltThread.isRunning():
            self.dlg.callPlotter()
    
    def onDialButtonClicked2(self):
        """Launch the dialog."""
        if not self.dlg.isVisible():
            self.dlg = DialWindow(self.inlets)
            self.dlg.show()
        self.dlg.to_dial(1)
    
    ################################################# OFFLINE DATASET #################################################
    # Tree View Click function
    def onFolderClicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.ui.listView.setRootIndex(self.fileModel.setRootPath(path)) # Display the list of items

    def expandFile(self, index):    # More like read dataset [expand because it expand the content of dataset file]
        path = self.fileModel.fileInfo(index).absoluteFilePath()
        if os.path.isfile(path):
            data = load_mat(path)
            for i, (k, con) in enumerate(data.items()):
                if not k.startswith('__'):
                    p = self.ui.ds_contents.rowCount()
                    self.addContentsRow(p, k, con)

    def onFileClicked(self):
        self.ui.ds_contents.setRowCount(0)
        for i in self.ui.listView.selectedIndexes():
            self.expandFile(i)

    def addContentsRow(self, rowPos, key, data):
        # Insert new row
        self.ui.ds_contents.insertRow(rowPos)
        # Row contents
        groupButton = QtWidgets.QButtonGroup(self.ui.ds_contents)
        groupButton.setExclusive(True)
        it1 = QtWidgets.QTableWidgetItem(key)
        self.ui.ds_contents.setItem(rowPos, 0, it1)
        if isinstance(data, np.ndarray):
            # Sequence can also be dict or list, which might not have shape (?)
            shp = str(np.shape(data))
        else:
            shp = '1'
        it2 = QtWidgets.QTableWidgetItem(shp)
        self.ui.ds_contents.setItem(rowPos, 1, it2)
        ch_bx1 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx1)
        self.ui.ds_contents.setCellWidget(rowPos, 2, ch_bx1)
        ch_bx2 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx2)
        self.ui.ds_contents.setCellWidget(rowPos, 3, ch_bx2)

    ################################################# DATASET BUTTONS #################################################
    def resetContentSelection(self):    #[Not Working yet]
        for i in range(self.ui.ds_contents.rowCount()):
            self.ui.ds_contents.cellWidget(i, 2).setChecked(False)
            self.ui.ds_contents.cellWidget(i, 3).setChecked(False)

    def applyContentSelection(self):    #[Should be working, not applied yet]
        for i in range(self.ui.ds_contents.rowCount()):
            if self.ui.ds_contents.cellWidget(i, 1).isChecked():
                pass
            elif self.ui.ds_contents.cellWidget(i, 1).isChecked():
                pass

    # Function for browsing files
    def browseFiles(self):  # Open browse dialog window
        self.data_path = QFileDialog.getExistingDirectory(self, 'Folder', self.data_path)
        self.ui.pathBox.setText(self.data_path)
        self.ui.treeView.setRootIndex(self.dirModel.index(self.data_path))
        self.ui.listView.setRootIndex(self.fileModel.index(self.data_path))

    def resPath(self):      # Reset Path to default
        self.data_path = g_var.base_path
        self.ui.pathBox.setText(self.data_path)
        self.ui.treeView.setRootIndex(self.dirModel.index(self.data_path))
        self.ui.listView.setRootIndex(self.fileModel.index(self.data_path))
    
    # Close Event of the  
    def closeEvent(self, event):
        # Stopping stream in thread
        if self.streamThread.isRunning():
            self.stopDataThreads()
        if self.dlg.pltThread.isRunning():
            self.dlg.stop_plotThread()
        # Need to stop other threads too

################################################# Dialog Window Class #################################################   
class DialWindow(QDialog):
    """Dialog Window"""
    def __init__(self, inlets, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        self.setWindowTitle('Extension')
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.pltSignal = guiSignals()
        ########################## Data Related ##########################
        self.inlet = inlets
        self.pltThread = QThread()    # Generate data, emit it 
        ########################## Plot Related ##########################
        pw = self.ui.graphicsView               # Get the plot widget
        plt = pw.getPlotItem()                  # Get the plot items
        #plt.enableAutoScale()
        self.init_plot_items(plt)
    
    # Create plot object
    def init_plot_items(self, plt: pg.PlotItem):
        # Check if inlet is empty or not
        if self.inlet:
            for inl in self.inlet:
                if isinstance(inl, DataInlet):
                    # Add as much plot items as the channels
                    num = inl.channel_count
                else:
                    pass
        else:
            num = 1
        # Create curves based on the inlet [create 1 item if no inlet, create multiple item if inlet exists (based on channel num)]
        self.curves = [pg.PlotCurveItem(x=np.array([]), y=np.array([]), autoDownsample=True) for _ in range(num)]     # Empty plot items
        for curve in self.curves:
            plt.addItem(curve)

    # Terminate plot threads when closed
    def closeEvent(self, event):
        self.stop_plotThread()

    # Change index of stacked widgets
    def to_dial(self, id):
        self.ui.dialogPages.setCurrentIndex(id)
    
    # Plot widget   
    def callPlotter(self):
        if not self.inlet:      # If inlet is empty, run this thread instead
            if not self.pltThread.isRunning():  # If thread is not already running
                self.pltWorker = plotWorker()
                self.pltWorker.moveToThread(self.pltThread)
                self.pltSignal.stopSig.connect(self.pltWorker.stop_timer, Qt.QueuedConnection)
                self.pltWorker.pltSignals.progress.connect(self.displayS)       # Connect signal to displayS
                self.pltWorker.pltSignals.finished.connect(self.killPlotter)    # After timer stopped, end thread
                self.pltThread.started.connect(self.pltWorker.start_timer)
                self.pltThread.start()
        else:
            pass
            # If inlet is not empty, get data from the stream thread

    def stop_plotThread(self):
        self.pltSignal.stopSig.emit()

    def killPlotter(self):
        self.pltThread.quit()
        self.pltThread.wait()

    def plot_sig(self, t, y):
        for idx, sig in enumerate(y):
            self.curves[idx].setData(t, sig)

    def plotarr(self, s):
        self.ui.graphicsView.clear()
        # Example, plot 3 signals
        for i in range(3):
            self.ui.graphicsView.plot(s + i)
    
    @Slot(list)
    def displayS(self, sig):
        '''
        signal emitted is connected to here
        '''
        #self.plotarr(sig)
        self.plot_sig(sig[0], sig[1])
        # Optional scroll the plot [still not working] --> data taken based on index while the timestamp have gone beyond that --> plotter already scroll
        #self.scroll()

    # Plot related
    def scroll(self):
        """Move the view so the data appears to scroll"""
        # We show data only up to a timepoint shortly before the current time
        # so new data doesn't suddenly appear in the middle of the plot
        fudge_factor = pull_interval * .002
        plot_time = pylsl.local_clock()
        self.ui.graphicsView.setXRange(plot_time - plot_duration + fudge_factor, plot_time - fudge_factor)
    
################################################# Workers #################################################
# Stream in Worker
class dataWorker(QObject):

    workSignals = WorkerSignals()
    plotSignals = Signal(object)
    procSignals = Signal(object)

    def __init__(self, inlet, parent=None):
        super().__init__()
        self.inl = inlet

    def start(self):
        # After thread started, run the timers
        self.pull_timer = QTimer(self)
        self.pull_timer.timeout.connect(self.pull_routine)
        self.pull_timer.start(pull_interval)
    
    @Slot()
    def stop(self):
        self.pull_timer.stop()
        self.workSignals.finished.emit()

    def pull_routine(self):
        # Pull LSL data routine
        for inlet in self.inl:
            inlet.pull_data()
            pass

    def plot_routine(self):
        # Prepare X Axis
        ct = pylsl.local_clock()
        t = np.arange(ct - plot_duration, ct, 0.01)
        # Prepare Y Axis
        
        # Emit data for plotter
        self.plotSignals.emit()

    def proc_routine(self):
        # Emit data for classification
        self.procSignals.emit()

# Plotter Object
class plotWorker(QObject):

    pltSignals = WorkerSignals()

    def __init__(self, parent=None):
        super().__init__()
        self.s = None
        self.phase = 0
        self.init_timer()

    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.routine)

    def start_timer(self):
        self.timer.start(100)

    def update(self):
        ct = pylsl.local_clock()
        t = np.arange(ct - plot_duration, ct, 0.01) # X Axis
        sig = np.sin(2 * np.pi * t + self.phase)    # Data [Example is sin wave]    # Y axis [All data displayed]
        #self.s = [pg.PlotCurveItem(x=t, y=sig, autoDownsample=True)]
        self.s = [t, [sig]]   # X axis, Y axis [List of signals]
        self.phase += 0.1

    def routine(self):
        self.update()
        self.pltSignals.progress.emit(self.s)

    @Slot()
    def stop_timer(self):
        self.timer.stop()
        self.pltSignals.finished.emit()

################################################# Execute #################################################
if __name__ == "__main__":
    #pg.systemInfo()
    app = QApplication(sys.argv)
    window = MainWindow()
    app.aboutToQuit.connect(window.stopDataThreads)
    window.show()
    sys.exit(app.exec_())

## End