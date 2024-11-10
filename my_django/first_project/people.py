import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#Fake Pop Script
import random
from nanedu.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Course', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        
        #Get The Topic For The Entry
        top = add_topic()
        
        #Create The Fake Data For That Entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #Create The New Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]
        
        #Create A Fake Access Record For That Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populating Complete!")