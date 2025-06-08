from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import cv2
import numpy as np

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "Processor is running"}

@app.post("/process/")
async def process_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        # Convert to numpy array and decode into OpenCV image
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if img is None:
            print("Failed to decode image")
            return Response(status_code=400, content=b"Failed to decode image")

        # ✅ Image processing (example: grayscale)
        processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Encode back to JPEG format
        success, encoded_image = cv2.imencode(".jpg", processed)
        if not success:
            print("Failed to encode image")
            return Response(status_code=500, content=b"Failed to encode image")

        # Return the processed image bytes
        return Response(content=encoded_image.tobytes(), media_type="image/jpeg")

    except Exception as e:
        print(f"Error processing image: {e}")
        return Response(status_code=500, content=b"Internal server error")
