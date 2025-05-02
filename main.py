import pyautogui
import cv2
import numpy as np
import time

print("Starting Aimbot Script...")

# Ensure the script waits for the game window to be active
time.sleep(2)

# Take a screenshot and convert it properly for OpenCV processing
screenshot = pyautogui.screenshot()
frame = np.array(screenshot)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Convert image to HSV color space for better color detection
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define red color range (adjust as needed)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)

# Apply morphological operations to reduce noise in detection
kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Find contours of detected red objects
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Debugging step - visualize detection
cv2.imshow("Detected Areas", mask)
cv2.waitKey(1000)  # Display the window briefly for debugging

# Process valid contours
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 200:  # Adjust threshold to filter out noise
        x, y, w, h = cv2.boundingRect(contour)
        center_x = x + w // 2
        center_y = y + h // 2

        # Move mouse and click
        pyautogui.moveTo(center_x, center_y, duration=0.1)  # Smooth movement
        pyautogui.click()

        print(f"Aimed and clicked at: ({center_x}, {center_y})")

        break  # Stops after first detected target

# Close OpenCV window after debugging
cv2.destroyAllWindows()