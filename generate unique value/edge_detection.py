import cv2
import numpy as np

def draw_approx_hull_polygon(img, cnts):
    img = np.copy(img)
    img = np.zeros(img.shape, dtype=np.uint8) #create a new blank canvas

    cv2.drawContours(img, cnts, -1, (255, 0, 0), 2)  # draw all contour points in blue

    min_side_len = img.shape[0] / 32  #  the minimum side length of polygon
    min_poly_len = img.shape[0] / 16  # the minimum round length of polygon
    min_side_num = 3  # the minimum number of sides
    approxs = [cv2.approxPolyDP(cnt, min_side_len, True) for cnt in cnts]  # draw polygons with the limitation
    approxs = [approx for approx in approxs if cv2.arcLength(approx, True) > min_poly_len]  # filter out polygons whose perimeters are less than min
    approxs = [approx for approx in approxs if len(approx) > min_side_num]  # filter out polygons whose sides are less than min
    cv2.polylines(img, approxs, True, (0, 255, 0), 2)  # draw polygon in green

    #find the convex hulls of all contour points and draw
    hulls = [cv2.convexHull(cnt) for cnt in cnts] 
    cv2.polylines(img, hulls, True, (0, 0, 255), 2)  # red


    for cnt in cnts:
        cv2.drawContours(img, [cnt, ], -1, (255, 0, 0), 2)  # blue
    
        epsilon = 0.02 * cv2.arcLength(cnt, True)  #set the precision 
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        cv2.polylines(img, [approx, ], True, (0, 255, 0), 2)  # green
    
        hull = cv2.convexHull(cnt)
        cv2.polylines(img, [hull, ], True, (0, 0, 255), 2)  # red
    return img


def run():
    image = cv2.imread('test1.png')  # INPUT (a black objects on white image is better)

    thresh = cv2.Canny(image, 128, 256)  # perform edge detection

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   

    imgs = [
        image, thresh,

        draw_approx_hull_polygon(image, contours),  #draw the polygon
    ]

    for img in imgs:
        # cv2.imwrite("%s.jpg" % id(img), img)
        cv2.imshow("contours", img)
        cv2.waitKey(1943)


if __name__ == '__main__':
    run()
pass