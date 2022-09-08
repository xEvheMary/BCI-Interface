from PySide2.QtCore import QThread, QRunnable, Slot, Signal, QObject, QThreadPool
import traceback, sys
import g_var
'''
BASE OBJECTS FOR THREADS WORKERS
'''

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(object)

class guiSignals(QObject):
    
    startSig = Signal()
    stopSig = Signal()

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
    Inherits from QRunnable for long-running, non-interruptable tasks
    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

'''
When you think about it, this is not necessary (*lol)
because technically it has nothing special about it other than the signal
'''

class WorkerThread(QThread):
    '''
    Base Worker thread

    Inherits from QThread to handler worker thread setup, signals and wrap-up.
    Inherits from QThread for short-running, interruptable tasks

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    '''
    def __init__(self, *args, **kwargs):
        super().__init__()
        # Store constructor arguments (re-used for processing)
        #self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    def __del__(self):
        '''
        What to be done after the thread ended
        '''
        pass

    def update(self):
        '''
        What to be done every update
        '''
        self.msleep(100) # example for the delay or sleep time
    
    def run(self):
        '''
        What needs to be run [also call update() & signal emits]
        '''
        pass