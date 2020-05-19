from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):  
    @task
    def index(self):
        self.client.get("/")
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://www.mfinformatica.com/"
    min_wait = 5000
    max_wait = 15000
