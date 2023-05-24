from lesson27.entities.people_entity import People


def test_check_person_1(people_service):
    response = people_service.get_person(1)
    print(response.json())
    assert response.json()['name'] == 'Luke Skywalker'

def test_check_person_2(people_service):
    response = people_service.get_person(2)
    keys = ['name', 'height']
    assert all(key in response.json() for key in keys)

def test_check_person_2(people_service, fifth_person):
    response = people_service.get_person(5)
    actual_leia_organa = People(
        response.json()['name'],
        response.json()['height'],
        response.json()['mass'],
        response.json()['hair_color'],
        response.json()['skin_color']
    )
    assert actual_leia_organa == fifth_person

