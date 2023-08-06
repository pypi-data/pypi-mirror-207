from PySide6.QtCore import QRect, QPoint
from PySide6.QtGui import QGuiApplication

from matplotlib import pyplot as plt

import numpy as np
import mss as m
import cv2

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

    def locate_image_on_screen(
            self, image: str | type[np.array], rect: QRect = None, confidence: float = 0.8
    ) -> QPoint | bool:
        """
        Search for an image on the screen and returns the location of the found image in pixel or False, if no image was found.

        :param image:       URL or numpy-array of the image to find.
        :param rect:        A rectangular area where to search for the image.
        :param confidence:  A threshold when an image is declared as found.
        :return:            Returns the location of the image or False, if no image was found.
        """
        screenshot = self.take_screenshot(rect)
        result = self.locate_image_in_image(image, screenshot, confidence)
        return result

    def locate_image_in_image(
            self, img_to_find: str | type[np.array], in_img_to_search: str | type[np.array], confidence: float = 0.8
    ) -> QPoint | bool:
        """
        Search for an image (template) in another image and returns the location of the found image in pixels.

        :param img_to_find:         URL or numpy-array of the image to find.
        :param in_img_to_search:    URL or numpy-array of the image where to search.
        :param confidence:          A threshold when an image is declared as found.
        :return:                    Returns the location of the image or False, if no image was found.
        """
        if type(img_to_find) is str:
            template = cv2.imread(img_to_find, cv2.IMREAD_GRAYSCALE)
        else:
            template = cv2.cvtColor(img_to_find, cv2.COLOR_BGR2GRAY)

        if type(in_img_to_search) is str:
            image = cv2.imread(in_img_to_search, cv2.IMREAD_GRAYSCALE)
        else:
            image = cv2.cvtColor(in_img_to_search, cv2.COLOR_BGR2GRAY)

        heat_map = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(heat_map)
        # self.show_located_image(template, image, heat_map, max_loc)
        if max_val >= confidence:
            w, h = template.shape
            return QPoint(max_loc[0] + (w/2), max_loc[1] + (h/2))
        else:
            return False

    def show_located_image(self, template, image, heat_map, max_loc) -> None:
        """
        A function for debugging locate_image_in_image. It shows the located template with a frame in the image.

        :param template:    Image to search for.
        :param image:       Image where to search in.
        :param heat_map:    Result of the cv2.matchTemplate-function.
        :param max_loc:     Point of the maximum value in the heatmap.
        """
        w, h = template.shape

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(image, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(heat_map, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

        plt.subplot(122), plt.imshow(image, cmap='gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.show()

    def take_screenshot(self, rect: QRect = None) -> type[np.array]:
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

