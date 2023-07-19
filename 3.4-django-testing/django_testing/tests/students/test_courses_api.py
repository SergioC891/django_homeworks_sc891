import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(api_client, courses_factory, students_factory):
    courses = courses_factory(_quantity=1)

    response = api_client.get(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_get_courses(api_client, courses_factory, students_factory):
    courses = courses_factory(_quantity=10)

    response = api_client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


@pytest.mark.django_db
def test_course_filter_by_id(api_client, courses_factory, students_factory):
    courses = courses_factory(_quantity=10)

    response = api_client.get('/api/v1/courses/', {'id': courses[5].id})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[5].id


@pytest.mark.django_db
def test_course_filter_by_name(api_client, courses_factory, students_factory):
    courses = courses_factory(_quantity=10)

    response = api_client.get('/api/v1/courses/', {'name': courses[4].name})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[4].name


@pytest.mark.django_db
def test_create_course(api_client, courses_factory, students_factory):
    response = api_client.post('/api/v1/courses/', data={'name': 'Computer Science'})

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(api_client, courses_factory, students_factory):
    courses = courses_factory(_quantity=1)

    name_value = 'Artificial Intelligence'
    response = api_client.patch(f'/api/v1/courses/{courses[0].id}/', {'name': name_value})

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == name_value


@pytest.mark.django_db
def test_delete_course(api_client, courses_factory, students_factory):
    courses = courses_factory(_quantity=3)

    response = api_client.delete(f'/api/v1/courses/{courses[1].id}/')

    assert response.status_code == 204
