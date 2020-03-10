import requests


class ManagerBlockchain:
    def __init__(self):
        self.url = "http://localhost:3000"
        self.action_url = "/api"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def getAll(self, ns_name):
        url = self.url + self.action_url + ns_name
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload)
        return response.json()

    def getSingle(self, ns_name, id):
        url = self.url + self.action_url + ns_name + id
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload)
        return response.json()

    def add(self, ns_name, payload):
        url = self.url + self.action_url + ns_name
        response = requests.request("POST", url, headers=self.headers, data=payload)
        return response.json()
