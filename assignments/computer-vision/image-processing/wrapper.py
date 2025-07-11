import os
import cv2
from hw1 import *


def main() -> None:
    # TODO: Add in images to read
    img1 = read_image("img1/pic1.jpg")
    img2 = read_image("img2/pic2.jpg")

    # TODO: replace None with the correct code to convert img1 and img2
    img1_gray = grayscale(img1)
    img2_gray = grayscale(img2)

    img1_hsv = hsv(img1)
    img2_hsv = hsv(img2)

    img1_red = extract_red(img1)
    img1_green = extract_green(img1)
    img1_blue = extract_blue(img1)

    img2_red = extract_red(img2)
    img2_green = extract_green(img2)
    img2_blue = extract_blue(img2)

    img1_swap = swap_red_blue_channel(img1)
    img2_swap = swap_red_blue_channel(img2)

    embed_img = embed_middle(img1, img2, (60, 60))

    img1_stats = calc_stats(img1_gray)
    img2_stats = calc_stats(img2_gray)

    # TODO: Replace None with correct calls
    img1_shift = shift_image(img1_gray, 2)
    img2_shift = shift_image(img2_gray, 2)

    # TODO: Replace None with correct calls. The difference should be between the original and shifted image
    img1_diff = difference_image(img1_gray, img1_shift)
    img2_diff = difference_image(img2_gray, img2_shift)

    # TODO: Select appropriate sigma and call functions
    sigma = 100
    img1_noise_red = add_channel_noise(img1, 2, sigma)
    img1_noise_green = add_channel_noise(img1, 1, sigma)
    img1_noise_blue = add_channel_noise(img1, 0, sigma)

    img2_noise_red = add_channel_noise(img2, 2, sigma)
    img2_noise_green = add_channel_noise(img2, 1, sigma)
    img2_noise_blue = add_channel_noise(img2, 0, sigma)

    img1_spnoise = add_salt_pepper(img1_gray)
    img2_spnoise = add_salt_pepper(img2_gray)

    # TODO: Select appropriate ksize, must be odd
    ksize = 3
    img_blur = blur_image(img1_spnoise, ksize)
    img2_blur = blur_image(img2_spnoise, ksize)

    # TODO: Write out all images to appropriate files
    cv2.imwrite('img1/pic1_green.jpg', img1_green)
    cv2.imwrite('img1/pic1_red.jpg', img1_red)
    cv2.imwrite('img1/pic1_blue.jpg', img1_blue)
    cv2.imwrite('img1/pic1_gray.jpg', img1_gray)
    cv2.imwrite('img1/pic1_swapped.jpg', img1_swap)
    cv2.imwrite('img1/pic1_hsv.jpg', img1_hsv)
    cv2.imwrite('img1/pic1_shifted.jpg', img1_shift)
    cv2.imwrite('img1/pic1_difference.jpg', img1_diff)
    cv2.imwrite('img1/pic1_bluenoise.jpg', img1_noise_blue)
    cv2.imwrite('img1/pic1_greennoise.jpg', img1_noise_green)
    cv2.imwrite('img1/pic1_rednoise.jpg', img1_noise_red)
    cv2.imwrite('img1/pic1_spnoise.jpg', img1_spnoise)
    cv2.imwrite('img1/pic1_blur.jpg', img_blur)

    cv2.imwrite('img2/pic2_green.jpg', img2_green)
    cv2.imwrite('img2/pic2_red.jpg', img2_red)
    cv2.imwrite('img2/pic2_blue.jpg', img2_blue)
    cv2.imwrite('img2/pic2_gray.jpg', img2_gray)
    cv2.imwrite('img2/pic2_swapped.jpg', img2_swap)
    cv2.imwrite('img2/pic2_hsv.jpg', img2_hsv)
    cv2.imwrite('img2/pic2_shifted.jpg', img2_shift)
    cv2.imwrite('img2/pic2_difference.jpg', img2_diff)
    cv2.imwrite('img2/pic2_bluenoise.jpg', img2_noise_blue)
    cv2.imwrite('img2/pic2_greennoise.jpg', img2_noise_green)
    cv2.imwrite('img2/pic2_rednoise.jpg', img2_noise_red)
    cv2.imwrite('img2/pic2_spnoise.jpg', img2_spnoise)
    cv2.imwrite('img2/pic2_blur.jpg', img2_blur)

    cv2.imwrite('embedded.jpg', embed_img)

    # Print the statistics of the grayscale images
    print("Grayscale Image Statistics:\n")
    print(f"Image 1:\n - Mean: {img1_stats[0][0][0]}\n - Standard Deviation: {img1_stats[1][0][0]}")
    print(f"\n\nImage 2:\n - Mean: {img2_stats[0][0][0]}\n - Standard Deviation: {img2_stats[1][0][0]}")

if __name__ == '__main__':
    main()