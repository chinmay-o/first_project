import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#IMPORTING ESSENTIAL MODULES
import random
from first_app.models import AccessLog, Topics, Webpage
from faker import Faker

fake_detail = Faker()
topics = ['Search', 'Social', 'Market', 'News', 'Games']

#Adding Topics
def add_Topics():

    t = Topics.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

#Adding Fake Populations
def populate(N=5):

    for entry in range(N):

        #Get or Create the Topic
        top = add_Topics()

        #Fake Data
        fake_company = fake_detail.company()
        fake_url = fake_detail.url()
        fake_date = fake_detail.date()

        #Add Data to Database
        webpage_data = webpage.objects.get_or_create(topic=top, name=fake_company, url=fake_url)[0]

        AccessLog_data = AccessLog.objects.get_or_create(name=webpage_data, date=fake_date)[0]

if __name__ == '__main__':

    print("Populating Scripts")
    populate(1)
    print("Population Completed")
