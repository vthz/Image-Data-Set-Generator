import cv2


def readframes(fra, size):
    vid = cv2.VideoCapture(0)
    counter = 0
    key = 0
    flag = False
    while counter < fra:
        ret, frame = vid.read()
        frame = cv2.resize(frame, (size, size))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', frame)
        path = r"E:/Documents/Data Sets/RockPaperScissors Data/Coloured"
        cv2.imwrite(path + "/img%d.jpg" % counter, frame)
        # print("img%d.jpg", counter, " has been saved!")
        counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    no_frames = int(input("Enter max frames limit:"))
    size_img = int(input("Enter scale of the image:"))
    readframes(no_frames, size_img)
