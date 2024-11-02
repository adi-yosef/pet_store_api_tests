import pytest
from petstore_api import PetStoreAPI

@pytest.fixture(scope="class")
def api():
    return PetStoreAPI()

@pytest.fixture(scope="class")
def pet_data(api, request):
    pet_data = {
        "id": 123456,
        "name": "Fluffy",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "http://example.com/photo1.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "cute"
            }
        ],
        "status": "available"
    }
    created_pet = api.create_pet(pet_data)
    assert created_pet["id"] == pet_data["id"], "Failed to create pet"

    request.cls.api = api
    request.cls.pet_data = pet_data
    yield pet_data

    api.delete_pet(pet_data["id"])
