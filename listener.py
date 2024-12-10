from pynput.mouse import Listener as Lstnr
from repeated_timer import RepeatedTimer
import pyautogui as pag

class Listener:
    def __init__(self, interval : int) -> None:
        self.__interval = interval
        self.__no_action_time = 0

        self.__counter_timer = RepeatedTimer(1, self.__increment_time)

        # Bind callbacks
        self.__lstnr = Lstnr(on_move=self.__something, on_click=self.__somewhere, on_scroll=self.__nowhere)
        

    # Timer Control methods
    def __restart_time(self) -> None:
        self.__no_action_time = 0

    def __do_something(self) -> None:
        self.__restart_time()
        for i in range(5):
            pag.move(10, 10)
            pag.move(-10, -10)

        for i in range(5):
            pag.scroll(-10)
            pag.scroll(10)
        

    def __increment_time(self) -> None:
        self.__no_action_time += 1
        if self.__no_action_time >= self.__interval:
            self.__do_something()

    # Callbacs methods
    def __something(self, x, y):
        self.__restart_time()

    def __somewhere(self, x, y, button, pressed):
        self.__restart_time()

    def __nowhere(self, x, y, dx, dy):
        self.__restart_time()

    def stop(self):
        self.__counter_timer.stop()
        self.__lstnr.stop()

    def start(self) -> None:
        self.__counter_timer.start()

        self.__lstnr.start()
        self.__lstnr.join()
