import cv2
import numpy as np


def sign_lines(img: np.ndarray) -> np.ndarray:
    """
    This function takes in the image as a numpy array and returns a numpy array of lines.

    https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html

    :param img: Image as numpy array
    :return: Numpy array of lines.
    """
    lines = cv2.HoughLinesP(img,
                            rho=1,
                            theta=np.pi/180,
                            threshold=35,
                            minLineLength=5,
                            maxLineGap=5)
    
    if lines is not None:
        return lines
    return None


def sign_circle(img: np.ndarray) -> np.ndarray:
    """
    This function takes in the image as a numpy array and returns a numpy array of circles.

    :param img: Image as numpy array
    :return: Numpy array of circles.
    """
    circles = cv2.HoughCircles(img,
                               cv2.HOUGH_GRADIENT,
                               1,
                               10,
                               None,
                               41,
                               36,
                               1,
                               0)
    if circles is not None:
        return circles
    return None


def sign_axis(lines: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    This function takes in a numpy array of lines and returns a tuple of np.ndarray and np.ndarray.

    This function should identify the lines that make up a sign and split the x and y coordinates.

    :param lines: Numpy array of lines.
    :return: Tuple of np.ndarray and np.ndarray with each np.ndarray consisting of the x coordinates and y coordinates
             respectively.
    """
    xaxis = np.empty(0, dtype=np.int32)
    yaxis = np.empty(0, dtype=np.int32)

    if lines is not None:
        for line in lines:
            for x0, y0, x1, y1 in line:
                xaxis = np.append(xaxis, x0)
                xaxis = np.append(xaxis, x1)
                yaxis = np.append(yaxis, y0)
                yaxis = np.append(yaxis, y1)

    return xaxis, yaxis


def center(xaxis: np.ndarray, yaxis: np.ndarray) -> tuple[int, int]:
    """
    This function takes in two numpy arrays representing the x and y axis of a set of lines. It returns a tuple of
    int and int.

    This function uses the axes to identify an x and y value for the center.

    :param xaxis: Numpy array of x values.
    :param yaxis: Numpy array of y values.
    :return: Tuple of int and int, containing the center x and y values respectively.
    """ 
    xmin = None
    xmax = None
    ymin = None
    ymax = None

    cX = None
    cY = None

    if len(xaxis) != 0 and len(yaxis) != 0:
        # Calculate the range of x and y values for a set of lines
        xmin = xaxis.min()
        xmax = xaxis.max()
        ymin = yaxis.min()
        ymax = yaxis.max()

        # Use the range of x and y values to get the center coordinate
        cX = ((xmax - xmin)//2)+xmin
        cY = ((ymax - ymin)//2)+ymin

    return cX, cY


def filter_angles(lines: np.ndarray, angle_a: int, angle_b: int, diagonal: bool) -> np.ndarray:
    """
    This function takes in a numpy array of lines, two angles representing either a range of 
    angles or two specific angles that are significant to the sign and a boolean stating if
    the angles are diagonal.

    This function uses the lines to calculate the angles of the sign, then uses the diagonal
    boolean to determine if the two given angles are a range or two specific angles. Finally,
    it will use either the range or specific values of the angles to determine which lines to
    eliminate. If the angles are a range, it will eliminate all lines with angles outside of
    that range, and if the angles are specific values, it will eliminate all lines with angles
    that do not equal one of those specific values.

    :param lines: Numpy array of lines.
    :param angle_a: Integer representing the first (lower) angle.
    :param angle_b: Integer representing the second (upper) angle.
    :return: Numpy array of lines that excludes any lines outside of the angle range.
    """
    i = 0
    filtered_lines = lines

    for line in lines:
        for x0, y0, x1, y1 in line:
            # Calculate the angle of the line
            angle = np.abs(np.arctan2(y1-y0, x1-x0)*180/np.pi)
            if diagonal == True:
                # If the line is diagonal, check if it falls in the angle range
                if angle_a < angle < angle_b:
                    pass
                else:
                    # If it's outside of the range, remove it
                    filtered_lines = np.delete(filtered_lines, i, 0)

                    # Subtract 1 index to stay in sync with the line being removed
                    i -= 1
            else:
                # If the line isn't diagonal, check if it matches one of the specified angles
                if angle == angle_a or angle == angle_b:
                    pass
                else:
                    # If it doesn't match, remove it
                    filtered_lines = np.delete(filtered_lines, i, 0)

                    # Subtract 1 index to stay in sync with the line being removed
                    i -= 1
        i += 1

    return filtered_lines


def exclude_range(lines: np.ndarray, x_range: tuple[int, int], y_range: tuple[int, int]) -> np.ndarray:
    """
    This function takes in a numpy array of lines, and two tuples of int and int. The two tuples
    represent a range of x and y values respectively.

    This function traverses the numpy array of lines, and uses the range of x and y values to remove
    every line that falls within those ranges.

    :param lines: Numpy array of lines.
    :param x_range: Tuple of int and int representing a range of x values.
    :param y_range: Tuple of int and int representing a range of y values.
    :return: Numpy array of lines that excludes any lines inside the range of x and y values.
    """
    i = 0
    filtered_lines = lines

    # Extract the min and max x and y values from their ranges
    xmin = x_range[0]
    xmax = x_range[1]
    ymin = y_range[0]
    ymax = y_range[1]

    for line in lines:
        for x0, y0, x1, y1 in line:
            # Check if the line falls within the specified range of x and y values
            if (xmin <= x0 <= xmax and xmin <= x1 <= xmax) and (ymin <= y0 <= ymax and ymin <= y1 <= ymax):
                # If it is within the specified range, remove it
                filtered_lines = np.delete(filtered_lines, i, 0)

                # Subtract 1 index to stay in sync with the line being removed
                i -= 1
        i += 1

    return filtered_lines


def center_rad(circles:np.ndarray, min_radius: int) -> tuple[int, int, int]:
    """
    This function takes in a numpy array of circles and an int representing a minimum radius value.

    This function traverses the array of circle, calculating the center coordinate and radius for
    each. If the radius is greater than the min_radius, then the center x, center y, and radius
    values get appended to a list that stores each of those values. Then, it calculates the sum
    of every value in each list. These sums, along with the number of indices in each list, are
    used to calculate an average (or final) value for the center coordinates and radius of a
    "main" circle that was detected in the region.

    :param circles: Numpy array of circles.
    :param min_radius: Integer representing the minimum radius.
    :return: Three integers representing the center x value, center y value, and radius of the circle.
    """

    # Initialize a list of x values, y values, and radiuses
    x_coords = []
    y_coords = []
    radiuses = []

    cX = 0
    cY = 0
    r = 0

    for circle in circles[0]:
        # Calculate the center coordinate and the radius of the circle
        x, y, radius = circle
        x = int(x)
        y = int(y)
        radius = int(radius)

        if radius > min_radius:
            # If the radius is above the minimum, append each value to its respective list
            x_coords.append(x)
            y_coords.append(y)
            radiuses.append(radius)
    
    # Sum the x coordinates
    for x_coord in x_coords:
        cX += x_coord
    
    # Sum the y coordinates
    for y_coord in y_coords:
        cY += y_coord
    
    # Sum the radiuses
    for rad in radiuses:
        r += rad

    # Calculate the average x and y to get the center coordinate
    if len(x_coords) >= 1 and len(y_coords) >= 1:
        cX = int(cX/len(x_coords))
        cY = int(cY/len(y_coords))
    
    # Calculate the average radius to get the final radius value
    if len(radiuses) >= 1:
        r = int(r/len(radiuses))

    return cX, cY, r  