from PySide6.QtCore import QRect
from PySide6.QtGui import QGuiApplication

import numpy as np
import mss as m

from screeny.mouse import Mouse


class Screeny:

    def __init__(self):
        """
        Initializing variables of the class.
        """
        self.mss = m.mss()
        self.mss_monitor = self.mss.monitors[1]
        self.q_screen = QGuiApplication().primaryScreen()
        self.mouse = Mouse(self.q_screen)

    def take_screenshot(self, rect: QRect = None):
        """
        Takes a screenshot of the complete monitor or a given area.

        :param rect:    Rectangular area where the screenshot will be taken.
        :return:        Image as a numpy-array.
        """
        if rect is None:
            img = np.array(self.mss.grab(self.mss_monitor))
        else:
            img = np.array(self.mss.grab((rect.x(), rect.y(), rect.width(), rect.height())))
        return img

    def get_mouse_pos(self):
        """
        Returns the current position of the mouse.

        :return:    Tuple of xy-coordinates of the current mouse position. -> (x, y)
        """
        return self.mouse.get_pos()

