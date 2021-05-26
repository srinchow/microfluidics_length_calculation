import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance


def pink(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_purple = np.array([140, 50, 70])
    upper_purple = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    channel = cv2.bitwise_and(image, image, mask=mask)
    channel_bgr = cv2.cvtColor(channel, cv2.COLOR_HSV2BGR)
    channel_gray = cv2.cvtColor(channel_bgr, cv2.COLOR_BGR2GRAY)
    ret, white = cv2.threshold(channel_gray, 0, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(white, kernel, iterations=1)
    coordinates = np.column_stack(np.where(erosion == 255))
    list1 = coordinates.tolist()
    for i in list1:
        temp = i[0]
        i[0] = i[1]
        i[1] = temp
        temp = 0
    temp = 0
    temp1 = [[]]
    for i in list1:
        if i[1] > temp:
            temp1 = i
            temp = i[1]
    highest = temp1
    new1 = []
    for i in list1:
        if i[0] == temp1[0]:
            new1.append(i)
    new2 = []
    for i in new1:
        j = i[1]
        new2.append(j)
    minimum1 = min(new2)
    lowest = [temp1[0], minimum1]
    dist1 = distance.euclidean(highest, lowest)
    return dist1


def green(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_purple = np.array([20, 10, 10])
    upper_purple = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    channel = cv2.bitwise_and(image, image, mask=mask)
    channel_bgr = cv2.cvtColor(channel, cv2.COLOR_HSV2BGR)
    channel_gray = cv2.cvtColor(channel_bgr, cv2.COLOR_BGR2GRAY)
    ret, white = cv2.threshold(channel_gray, 0, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(white, kernel, iterations=1)
    coordinates = np.column_stack(np.where(erosion == 255))
    list1 = coordinates.tolist()
    for i in list1:
        temp = i[0]
        i[0] = i[1]
        i[1] = temp
        temp = 0
    temp = 0
    temp1 = [[]]
    for i in list1:
        if i[1] > temp:
            temp1 = i
            temp = i[1]
    highest = temp1
    new1 = []
    for i in list1:
        if i[0] == temp1[0]:
            new1.append(i)
    new2 = []
    for i in new1:
        j = i[1]
        new2.append(j)
    minimum1 = min(new2)
    lowest = [temp1[0], minimum1]
    dist1 = distance.euclidean(highest, lowest)
    return dist1


def length(pink, green):
    return pink / green


def action(filename):
    filepath = "images/" + filename
    image = cv2.imread(filepath)
    return length(pink(image), green(image))
