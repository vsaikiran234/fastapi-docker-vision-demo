FROM python:3.10

WORKDIR /app

# 🩹 Fix OpenCV's missing libGL.so.1 issue
RUN apt-get update && apt-get install -y libgl1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "processor:app", "--host", "0.0.0.0", "--port", "5000"]
