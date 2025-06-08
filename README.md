# 🖼️ FastAPI + Docker + Vision: Demo Project

A mini project to learn Docker Compose, FastAPI, OpenCV, multi-container setup, inter-service communication.

---

## 📦 Project Overview

This project uses a **multi-container Docker architecture** to build an image processing service with a simple front-end and backend:

- `app/`: Frontend + API container (FastAPI)
- `processor/`: Image processing container (OpenCV via FastAPI)
- `docker-compose.yml`: Defines service relationships

---

## 🧰 Tech Stack

| Component     | Tech Used              |
|---------------|------------------------|
| Backend       | FastAPI                |
| Image Processing | OpenCV (Grayscale filter) |
| Frontend      | HTML + JS (vanilla)    |
| Communication | FastAPI internal REST  |
| Containerization | Docker & Docker Compose |
| DevOps        | Multi-container architecture |

---

## 🧪 How it Works

1. Open `http://localhost:8000/` in your browser.
2. Upload an image via the HTML file input.
3. The image is sent to the `/upload/` endpoint.
4. FastAPI forwards the image to `processor:5000/process/`.
5. The processor:
   - Decodes the image
   - Applies a grayscale filter
   - Sends it back
6. The UI shows the processed image.

---

## 🗂️ Project 
```bash
project-root/
├── app/
│ ├── main.py
│ ├── requirements.txt
│ ├── static/
│ │ ├── script.js
│ │ └── result.jpg
│ └── templates/
│ └── index.html
├── processor/
│ ├── processor.py
│ ├── requirements.txt
│ └── Dockerfile
├── docker-compose.yml
└── README.md
 ```

## 🚀 Quick Start

### 🔧 1. Clone and build

```bash
git clone https://github.com/vickyr95/fastapi-docker-vision-demo.git
cd fastapi-docker-vision-demo
docker-compose up --build
```
### 🌐 2. Visit in Browser
```bash
http://localhost:8000/
```
Upload an image to see it processed and displayed.

## 🐳 Docker Compose Services

| Service     | Description              | Port              |
|---------------|------------------------|-------------------|
| `app`       | 	Handles frontend and uploads                |  `8000` |
| `processor` | Processes images via OpenCV | `5000` (internal only)|

## 🛠️ API Reference
`POST /upload/`
- Accepts image file
- Sends to processor
- Returns processed image path

`POST /process/` (internal)
- Accepts image file
- Applies grayscale filter
- Returns processed image bytes

## 🔍 Current Features
- ✅ Image upload via frontend UI
- ✅ REST API for backend-to-backend calls
- ✅ Grayscale filter using OpenCV
- ✅ Live reload via Docker Compose
- ✅ Cache-busting for latest images
- ✅ Multi-container orchestration with Docker Compose

## 🔜 Next Steps & Roadmap
| Task                        | Description                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| 📸 Add Camera Button        | Add a button to request camera stream from user system                 |
| 🎥 Video Feed Support       | Use OpenCV to show a live webcam feed in-browser                       |
| 🧠 YOLO Object Detection    | Add another container with YOLOv5 or YOLOv8 model for object detection |
| 🧪 Camera Relay             | Share live camera feed from app → YOLO container for object detection  |
| 🧩 Add filter options       | Let user choose grayscale, blur, edge detection, sepia, etc.           |
| 📤 Download Processed Image | Add "Download" button to save processed image                          |
| 🔄 WebSocket Streaming      | Replace polling with real-time frame updates via WebSockets            |
| 🧪 Unit Tests               | Add tests for endpoints and image outputs                              |
| 🤝 GitHub Fork + PR Flow    | Document how to fork, clone, and create pull requests                  |

## 🤔 Why This Project?
This project is a perfect hands-on playground to understand:
- Real-world Docker Compose usage
- RESTful APIs across containers
- Python + JS integration
- OpenCV filter pipelines
- Future expansion to live feeds and ML pipelines