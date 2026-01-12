FROM python:3.11-slim

# منع Python من إنشاء __pycache__
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# تثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ المشروع كامل
COPY . .

# إنشاء مجلدات الرفع (مهم)
RUN mkdir -p uploads obxod

# فتح البورت
EXPOSE 8001

# تشغيل FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
