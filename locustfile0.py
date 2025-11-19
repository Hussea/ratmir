from locust import HttpUser, task, between
import base64
from datetime import date, time

class FastAPIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def add_work_shift(self):
        # توليد صورة Base64 بسيطة (تجريبية)
        with open("test_image.jpg", "rb") as img_file:
            encoded_image = "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode("utf-8")

        # بيانات النموذج
        data = {
            "employee_id_input": 1,
            "project_id_input": 2,
            "start_date": str(date.today()),
            "start_time": "09:00:00",
            "end_date": str(date.today()),
            "end_time": "17:00:00",
            "image": encoded_image
        }

        # إرسال الطلب إلى FastAPI
        with self.client.post("/add_work_shifts", data=data, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed with status {response.status_code}")
            else:
                response.success()
