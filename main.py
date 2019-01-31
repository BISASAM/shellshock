from PIL import Image, ImageGrab
'''
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('screenshot.png', 0)
img2 = img.copy()
template = cv.imread('hook.png', 0)
w, h = template.shape[::-1]

img = img2.copy()
method = cv.TM_SQDIFF_NORMED

# Apply template Matching
res = cv.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img, top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(method)
plt.show()
'''

import cv2 as cv
import numpy as np


img = cv.imread(cv.samples.findFile('screenshot.png'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv.imwrite('houghlines5.jpg', img)

