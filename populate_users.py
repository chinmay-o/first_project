import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#IMPORTING ESSENTIAL MODULES
import random
from first_app.models import User
from faker import Faker

fake_detail = Faker()

#Adding Fake Populations
def populate(N=5):

    for entry in range(N):

        #Fake User
        fake_first_name = fake_detail.first_name()
        fake_last_name = fake_detail.last_name()
        fake_email = fake_detail.email()

        #Add Data to Database
        user_data = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':

    print("Populating Scripts")
    populate(20)
    print("Population Completed")
