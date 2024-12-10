from threading import Timer

class RepeatedTimer:
    def __init__(self, interval: float, function, daemon: bool = False, *args, **kwargs):
        """A timer that repeats the `function` every `interval` seconds.
        
        The timer is `not` auto-started, it must be started by using start().
        """
        self.args = args
        self.kwargs = kwargs
        self._timer = None
        self._daemon = daemon
        self.function = function
        self.interval = interval
        self.is_running = False
    
    def _run(self):
        """Internal: triggers the next timer and runs the function once."""
        self.is_running = False
        self.start(False) # Must be False or else the function is called twice
        self.function(*self.args, **self.kwargs)
    
    def start(self, initial_run: bool = False):
        """Starts the repeated timer and automatically keeps it repeating."""
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.daemon = self._daemon
            self._timer.start()
            self.is_running = True
        
        # Runs the function once when calling start(True). This is kinda the
        # expected behavior, but is disabled by default for compatibility.
        if initial_run:
            self.function(*self.args, **self.kwargs)
    
    def stop(self):
        """Stops the timer and all following calls."""
        self._timer.cancel()
        self.is_running = False