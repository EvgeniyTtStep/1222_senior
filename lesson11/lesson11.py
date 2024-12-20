import cv2
from PIL import Image

image_path = "cat.jpeg"

cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
img = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(img)

# cv2.imshow("Cat", img)
# cv2.waitKey()

cat = Image.open(image_path)
glasses = Image.open("glasses.png")

for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/2)))
    cat.paste(glasses, (x, int(y + h / 4)), glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()