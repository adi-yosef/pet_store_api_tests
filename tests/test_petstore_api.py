import pytest

@pytest.mark.usefixtures("api", "pet_data")
class TestPetStoreAPI:
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("api", "pet_data")
    def test_update_pet_status(self):
        self.pet_data["status"] = "sold"
        updated_pet = self.api.update_pet(self.pet_data)
        assert updated_pet["status"] == "sold", "Pet status not updated"

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.usefixtures("api", "pet_data")
    def test_find_pet_by_status_available(self):
        available_pets = self.api.find_pets_by_status("available")
        assert len(available_pets) >= 4, "Less than 4 pets available"
        assert available_pets[3]["name"] == "Puff", "Fourth pet's name is not Puff"
        print(f"Fourth Pet Object: {available_pets[3]}")

    @pytest.mark.regression
    @pytest.mark.usefixtures("api", "pet_data")
    def test_find_pet_by_status_sold(self):
        sold_pets = self.api.find_pets_by_status("sold")
        all_sold = all(pet["status"] == "sold" for pet in sold_pets)
        assert all_sold, "Not all pets have status 'sold'"
        print(f"Sold Pets: {sold_pets}")
