import cv2
import numpy as np
import traffic_light as tl
import features as feat


def identify_traffic_light(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple identifying the location
    of the traffic light in the image and the lighted light.

    :param img: Image as numpy array
    :return: Tuple identifying the location of the traffic light in the image and light.
             ( x,   y, color)
             (140, 100, 'None') or (140, 100, 'Red')
             In the case of no light lit, coordinates can be just center of traffic light
    """
    # Copy the image and get the edges
    coord_img = img.copy()
    img_gray = cv2.cvtColor(coord_img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (0, 0), 1.5)
    img_edge = cv2.Canny(img_blur, 0, 2)

    # Use the copied image and its edges to get the center and dimensions of the traffic light
    cX, cY, xaxis, yaxis = tl.coords(coord_img, img_edge)

    xmin = None
    xmax = None
    ymin = None
    ymax = None

    # Use the dimensions to crop the traffic light into its own image
    if len(xaxis) != 0 and len(yaxis) != 0:
        xmin = xaxis.min()
        xmax = xaxis.max()
        ymin = yaxis.min()
        ymax = yaxis.max()
    cropped_img = img[ymin:ymax, xmin:xmax]

    # Convert the traffic light to grayscale and blur it
    cropped_gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
    cropped_blur = cv2.GaussianBlur(cropped_gray, (0,0), 1.5)

    # Look for color(s) that are lit on the traffic light
    color = None
    if cX != None and cY != None:
        color = tl.color(cropped_img, cropped_blur)

    return cX, cY, color


def identify_stop_sign(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple of the sign location and name.

    :param img: Image as numpy array
    :return: tuple with x, y, and sign name
             (x, y, 'stop')
    """
    # Set an acceptable color (BGR) range to threshold
    color_low = np.array([0, 0, 200])
    color_high = np.array([5, 5, 255])

    # Form a mask based on the color range
    mask = cv2.inRange(img, color_low, color_high)

    # Use the mask to find the edges
    edges = cv2.Canny(mask, 100, 200)

    # Use the edges to find the lines
    lines = feat.sign_lines(edges)

    # Set an acceptable angle range to search
    lower_angle = 40
    upper_angle = 50

    # The lines being searched are diagonal
    diagonal = True

    if lines is None:
        return None, None, ""

    # Filter out lines that are outside of the angle range
    lines = feat.filter_angles(lines, lower_angle, upper_angle, diagonal)

    if lines is None:
        return None, None, ""

    name = "Stop"

    # Find the center of the stop sign
    xaxis, yaxis = feat.sign_axis(lines)
    cX, cY = feat.center(xaxis, yaxis)

    return cX, cY, name


def identify_yield(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple of the sign location and name.

    :param img: Image as numpy array
    :return: tuple with x, y, and sign name
             (x, y, 'yield')
    """
    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set an acceptable color (HSV) range to threshold
    color_low = np.array([0, 250, 250])
    color_high = np.array([5, 255, 255])

    # Form a mask based on the color range
    mask = cv2.inRange(hsv, color_low, color_high)

    # Using the mask, find the edges
    edges = cv2.Canny(mask, 100, 200)

    # Using the edges, find the lines
    lines = feat.sign_lines(edges)

    if lines is None:
        return None, None, ""

    # Set an acceptable angle range to search
    lower_angle = 50
    upper_angle = 70

    # The lines being searched are diagonal
    diagonal = True

    # Filter out lines that are outside of the angle range
    lines = feat.filter_angles(lines, lower_angle, upper_angle, diagonal)

    if lines is None:
        return None, None, ""

    name = "Yield"

    # Find the center of the yield sign
    xaxis, yaxis = feat.sign_axis(lines)
    cX, cY = feat.center(xaxis, yaxis)

    return cX, cY, name


def identify_construction(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple of the sign location and name.

    :param img: Image as numpy array
    :return: tuple with x, y, and sign name
             (x, y, 'Construction')
    """
    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set an acceptable color (HSV) range to threshold
    color_low = np.array([15, 250, 250])
    color_high = np.array([20, 255, 255])

    # Form a mask based on the color range
    mask = cv2.inRange(hsv, color_low, color_high)

    # Using the mask, find the edges
    edges = cv2.Canny(mask, 100, 200)

    # Using the edges, find the lines
    lines = feat.sign_lines(edges)

    if lines is None:
        return None, None, ""

    name = "Construction"

    # Find the center of the construction sign
    xaxis, yaxis = feat.sign_axis(lines)
    cX, cY = feat.center(xaxis, yaxis)

    return cX, cY, name


def identify_warning(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple of the sign location and name.

    :param img: Image as numpy array
    :return: tuple with x, y, and sign name
             (x, y, 'Warning')
    """
    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set an acceptable color (HSV) range to threshold
    color_low = np.array([20, 250, 250])
    color_high = np.array([30, 255, 255])

    # Form a mask based on the color range
    mask = cv2.inRange(hsv, color_low, color_high)

    # Using the mask, find the edges
    edges = cv2.Canny(mask, 100, 200)

    # Blur the masked image
    blur = cv2.GaussianBlur(mask, (0,0), 1.5)

    # Using the edges, find the lines
    lines = feat.sign_lines(edges)

    if lines is None:
        return None, None, ""

    # Set an acceptable angle range to search
    lower_angle = 40
    upper_angle = 50

    # The lines being searched are diagonal
    diagonal = True

    # Filter out lines that are outside of the angle range
    lines = feat.filter_angles(lines, lower_angle, upper_angle, diagonal)

    # Use the blurred image to find circles
    circles = feat.sign_circle(blur)

    if lines is None:
        return None, None, ""
    
    if circles is not None:
        # If there are circles, they are likely either railroad crossings or yellow traffic lights
        # Get the center and radius of the circles
        circle_cX, circle_cY, r = feat.center_rad(circles, 52)

        # Find the range of x and y values that the circle exists within
        xmin = circle_cX - r
        xmax = circle_cX + r
        ymin = circle_cY - r
        ymax = circle_cY + r

        x_range = [xmin, xmax]
        y_range = [ymin, ymax]

        # Use the range of x and y values to exclude any lines inside the circle from the 'lines' list
        lines = feat.exclude_range(lines, x_range, y_range)


    name = "Warning"

    # Find the center of the warning sign
    xaxis, yaxis = feat.sign_axis(lines)
    cX, cY = feat.center(xaxis, yaxis)

    return cX, cY, name


def identify_rr_crossing(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple of the sign location and name.

    :param img: Image as numpy array
    :return: tuple with x, y, and sign name
             (x, y, 'rr_crossing')
    """
    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set an acceptable color (HSV) range to threshold
    color_low = np.array([20, 250, 250])
    color_high = np.array([30, 255, 255])

    # Form a mask based on the color range
    mask = cv2.inRange(hsv, color_low, color_high)

    # Blur the masked image
    blur = cv2.GaussianBlur(mask, (0,0), 1.5)

    # Use the blurred image to find circles
    circles = feat.sign_circle(blur)

    if circles is None:
        return None, None, ""

    name = "RR_Crossing"
    
    # Find the center of the railroad crossing sign
    cX, cY, radius = feat.center_rad(circles, 52)

    return cX, cY, name


def identify_services(img: np.ndarray) -> tuple:
    """
    This function takes in the image as a numpy array and returns a tuple of the sign location and name.

    :param img: Image as numpy array
    :return: tuple with x, y, and sign name
             (x, y, 'Services')
    """
    # Convert the image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set an acceptable color (HSV) range to threshold
    color_low = np.array([115, 250, 250])
    color_high = np.array([125, 255, 255])

    # Form a mask based on the color range
    mask = cv2.inRange(hsv, color_low, color_high)

    # Using the mask, find the edges
    edges = cv2.Canny(mask, 100, 200)

    # Using the edges, find the lines
    lines = feat.sign_lines(edges)

    if lines is None:
        return None, None, ""

    # Set acceptable angles to search
    lower_angle = 0
    upper_angle = 90

    # The lines being searched are not diagonal
    diagonal = False

    # Filter out lines that are outside of the specified angles
    lines = feat.filter_angles(lines, lower_angle, upper_angle, diagonal)

    if lines is None:
        return None, None, ""

    name="Services"

    # Find the center of the services sign
    xaxis, yaxis = feat.sign_axis(lines)
    cX, cY = feat.center(xaxis, yaxis)

    return cX, cY, name


def identify_signs(img: np.ndarray) -> np.ndarray:
    """
    This function takes in the image as a numpy array and returns a numpy array of all signs locations and name.
    Call the other identify functions to determine where that sign is if it exists.

    :param img: Image as numpy array
    :return: Numpy array of all signs locations and name.
             [[x, y, 'stop'],
              [x, y, 'construction']]
    """
    found_signs = []
    sign_names = ["Traffic Light", "Construction", "Stop", "Yield", "RR_Crossing", "Services", "Warning"]
    sign_functions = [identify_traffic_light, identify_construction, identify_stop_sign, identify_yield,
                      identify_rr_crossing, identify_services, identify_warning]
    
    for sign_name, function_call in zip(sign_names, sign_functions):
        if sign_name == "Traffic Light":
            cX, cY, color = function_call(img)

            if None not in (cX, cY, color):
                sign = [cX, cY, f'{sign_name} ({color})']
                found_signs.append(sign)
        else:
            cX, cY, name = function_call(img)

            if cX != None and cY != None:
                sign = [cX, cY, name]
                found_signs.append(sign)
    
    return found_signs


def identify_signs_noisy(img: np.ndarray) -> np.ndarray:
    """
    This function takes in the image as a numpy array and returns a numpy array of all signs locations and name.
    Call the other identify functions to determine where that sign is if it exists.

    The images will have gaussian noise applied to them so you will need to do some blurring before detection.

    :param img: Image as numpy array
    :return: Numpy array of all signs locations and name.
             [[x, y, 'stop'],
              [x, y, 'construction']]
    """
    raise NotImplemented


def identify_signs_real(img: np.ndarray) -> np.ndarray:
    """
    This function takes in the image as a numpy array and returns a numpy array of all signs locations and name.
    Call the other identify functions to determine where that sign is if it exists.

    The images will be real images so you will need to do some preprocessing before detection.
    You may also need to adjust existing functions to detect better with real images through named parameters
    and other code paths

    :param img: Image as numpy array
    :return: Numpy array of all signs locations and name.
             [[x, y, 'stop'],
              [x, y, 'construction']]
    """
    raise NotImplemented