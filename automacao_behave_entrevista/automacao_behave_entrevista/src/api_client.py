import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    @staticmethod
    def get_user(user_id: int):
        return requests.get(f"{APIClient.BASE_URL}/{user_id}")
