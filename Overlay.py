import os

import cv2 as cv
import numpy as np

windowSize = 40
overlay_alpha = 0.7

originImage = cv.imread("PATH_TO_THE_INPUT_PICTURE")
orig_height, orig_width, _ = originImage.shape

newHeight = round(orig_height / windowSize)
newWidth = round(orig_width / windowSize)

originImage = cv.resize(
    originImage, (newWidth, newHeight), interpolation=cv.INTER_NEAREST_EXACT
)

overlay_texture_path = "PATH_TO_THE_TEXTURE"
overlay_texture = None
if os.path.exists(overlay_texture_path):
    overlay_texture = cv.imread(overlay_texture_path)
    overlay_texture = cv.resize(
        overlay_texture, (windowSize, windowSize), interpolation=cv.INTER_LINEAR
    )

    overlay_gray = cv.cvtColor(overlay_texture, cv.COLOR_BGR2GRAY)

    shadow_mask = cv.bitwise_not(overlay_gray)

    shadow_mask = cv.normalize(
        shadow_mask, None, alpha=0, beta=overlay_alpha * 255, norm_type=cv.NORM_MINMAX
    )

    shadow_mask = cv.cvtColor(shadow_mask, cv.COLOR_GRAY2BGR)

output_height = newHeight * windowSize
output_width = newWidth * windowSize

img = np.full((output_height, output_width, 3), 255, dtype="uint8")

for i in range(newHeight):
    for j in range(newWidth):
        current_color = originImage[i, j]

        color_block = np.full((windowSize, windowSize, 3), current_color, dtype="uint8")

        if overlay_texture is not None:
            blended_block = cv.subtract(color_block, shadow_mask)
        else:
            blended_block = color_block

        x, y = i * windowSize, j * windowSize
        img[x : x + windowSize, y : y + windowSize] = blended_block

cv.imshow("Display window", img)
cv.imwrite("output_image_with_shadows_only.png", img)
cv.waitKey(0)
cv.destroyAllWindows()
