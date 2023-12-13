import cv2

def Dphoto(camera_index=0):
    # Initialize video capture for the specified camera index
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print(f"Unable to open camera {camera_index}.")
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
    
    # Adjust the focus
    focus = 120  # min: 0, max: 255, increment: 5
    cap.set(0, focus)
    
    # Capture a frame
    ret, frame = cap.read()
    
    if ret:
        # Save the frame as a PNG image
        filename = f'img_test/photo.png'
        cv2.imwrite(filename, frame)
        print(f"Photo taken from camera {camera_index} and saved as {filename}.")
    else:
        print("Failed to capture a frame.")
    
    # Release the camera capture object
    cap.release()

# Capture from the connected camera (external webcam)
Dphoto(camera_index=0)

# Capture from the built-in camera (camera index may vary, often 1)
Dphoto(camera_index=1)