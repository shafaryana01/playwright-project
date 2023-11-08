import allure
from playwright.sync_api import APIRequestContext

from api.helpers import PetRequestHelper


@allure.title("Adding new animal test")
@allure.description("This test adds animals to the cart and checks if they have been added")
def test_add_pet(api_request_context: APIRequestContext):
    id = 4567
    name = 'Tom'
    body = PetRequestHelper.generate_body(id=id, name=name)
    new_pet = api_request_context.post(url="v2/pet", data=body)
    assert new_pet.ok, f'Response status code is not ok'
    response = api_request_context.get(url=f"v2/pet/{id}", )
    pet = response.json()

    actual_result = {'id': pet.get('id'), 'name': pet.get('name')}
    expected_result = {'id': id, 'name': name}
    assert response.ok, f'Response status code is not ok'
    assert actual_result == expected_result, \
        f'Response contains information about wrong pet. Expected {expected_result}, but was {actual_result}'
