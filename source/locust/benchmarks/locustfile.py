import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_movies(self):
        self.client.get("/api/Movies")


    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    def on_start(self):
        self.client.post("/api/Movies", json={ "title": "string", "overview": "string","poster_path": "string" })