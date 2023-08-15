import cv2

im = cv2.imread(r"C:\Users\Admin\Desktop\Python\screenshot.jpg")


def main():
    cv2.imshow("Display show", im)
    k = cv2.waitKey(0)

    if k == ord("s"):
        print("exit")


def webcam_capture():
    capture = cv2.VideoCapture(0)

    if not capture.isOpened():
        print("Камера не может быть открыта.")
        exit()

    while True:
        ret, frame = capture.read()
        if not ret:
            print("Камера не может быть открыта.")
            break
        cv2.imshow("WEBCAM", frame)

        k = cv2.waitKey(0)
        if k == ord("s"):
            print("exit")
            break
    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    webcam_capture()
