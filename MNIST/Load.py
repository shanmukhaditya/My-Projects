import cv2
import matplotlib.pyplot as plt
IMG_SIZE=28
def LoadImage(image):
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    try:
        img = img[:, :, 3]
    except:
        pass
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    plt.imshow(img)
