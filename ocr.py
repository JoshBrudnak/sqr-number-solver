import cv2
import numpy as np
from ClassifyDigits import ClassifyDigits
from matplotlib import pyplot as plt

def perspective_transform():
    # print(cv2.getVersionMajor())
    img = cv2.imread('sudokupic.jpg', 0)

    img = cv2.medianBlur(img,7)
    th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,75,10)
    th4 = mask_inv = cv2.bitwise_not(th4)

    cv2.imwrite("grayer.jpg", th4)

    # img = cv2.imread("grayer.jpg", 0)
    blob = cv2.imread('sudokupic.0.jpg', 0)
    #ret,thresh = cv2.threshold(img, 40, 255, 0)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, 255, 3)
    c = max(contours, key = cv2.contourArea)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    cv2.drawContours(blob, [approx], -1, (0, 255, 0), 3)

    # c = max(contours, key = cv2.contourArea)

    pts = approx.reshape(4, 2)
    rect = np.zeros((4, 2), dtype = "float32")
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # now that we have our rectangle of points, let's compute
    # the width of our new image
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    
    # ...and now for the height of our new image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    
    # take the maximum of the width and height values to reach
    # our final dimensions
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))
    
    # construct our destination points which will be used to
    # map the screen to a top-down, "birds eye" view
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    
    # calculate the perspective transform matrix and warp
    # the perspective to grab the screen
    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(blob, M, (maxWidth, maxHeight))
    #cv2.imshow("WARPED", warp)
    #cv2.waitKey()

    cv2.imwrite("warped.jpg", warp)

def detect_rects():
    img = cv2.imread('warped.jpg', 0)
    height = img.shape[0]
    width = img.shape[1]
    h_divs = height//9
    w_divs = width//9

    count = 0
    rowCount = 0

    arr = []

    for i in range(0, height - 1, h_divs):
        rowCount = rowCount + 1
        for j in range(0, width - w_divs, w_divs):
            if not j > width or not i > height:
                crop_img = img[(i):(h_divs + i ),
                            (j):(w_divs + j )]
                crop_img = cv2.resize(crop_img, (28, 28))
                arr.append(np.asarray(crop_img).tolist())
                cv2.imwrite('ocr_cell_' + str(count) + '.jpg', crop_img)
                count = count + 1
    return arr


if __name__ == '__main__':
    perspective_transform()
    images = detect_rects()
    digit = ClassifyDigits()
    numbers = digit.classifyDigitArray(images)
    print(numbers)