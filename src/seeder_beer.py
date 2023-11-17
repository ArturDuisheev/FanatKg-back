import random

from faker import Faker
from faker.providers import lorem

from vacancies import models as vac_models
from price import models as price_models
from services import models as services_models
from contact import models as contact_models

fake = Faker()
fake.add_provider(lorem)

vacancies_list = ['Уборщица', 'Админ', 'охранник']
streets_list = ['Киевская 23', 'Киевская 43', 'Орозбекова 24', 'Фатьянова 24']

# def generate_status():
#
#     for status in status_options:
#         yield status

status_options = ["comfort", "econom", "premium", "basic", "deluxe"]


def generate_fake_image_url(width=640, height=480):
    return fake.image_url(width=width, height=height)


def create_vacancy():
    vac_models.Vacancy.objects.all().delete()
    for vacancy in vacancies_list:
        vac_models.Vacancy.objects.create(
            title=vacancy,
            title_ky=vacancy,
            title_en=vacancy,
            description='Lorem Ipsum',
            description_ky='Lorem Ipsum(на кг)',
            description_en='Lorem Ipsum(на англ)',
            address='Киевская 49(русс)',
            address_ky='Киевская 49(на кг)',
            address_en='Киевская 49(англ)',
            google_form='https://www.google.com/'

        )


def create_price():
    price_models.Location.objects.all().delete()
    price_models.Privilege.objects.all().delete()
    for street in set(streets_list):
        for status in set(status_options):
            if status in status_options:
                status_options.remove(status)
                privilege = price_models.Privilege.objects.create(
                    name=status,
                    name_ky=status,
                    name_en=status,
                    image=generate_fake_image_url(),
                    price_image=generate_fake_image_url()
                )

                location = price_models.Location.objects.create(
                    street=street,
                    street_ky=street,
                    street_en=street,
                    image=generate_fake_image_url(),
                )
                location.privilege.set([privilege])


def seed():
    create_vacancy()
    create_price()
