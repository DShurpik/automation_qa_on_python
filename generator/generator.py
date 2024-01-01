import random

from data.data import User
from faker import Faker

faker = Faker()


def person_generator():
    yield User(
        full_name=faker.first_name() + " " + faker.last_name(),
        email=faker.email(),
        current_address=faker.city(),
        permanent_address=faker.city(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=random.randint(18, 65),
        salary=random.randint(1000,5000),
        department=faker.job()
    )
