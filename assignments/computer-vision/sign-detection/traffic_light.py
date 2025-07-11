import cv2
import numpy as np
import hw2
import features as feat


def coords(img: np.ndarray, img_edge: np.ndarray) -> tuple:
    """
    This function identifies lines within a given image, and uses this data
    to identify any rectangles in the image. This is the first step of traffic
    light detection.
    :param: Image as numpy array
    :param: Binary Image showing the edges in the image, as numpy array
    :return: ...
    """
    # Convert the traffic light to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h, w = hsv.shape[:2]

    # Get the edges of the traffic light
    color_low = np.array([0, 0, 38])
    color_high = np.array([0, 64, 76])
    mask = cv2.inRange(hsv, color_low, color_high)
    img_edge = cv2.Canny(mask, 20, 100)
    
    cX = None
    cY = None

    # Using the edges, find the lines on the traffic light
    lines = cv2.HoughLinesP(img_edge, 1, np.pi / 180, 50, None, 5, 10)
    if lines is not None:
        for line in lines:
            x0, y0, x1, y1 = line[0]

    # Using the lines, find the dimensions of the traffic light
    xaxis, yaxis = feat.sign_axis(lines)

    # Get the center coordinate
    cX, cY = feat.center(xaxis, yaxis)
  
    return cX, cY, xaxis, yaxis


def color(img: np.ndarray, img_blur: np.ndarray) -> tuple:
    """
    This function searches for circles within a given image, representing traffic lights.
    If lights are found, it measures the intensity of their colors, and uses this data
    to determine which lights are lit. This is the second (and final) step of traffic
    light detection.
    :param: Image as numpy array
    :param: Blurred Image as numpy array
    :return: String representing the color of the lit lights.
    """
    # Find the circles in the traffic light
    circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 1, param1=41, param2=34, minRadius=1, maxRadius=0)

    # Initialize each possible color to 'False' by default
    red = False
    yellow = False
    green = False

    # Initialize the lit color to 'None' by default
    color = None

    # If circles are found, analyze their colors to determine which lights are lit, if any
    if circles is not None:
        for circle in circles[0]:
            x, y, radius = circle
            x = int(x)
            y = int(y)

            # Get the green and red values of the center point of the circle
            g = img[y][x][1]
            r = img[y][x][2]

            if g >= 250 and r >= 250:
                # If 'g' and 'r' are greater than 250, the light is lit yellow
                yellow = True
            elif g >= 250:
                # If 'g' is greater than 250, the light is lit green
                green = True
            elif r >= 250:
                # If 'r' is greater than 250, the light is lit red
                red = True
            else:
                pass
        
        if green == True:
            # If green is lit
            if yellow == True:
                # If green and yellow are lit, red is likely lit as well
                color = "All"
            else:
                color = "Green"
        elif yellow == True:
            # If yellow is lit
            if green == True:
                # If yellow and green are lit, red is likely lit as well
                color = "All"
            else:
                color = "Yellow"
        elif red == True:
            # If red is lit
            color = "Red"
        else:
            # If no lights are lit
            color = "None"
    
    return color