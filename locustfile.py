from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_all_guards(self):
        # استدعاء بدون أي معاملات
        self.client.get("/get_guards")

    @task
    def get_by_project(self):
        # استدعاء مع باراميتر project_id
        self.client.get("/get_guards", params={"project_id": 1})

    @task
    def get_by_employee(self):
        # استدعاء مع أكثر من باراميتر
        self.client.get("/get_guards", params={"project_id": 2, "employee_id": 10})
