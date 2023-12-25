from data.data import User
from faker import Faker

faker = Faker()


def person_generator():
    yield User(
        full_name=faker.first_name() + " " + faker.last_name(),
        email=faker.email(),
        current_address=faker.city(),
        permanent_address=faker.city(),
    )
