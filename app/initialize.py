from datetime import datetime

from django.contrib.auth.models import User
from app.models import *


def initialize():
    user1 = User.objects.create(
        username='nima',
        first_name='Nima',
        last_name='modares gorji',
        password='12345',
    )

    user2 = User.objects.create(
        username='bardia',
        first_name='bardia',
        last_name='eghbali',
        password='12345',
    )

    lab1 = Laboratory.objects.create(
        name='salam lab'
    )

    lab2 = Laboratory.objects.create(
        name='sab lab'
    )

    Expert.objects.create(
        user=user1,
        laboratory=lab1
    )

    Expert.objects.create(
        user=user2,
        laboratory=lab2
    )

    patient1 = Patient.objects.create(
        user=user2
    )

    Address.objects.create(
        address='kerman',
        patient=patient1,
    )

    Address.objects.create(
        address='theran, borj-e milad',
        patient=patient1,
    )

    test_description1 = TestDescription.objects.create(
        name='khoon'
    )

    test_description2 = TestDescription.objects.create(
        name='edrar'
    )

    test_description3 = TestDescription.objects.create(
        name='aids'
    )

    LabTest.objects.create(
        name='khoon',
        available=True,
        lab=lab1,
        test_description=test_description1,
    )

    LabTest.objects.create(
        name='edrar',
        available=False,
        lab=lab1,
        test_description=test_description2,
    )

    LabTest.objects.create(
        name='aids',
        available=True,
        lab=lab1,
        test_description=test_description3,
    )

    LabTest.objects.create(
        name='khoon',
        available=True,
        lab=lab2,
        test_description=test_description1,
    )

    LabTest.objects.create(
        name='edrar',
        available=True,
        lab=lab2,
        test_description=test_description2,
    )

    LabTest.objects.create(
        name='aids',
        available=False,
        lab=lab2,
        test_description=test_description3,
    )

    TimeSlot.objects.create(
        lab=lab1,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(minutes=30),
    )

    TimeSlot.objects.create(
        lab=lab1,
        start_date=datetime.now() + timedelta(days=1),
        end_date=datetime.now() + timedelta(days=1, minutes=30),
    )

    TimeSlot.objects.create(
        lab=lab1,
        start_date=datetime.now() + timedelta(days=2),
        end_date=datetime.now() + timedelta(days=2, minutes=30),
    )

    TimeSlot.objects.create(
        lab=lab2,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(minutes=30),
    )

    TimeSlot.objects.create(
        lab=lab2,
        start_date=datetime.now() + timedelta(days=1),
        end_date=datetime.now() + timedelta(days=1, minutes=30),
    )

    TimeSlot.objects.create(
        lab=lab2,
        start_date=datetime.now() + timedelta(days=2),
        end_date=datetime.now() + timedelta(days=2, minutes=30),
    )

