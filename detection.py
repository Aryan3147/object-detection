import cv2
from ultralytics import YOLO
import time

def run_obect_detection():
    """
    Main function - run real-time object detection using webcam.
    Uses YOLO model to detect objects from camera feed.
    """
    
    print("🚀 Starting Object Detection...")
    print("Loading YOLO model (this may take a moment on first run)...")
    model = YOLO('yolov8s.pt')  # Load the YOLOv8s model
    
    print("✅ Model loaded successfully!")
    print("📸 Opening camera...")
    
    cap = cv2.VideoCapture(0)  # Open the default camera (webcam)
    
    # Set camera resolution for better detection
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    if not cap.isOpened():
        print("❌ Error: Could not open camera.")
        return
    
    print("✅ Camera opened successfully!")
    print("\n🎯 Instructions:")
    print("   - Press 'Q' to quit")
    print("   - Press 'S' to save a screenshot")
    print("   - Press '+' to increase confidence threshold")
    print("   - Press '-' to decrease confidence threshold")
    print("\nStarting detection in 2 seconds...")
    time.sleep(2)  # Give user time to read instructions
    
    # Adjustable confidence threshold
    confidence_threshold = 0.6  # Start with higher threshold to reduce false positives
    
    frame_count = 0
    start_time = time.time()
    
    suspicious_classes = [] 
    
    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            print("❌ Error: Failed to read frame from camera.")
            break
        results = model(frame, conf=confidence_threshold, verbose=False) # Run YOLO detection on the frame with confidence detection
        
        # Filter and process detections
        boxes = results[0].boxes
        person_count = 0
        object_count = 0
        
        # Process each detection
        for i, box in enumerate(boxes):
            class_id = int(box.cls[0])
            class_name = results[0].names[class_id]
            confidence = float(box.conf[0])
            
            # Skip suspicious detections (optional filtering)
            if class_id in suspicious_classes:
                continue
            

                
            # Count people vs objects
            if class_id == 0:  # Person
                person_count += 1
            else:
                object_count += 1
        
        
        annotated_frame = results[0].plot()  # Get the annotated frame with detections
        
        # Calculate FPS
        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time if elapsed_time > 0 else 0
        
        # Display info on frame
        cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.putText(annotated_frame, f"People: {person_count}", (10, 70), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.putText(annotated_frame, f"Objects: {object_count}", (10, 110), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        
        cv2.putText(annotated_frame, f"Total: {person_count + object_count}", (10, 150), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Show current confidence threshold
        cv2.putText(annotated_frame, f"Conf: {confidence_threshold:.2f}", (10, 190), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
        
        
         # Tips for better detection
        cv2.putText(annotated_frame, "Tips: Good lighting, hold closer", 
                   (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        # Show the annotated frame
        cv2.imshow('People & Objects Detection', annotated_frame)
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):  # Quit on 'Q' key
            print("👋 Quitting...")
            break
        elif key == ord('s'):  # Save screenshot on 'S' key
            timestamp = time.strftime("%d:%m:%y-%H:%M:%S")
            filename = f"screenshot_{timestamp}.jpg"
            cv2.imwrite(filename, annotated_frame)
            print(f"📸 Screenshot saved as {filename}")
        elif key == ord('+') or key == ord('='):
            confidence_threshold = min(0.9, confidence_threshold + 0.05)
            print(f"⬆️ Confidence threshold increased to {confidence_threshold:.2f}")
        elif key == ord('-') or key == ord('_'):
            confidence_threshold = max(0.1, confidence_threshold - 0.05)
            print(f"⬇️ Confidence threshold decreased to {confidence_threshold:.2f}")
        
    #cleanup
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\n📊 Statistics:")
    print(f"   Total frames: {frame_count}")
    print(f"   Average FPS: {fps:.1f}")
    print("\n✨ Object detection finished!")
    
    #entry point
if __name__ == "__main__":
    try:
        run_obect_detection()
    except KeyboardInterrupt:
        print("\n👋 Interrupted by user. Exiting...")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("\nTroubleshooting:")
        print("   1. Make sure camera is connected")
        print("   2. Close other apps using the camera")
        print("   3. Check if requirements are installed: pip install -r requirements.txt")    