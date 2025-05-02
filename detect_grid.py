import cv2
import numpy as np

# === Load Image ===
image = cv2.imread("assets/first_frame.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# === Step 2: Edge detection ===
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# === Step 3: Hough Line Transform ===
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=40, maxLineGap=10)

# === Step 4: Draw lines ===
line_image = image.copy()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Detected Mosaic Tiles", line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
