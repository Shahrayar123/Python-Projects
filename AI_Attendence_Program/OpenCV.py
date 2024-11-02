try:
    import cv2
    print("OpenCV is installed and imported successfully.")
except ImportError:
    print("OpenCV is not installed. Please install OpenCV using pip:")
    print("    pip install opencv-python")