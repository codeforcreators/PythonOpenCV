# import the OpenCV library.
import cv2

# To read an image, use the cv2.imread() function.
img_colour = cv2.imread('daisy.jpg',1)
img_gray = cv2.imread('daisy.jpg',0)
img_unchanged = cv2.imread('daisy.jpg',-1)


# The cv2.imshow() function is used to show an image in a window.
cv2.imshow('Colour Image',img_colour)
cv2.imshow('Grayscale Image',img_gray)
cv2.imshow('Unchanged Image',img_unchanged)

# The waitKey() method is used to wait for a key press to shut the window, and the value 0 indicates an unlimited loop.
cv2.waitKey(0)

# cv2.destroyAllWindows() simply removes all of the windows that we have generated.
cv2.destroyAllWindows()