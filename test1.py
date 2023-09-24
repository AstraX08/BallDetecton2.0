import cv2
import numpy as np

# Focal length of the camera (in mm)
focal_length = 21.0

# Ball diameter (in mm)
ball_diameter = 190.0

# Function to calculate distance from camera to object
def calculate_distance(focal_length, actual_diameter, apparent_diameter):
    return (focal_length * actual_diameter) / apparent_diameter

# HSV color ranges for Dark Blue PANTONE 2727 C and purple Pantone 7655C
dark_blue_lower = np.array([100, 50, 50])
dark_blue_upper = np.array([140, 255, 255])

purple_lower = np.array([120, 50, 50])
purple_upper = np.array([160, 255, 255])

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color filtering
    dark_blue_mask = cv2.inRange(hsv_frame, dark_blue_lower, dark_blue_upper)
    purple_mask = cv2.inRange(hsv_frame, purple_lower, purple_upper)

    # Find contours
    contours_blue, _ = cv2.findContours(dark_blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_purple, _ = cv2.findContours(purple_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_blue:
        # Estimate ball size
        # Assuming circular shape, so using equivalent diameter
        diameter = np.sqrt(4 * cv2.contourArea(contour) / np.pi)
        if 185 <= diameter <= 195:
            # Draw mesh, center dot, and annotate
            # Calculate distance
            cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
                cv2.putText(frame, "Blue", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                distance = calculate_distance(focal_length, ball_diameter, diameter)
                cv2.putText(frame, f"Distance: {distance:.2f} mm", (cX - 50, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    for contour in contours_purple:
        # Estimate ball size
        diameter = np.sqrt(4 * cv2.contourArea(contour) / np.pi)
        if 185 <= diameter <= 195:
            # Draw mesh, center dot, and annotate
            # Calculate distance
            cv2.drawContours(frame, [contour], -1, (128, 0, 128), 2)
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
                cv2.putText(frame, "Purple", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                distance = calculate_distance(focal_length, ball_diameter, diameter)
                cv2.putText(frame, f"Distance: {distance:.2f} mm", (cX - 50, cY + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("Ball Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
