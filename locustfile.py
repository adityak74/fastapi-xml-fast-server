from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)  # Wait time between tasks

    @task
    def test_file_response(self):
        self.client.get("/file-response")

    @task
    def test_optimized_file_response(self):
        self.client.get("/optimized-file-response")
