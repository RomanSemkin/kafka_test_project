import json
import requests


class SiteChecker:
    url = None

    def __init__(self, url):
        self.url = url

    def check(self):
        response = requests.get(self.url)
        data = {
            "code": response.status_code,
            "request_time": response.elapsed.total_seconds(),
            "method": response.request.method,
            "content-type": response.headers.get("content-type"),
        }
        return json.dumps(data)
