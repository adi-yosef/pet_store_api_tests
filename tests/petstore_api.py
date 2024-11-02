import requests

class PetStoreAPI:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.session = requests.Session()

    def create_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = self.session.post(url, json=pet_data)
        response.raise_for_status()
        return response.json()

    def update_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = self.session.put(url, json=pet_data)
        response.raise_for_status()
        return response.json()

    def find_pets_by_status(self, status):
        url = f"{self.BASE_URL}/pet/findByStatus"
        params = {"status": status}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def delete_pet(self, pet_id):
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.json()
