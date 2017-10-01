import cv2
import numpy as np
from matplotlib import pyplot as plt


def read_lines():

    img = cv2.imread('./sudoku.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100,
                            minLineLength=1, maxLineGap=10)
    for line in lines:
        # print(line[0])
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite('houghlines.jpg', img)


def detect_rects():
    img = cv2.imread('houghlines.jpg', 0)
    # crop_img = img[55: 110, 165:220]
    # cv2.imshow('shit', crop_img)
    # cv2.waitKey(0)
    max = len(img) // 55
    count = 0

    for i in range(0, max, 1):
        for j in range(0, max, 1):
            inner = 55 * j
            print("i:{} j:{}".format(i * 55, j * 55))
            crop_img = img[(55 * i):(55 * (i + 1)),
                           (55 * j):(55 * (j + 1))]
            cv2.imwrite('ocr_cell_' + str(count) + '.jpg', crop_img)
            count = count + 1

    print(count)

    # im = cv2.imread('test.jpg')
    # imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    # im2, contours, hierarchy = cv2.findContours(
    #    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnt = contours[4]
    # cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
    # rsz_img = cv2.resize(im, None, fx=0.25, fy=0.25)
    # cv2.imshow('', rsz_img)
    # cv2.waitKey(0)

    # img = cv2.GaussianBlur(img, (25, 25), 0)
    # kernel = np.ones((5, 5), np.float32) / 25
    # dst = cv2.filter2D(img, -1, kernel)
    # dst = cv2.GaussianBlur(dst, (5, 5), 0)
    # crop_img = img[0: 100, 50:150]
    # cv2.imshow('shit', crop_img)
    # edges = cv2.Canny(img, 100, 200, apertureSize=3)
    # resize since image is huge
    # rsz_img = cv2.resize(dst, None, fx=0.25, fy=0.25)
    # print(len(rsz_img))
    # crop_img = rsz_img[10: 65, 15:70]
    # cv2.imshow('', crop_img)
    # cv2.waitKey(0)

    # rsz_img = cv2.resize(img, None, fx=0.25, fy=0.25)
    # max = 9
    # print(max)
    # count = 0
    # arr = []
    # for i in range(0, max, 1):
    #    for j in range(0, max, 1):
    #        inner = 55 * j
    #        print("i:{} j:{}".format(i * 55, j * 55))
    #        crop_img = rsz_img[(10 + (55 * i)):(10 + (55 * (i + 1))),
    #                           (15 + (55 * j)):(15 + (55 * (j + 1)))]
    #        crop_img = cv2.resize(crop_img, (28, 28))
    #        arr.append(crop_img)
    #        cv2.imwrite('gray_cell_' + str(count) + '.jpg', crop_img)
    #        count = count + 1

    # print(count)
    # print(arr[0][0])


if __name__ == '__main__':
    read_lines()
    detect_rects()
