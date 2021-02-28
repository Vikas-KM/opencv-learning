# importing the necessary opencv libraries
import cv2

# reading the image using the opencv
img = cv2.imread('./images/portrait.jpg', cv2.IMREAD_COLOR)

# function which takes the image and converts to pencil sketch
def convert_to_pencil_sketch(img_rgb, canvas=None):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    blurred_image = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    gray_sketch = cv2.divide(img_gray, blurred_image, scale=256)
    if canvas is not None:
        gray_sketch = cv2.multiply(gray_sketch, canvas, scale=1 / 256)
    return cv2.cvtColor(gray_sketch, cv2.COLOR_GRAY2RGB)

# condition check if the image was read properly
if img is None:
    print('No Image found!')
else:
    img = convert_to_pencil_sketch(img)
    cv2.imwrite('./images/pencil_sketch.jpg', img)

# displaying the pencil sketch of the image
cv2.imshow('Test image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
