#!/usr/bin/env python
from locust import HttpLocust, TaskSet, task
import pandas as pd


class MetricsTaskSet(TaskSet):

    def on_start(self):
        data_path = 'https://raw.githubusercontent.com/artefactory-global/mlflow-serving-example/main/notebooks/wine-quality-white.csv'
        self.test_data = pd.read_csv(data_path).drop(columns='quality')

    @task()
    def post_metrics(self):
        headers = {'Content-Type': 'application/json',}
        self.client.post("/invocations", headers=headers, data=self.test_data.sample(1).to_json(orient='split'))


class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet

