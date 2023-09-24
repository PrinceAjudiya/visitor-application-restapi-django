from rest_framework.test import APITestCase
from rest_framework import status
from .models import visitor_model, staff_member_model, drink_model, visitor_detail_model, visitor_drink_model
# Create your tests here.

class VisitorTestCase(APITestCase):

    def test_visitor(self):

        data= {
            'name': 'Test Visitor',
            'email': 'test@example.com',
            'mobile': '1234567890',
        }

        response= self.client.post('/visitor/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(visitor_model.objects.filter(name='Test Visitor').exists())


class StaffMemberTestCase(APITestCase):

    def setUp(self):

        self.staff_member= staff_member_model.objects.create(
            name='Test Staff Member',
            email='teststaffmember@email.com',
            mobile='1234567890',
            image='path/to/image.jpg',
        )

    def test_staff_member(self):

        respose= self.client.get("/staff_member/")
        
        self.assertEqual(respose.status_code, status.HTTP_200_OK)

        self.assertTrue(staff_member_model.objects.filter(name='Test Staff Member').exists())

        staff_member= staff_member_model.objects.get(name='Test Staff Member')
        self.assertEqual(staff_member.name, 'Test Staff Member')
        self.assertEqual(staff_member.email, 'teststaffmember@email.com')
        self.assertEqual(staff_member.mobile, '1234567890')
        self.assertEqual(staff_member.image, 'path/to/image.jpg')

class DrinkTestCase(APITestCase):

    def setUp(self):

        self.staff_member= staff_member_model.objects.create(
            name= 'Test Staff Member',
            email= 'teststaffmember@email.com',
            mobile= '1234567890',
            image= 'path/to/image.jpg',
        )

        self.drink = drink_model.objects.create(
            name= 'Test Drink Name',
            serve_member_name= self.staff_member,
        )

    def test_staff_member(self):

        respose = self.client.get("/drink/")
        
        self.assertEqual(respose.status_code, status.HTTP_200_OK)

        self.assertTrue(drink_model.objects.filter(name='Test Drink Name').exists())

        drink = drink_model.objects.get(name='Test Drink Name')
        self.assertEqual(drink.name, 'Test Drink Name')
        self.assertEqual(drink.serve_member_name, self.staff_member)

class VisitorDetailTestCase(APITestCase):

    def setUp(self):

        self.staff_member= staff_member_model.objects.create(
            name= 'Test Staff Member',
            email= 'teststaffmember@email.com',
            mobile= '1234567890',
            image= 'path/to/image.jpg',
        )

        self.visitor = visitor_model.objects.create(
            name= 'Test Visitor',
            email= 'testvisitor@email.com',
            mobile= '9876543210',
        )

        self.visitor_detail = visitor_detail_model.objects.create(
            staff_member_name= self.staff_member,
            visitor_name= self.visitor,
            reason= 'Some Reason',
            state= 'Inprogress',
        )

    def test_staff_member(self):

        respose = self.client.get("/visitor_details/")
        self.assertEqual(respose.status_code, status.HTTP_200_OK)

        self.assertTrue(visitor_detail_model.objects.filter(reason='Some Reason').exists())

        visitor_detail = visitor_detail_model.objects.get(reason='Some Reason')

        self.assertEqual(visitor_detail.staff_member_name, self.staff_member)
        self.assertEqual(visitor_detail.visitor_name, self.visitor)
        self.assertEqual(visitor_detail.reason, 'Some Reason')
        self.assertEqual(visitor_detail.state, 'Inprogress')

class VisitorDrinkTestCase(APITestCase):

    def setUp(self):

        self.visitor = visitor_model.objects.create(
            name= 'Test Visitor',
            email= 'testvisitor@email.com',
            mobile= '9876543210',
        )

        self.staff_member= staff_member_model.objects.create(
            name= 'Test Staff Member',
            email= 'teststaffmember@email.com',
            mobile= '1234567890',
            image= 'path/to/image.jpg',
        )

        self.drink = drink_model.objects.create(
            name= 'Test Drink Name',
            serve_member_name= self.staff_member,
        )

        self.visitor_drink = visitor_drink_model.objects.create(
            visitor_name= self.visitor,
            drink_name= self.drink,
            state= 'Inprogress'
        )

    def test_staff_member(self):

        respose = self.client.get("/visitor_drink/")
        self.assertEqual(respose.status_code, status.HTTP_200_OK)

        self.assertTrue(visitor_drink_model.objects.filter(state='Inprogress').exists())
        
        visitor_drink = visitor_drink_model.objects.get(state='Inprogress')

        self.assertEqual(visitor_drink.visitor_name, self.visitor)
        self.assertEqual(visitor_drink.drink_name, self.drink)
        self.assertEqual(visitor_drink.state, 'Inprogress')
