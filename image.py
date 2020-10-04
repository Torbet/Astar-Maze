import cv2
import numpy as np


class Image():
    def __init__(self, img):
        self.img = cv2.imread(img, 0)
        self.solved = cv2.imread(img)

    def refresh(self):
        for row in self.img:
            for i in row:
                print(i, end="     ")
            print('\n')

    def serialize(self):
        for row in self.img:
            for i in range(len(row)):
                if row[i] == 255:
                    row[i] = 1

        for row in self.img:
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1

    def solve(self, coords):
        for i in coords:
            self.solved[i[0]][i[1]] = [0, 0, 255]

    def save(self):
        cv2.imwrite('./img/saved.png', self.solved)
