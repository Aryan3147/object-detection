# 🎯 Real-Time Object Detection with YOLO

A project for real-time object detection using your computer's camera and YOLO (You Only Look Once) deep learning model.

## 📋 What This Project Does

This application uses your webcam to detect and identify objects in real-time. It can recognize 80+ different objects like:
- 👤 People
- 🚗 Cars, trucks, buses
- 🐕 Animals (dogs, cats, birds, etc.)
- 🛋️ Furniture (chairs, couches, tables)
- 📱 Electronics (cell phones, laptops, TVs)
- And many more!

## 🚀 Quick Start Guide

### Step 1: Install Python
Make sure you have Python 3.11:
```bash
python --version
```

If you don't have Python, download it from: https://python.org

### Step 2: Create Project Folder
Open your terminal/command prompt and navigate to where you want the project:
```bash
mkdir object-detection
cd object-detection
```

### Step 3: Create Virtual Environment (Recommended)
This keeps your project dependencies separate from other projects:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Required Packages
```bash
pip install -r requirements.txt
```

This will download:
- **Ultralytics YOLO** - The AI model for object detection
- **OpenCV** - For camera access and video display
- **PyTorch** - The deep learning framework

**Note:** First installation may take 5-10 minutes as it downloads the AI model.

### Step 5: Run the Application
```bash
python detection.py
```

## 🎮 How to Use

Once the program starts:
- **The camera feed will appear** with boxes around detected objects
- **Green labels** show what each object is (e.g., "person", "car")
- **FPS counter** shows how smooth the detection is running
- **Object counter** shows how many objects are detected

### Keyboard Controls:
- **`Q`** - Quit the application
- **`S`** - Save a screenshot of the current frame

## 📁 Project Files

```
object-detection/
├── detection.py       # Main application code
├── requirements.txt   # List of dependencies
└── README.md         # This file
```

## 🛠️ How It Works (For Beginners)

### 1. YOLO Model
YOLO (You Only Look Once) is a pre-trained AI model that can recognize objects in images. We use the "YOLOv8 Nano" version because it's:
- ✅ Fast (works on most computers)
- ✅ Accurate enough for most use cases
- ✅ Small file size (~6MB)

### 2. The Process
```
Camera Frame → YOLO Model → Detection Results → Draw Boxes → Display
```

1. **Capture**: Gets video frames from your webcam
2. **Detect**: AI analyzes each frame for objects
3. **Annotate**: Draws boxes and labels around detected objects
4. **Display**: Shows the result on your screen

### 3. Confidence Score
The model shows how confident it is about each detection (50% threshold by default). Higher confidence = more accurate detection.

## 🔧 Customization

### Change Camera
If you have multiple cameras, change this line in `detection.py`:
```python
cap = cv2.VideoCapture(0)  # Change 0 to 1, 2, etc.
```

### Adjust Detection Confidence
To make detections more or less strict, change the `conf` value:
```python
results = model(frame, conf=0.7)  # More strict (70% confidence)
results = model(frame, conf=0.3)  # Less strict (30% confidence)
```

### Use a Different YOLO Model
Choose from different model sizes:
- `yolov8n.pt` - Nano (fastest, smallest)
- `yolov8s.pt` - Small (good balance)
- `yolov8m.pt` - Medium (more accurate, slower)
- `yolov8l.pt` - Large (most accurate, requires good GPU)

Change this line in the code:
```python
model = YOLO('yolov8s.pt')  # Use small model instead
```

## 🐛 Troubleshooting

### "Could not open camera"
- Make sure your camera is connected
- Close other apps using the camera (Zoom, Skype, etc.)
- Try changing the camera index (0 → 1)

### "No module named 'ultralytics'"
- Make sure you activated the virtual environment
- Run `pip install -r requirements.txt` again

### "Model download fails"
- Check your internet connection
- The model downloads automatically on first run (~6MB)
- You can manually download from https://github.com/ultralytics/assets/releases

### Slow performance / Low FPS
- Use a smaller YOLO model (`yolov8n.pt`)
- Close other applications
- Lower camera resolution (add `cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)`)

## 📚 Learn More

### Resources for Beginners
- **YOLO Documentation**: https://docs.ultralytics.com
- **OpenCV Tutorials**: https://docs.opencv.org/4.x/d9/df8/tutorial_root.html
- **Python Basics**: https://docs.python.org/3/tutorial/

### What to Try Next
1. **Record video**: Save the detection output to a file
2. **Count specific objects**: Count how many people appear
3. **Alert system**: Play sound when specific object detected
4. **Custom objects**: Train YOLO on your own dataset

## 📜 License

This project is open source. Feel free to modify and share!

## 💡 Tips

- Good lighting helps the camera detect objects better
- Keep objects at a reasonable distance from the camera
- The model works best with common objects (people, cars, animals)
- Have fun experimenting!

---
