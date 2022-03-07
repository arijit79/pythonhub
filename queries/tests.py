from django.test import TestCase
from .models import Query
from users.models import User

# Create your tests here.
class QueryTest(TestCase):
    def setup(self):
        user = User(first_name="Test", last_name="User",
                        email="email@email.com", password="password")
        user.save()
        return user

    def testnew_query(self):
        user = self.setup()
        new_query = Query(title="Test", content="Query", asked_by=user)
        new_query.save()
        query = Query.objects.filter(id=1).first()
        super().assertEqual(query.title, "Test")
