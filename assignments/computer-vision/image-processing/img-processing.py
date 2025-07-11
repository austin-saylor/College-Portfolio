import cv2
import numpy as np


def read_image(image_path: str) -> np.ndarray:
    """
    This function reads an image and returns it as a numpy array
    :param image_path: String of path to file
    :return img: Image array as ndarray
    """

    # Obtain the image from the specified path
    img = cv2.imread(image_path)
    
    return img


def extract_green(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and returns the green channel
    :param img: Image array as ndarray
    :return: Image array as ndarray of just green channel
    """
    # Isolate the green channel in the image
    zeros = np.zeros(img.shape[:2], dtype = "uint8")
    green = cv2.merge([zeros, img[:, :, 1], zeros])

    return green

def extract_red(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and returns the red channel
    :param img: Image array as ndarray
    :return: Image array as ndarray of just red channel
    """
    # Isolate the red channel in the image
    zeros = np.zeros(img.shape[:2], dtype = "uint8")
    red = cv2.merge([zeros, zeros, img[:, :, 2]])

    return red

def extract_blue(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and returns the blue channel
    :param img: Image array as ndarray
    :return: Image array as ndarray of just blue channel
    """
    # Isolate the blue channel in the image
    zeros = np.zeros(img.shape[:2], dtype = "uint8")
    blue = cv2.merge([img[:, :, 0], zeros, zeros])

    return blue

def grayscale(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and converts it to greyscale
    :param img: Image array as ndarray
    :return: Image array as ndarray of the greyscale image
    """

    # Use cvtColor to convert to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray_img

def hsv(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and converts it to the hsv color scale
    :param img: Image array as ndarray
    :return: Image array as ndarray of the hsv image
    """

    # Use cvtColor to convert to the HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    return hsv_img

def swap_red_blue_channel(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and returns the image with the red and blue channel
    :param img: Image array as ndarray
    :return: Image array as ndarray of red and blue channels swapped
    """
    
    # Use cvtColor to reverse the color space, swapping the channels
    swapped_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    return swapped_img


def embed_middle(img1: np.ndarray, img2: np.ndarray, embed_size: (int, int)) -> np.ndarray:
    """
    This function takes two images and embeds the embed_size pixels from img2 onto img1
    :param img1: Image array as ndarray
    :param img2: Image array as ndarray
    :param embed_size: Tuple of size (width, height)
    :return: Image array as ndarray of img1 with img2 embedded in the middle
    """
    img = img1.copy()

    # Split the embed size into two separate variables
    embed_width, embed_height = embed_size
    
    # Get the dimensions of img2
    img2_height, img2_width = img2.shape[:2]
    
    # Calculate the starting and ending coordinates for cropping img2
    img2_x1 = img2_width // 2 - embed_width // 2
    img2_y1 = img2_height // 2 - embed_height // 2
    img2_x2 = img2_x1 + embed_width
    img2_y2 = img2_y1 + embed_height
    
    # Crop the center part of img2
    embedded_img = img2[img2_y1:img2_y2, img2_x1:img2_x2]
    
    # Get the dimensions of img1
    img1_height, img1_width = img1.shape[:2]
    
    # Calculate the starting and ending coordinates for embedding in img1
    img1_x1 = img1_width // 2 - embed_width // 2
    img1_y1 = img1_height // 2 - embed_height // 2
    img1_x2 = img1_x1 + embed_width
    img1_y2 = img1_y1 + embed_height
    
    # Embed cropped_img onto the center of img1
    img[img1_y1:img1_y2, img1_x1:img1_x2] = embedded_img
    
    return img

def calc_stats(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and returns the mean and standard deviation
    :param img: Image array as ndarray
    :return: Numpy array with mean and standard deviation in that order
    """
    # use meanStdDev to return a tuple containing the mean and standard deviation
    mean, stdev = cv2.meanStdDev(img)
    return mean, stdev


def shift_image(img: np.ndarray, shift_val: int) -> np.ndarray:
    """
    This function takes an image and returns the image shifted by shift_val pixels to the right.
    Should have an appropriate border for the shifted area:
    https://docs.opencv.org/3.4/dc/da3/tutorial_copyMakeBorder.html

    Returned image should be the same size as the input image.
    :param img: Image array as ndarray
    :param shift_val: Value to shift the image
    :return: Shifted image as ndarray
    """

    # Set the shift to be 'shift_val' pixels on the x-axis (to the right) and 0 pixels on the y axis
    shift = np.float32([[1, 0, shift_val], [0, 1, 0]])

    # Apply the shift
    shifted_img = cv2.warpAffine(img, shift, (img.shape[1], img.shape[0]))
    
    return shifted_img


def difference_image(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    """
    This function takes two images and returns the first subtracted from the second

    Make sure the image to return is normalized:
    https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga87eef7ee3970f86906d69a92cbf064bd

    :param img1: Image array as ndarray
    :param img2: Image array as ndarray
    :return: Image array as ndarray
    """

    # Subtract img2 from img1
    subtraction = img1.astype(np.float64) - img2.astype(np.float64)

    # Normalize the result
    difference_img = cv2.normalize(subtraction, subtraction, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
    
    return difference_img


def add_channel_noise(img: np.ndarray, channel: int, sigma: int) -> np.ndarray:
    """
    This function takes an image and adds noise to the specified channel.

    Should probably look at randn from numpy

    Make sure the image to return is normalized:
    https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga87eef7ee3970f86906d69a92cbf064bd

    :param img: Image array as ndarray
    :param channel: Channel to add noise to
    :param sigma: Gaussian noise standard deviation
    :return: Image array with gaussian noise added
    """

    # Apply gaussian noise to the image
    noise = np.random.randn(*img.shape) * sigma
    noisy_img = img + noise

    # Split the channels of the image
    zeros = np.zeros(noisy_img.shape[:2], dtype=noisy_img.dtype)

    blue_noise = cv2.merge([noisy_img[:, :, 0], zeros, zeros])
    green_noise = cv2.merge([zeros, noisy_img[:, :, 1], zeros])
    red_noise = cv2.merge([zeros, zeros, noisy_img[:, :, 2]])

    if (channel == 0):
        # Add noise to the blue channel
        noisy_img = blue_noise
    elif (channel == 1):
        # Add noise to the green channel
        noisy_img = green_noise
    else:
        # Add noise to the red channel
        noisy_img = red_noise

    # Normalize the image
    noisy_img = np.clip(noisy_img, 0, 255)
    noisy_img = noisy_img.astype(np.uint8)

    return noisy_img

def add_salt_pepper(img: np.ndarray) -> np.ndarray:
    """
    This function takes an image and adds salt and pepper noise.

    Must only work with grayscale images
    :param img: Image array as ndarray
    :return: Image array with salt and pepper noise
    """
    noisy_img = img.copy()

    # Determine the number of rows and columns in the image
    row, col = noisy_img.shape
    rows = row - 1
    cols = col - 1

    # Per assignment instructions, n = 5000
    n = 5000

    for i in range(n):
        # Randomly select n pixels to color white
        y = np.random.randint(0, rows) # Randomly select a row
        x = np.random.randint(0, cols) # Randomly select a col
        noisy_img[y][x] = 255
    
    for i in range(n):
        # Randomly select (another) n pixels to color black
        y = np.random.randint(0, rows) # Randomly select a row
        x = np.random.randint(0, cols) # Randomly select a col
        noisy_img[y][x] = 0

    return noisy_img


def blur_image(img: np.ndarray, ksize: int) -> np.ndarray:
    """
    This function takes an image and returns the blurred image

    https://docs.opencv.org/4.x/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html
    :param img: Image array as ndarray
    :param ksize: Kernel Size for medianBlur
    :return: Image array with blurred image
    """

    # Use medianBlur to add a blur to the given image
    blurred_img = cv2.medianBlur(img, ksize)

    return blurred_img