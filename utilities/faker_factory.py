from faker import Faker


class FakerFactory:
    """This class is used to generate test data."""
    def __init__(self):
        self.faker = Faker()

    def generate_first_name(self):
        return self.faker.first_name()

    def generate_last_name(self):
        return self.faker.last_name()

    def generate_zip_code(self):
        return self.faker.zipcode()
