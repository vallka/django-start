from django.test import TestCase

# Create your tests here.
from .models import Contact

class ContactModelTests(TestCase):

    def test_contact_save(self):
        contact = Contact()
        contact.save()

        self.assertNotEqual(contact.id, None,'id is autocreated')
        self.assertEqual(len(Contact.objects.all()),1,'Exactly 1 record in db after save')
