import cv2

im = cv2.imread(r"C:\Users\Admin\Desktop\Python\screenshot.jpg")


def main():
    cv2.imshow("Display show", im)
    k = cv2.waitKey(0)

    if k == ord("s"):
        print("exit")


if __name__ == '__main__':
    main()
