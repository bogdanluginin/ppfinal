from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Student, Rating
from .serializers import StudentSerializer, RatingSerializer

class StudentRatingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student_data = {'first_name': 'John', 'last_name': 'Doe'}
        self.student = Student.objects.create(**self.student_data)
        self.rating_data = {'student': self.student, 'value': 85.5}
        self.rating = Rating.objects.create(**self.rating_data)

    def test_get_student_list(self):
        response = self.client.get('/myapp/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_student(self):
        new_student_data = {'first_name': 'Jane', 'last_name': 'Doe'}
        response = self.client.post('/myapp/api/students/', new_student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
        self.assertEqual(Student.objects.last().first_name, new_student_data['first_name'])

    def test_get_student_detail(self):
        response = self.client.get(f'/myapp/api/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = StudentSerializer(self.student)
        self.assertEqual(response.data, serializer.data)

    def test_update_student(self):
        updated_data = {'first_name': 'Updated', 'last_name': 'Name'}
        response = self.client.put(f'/myapp/api/students/{self.student.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, updated_data['first_name'])

    def test_delete_student(self):
        response = self.client.delete(f'/myapp/api/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())

    def test_get_rating_list(self):
        response = self.client.get('/myapp/api/ratings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_rating(self):
        new_rating_data = {'student': self.student.id, 'value': 90.0}
        response = self.client.post('/myapp/api/ratings/', new_rating_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 2)
        self.assertEqual(Rating.objects.last().value, new_rating_data['value'])

    def test_get_rating_detail(self):
        response = self.client.get(f'/myapp/api/ratings/{self.rating.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = RatingSerializer(self.rating)
        self.assertEqual(response.data, serializer.data)

    def test_update_rating(self):
        updated_data = {'student': self.student.id, 'value': 95.0}
        response = self.client.put(f'/myapp/api/ratings/{self.rating.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.rating.refresh_from_db()
        self.assertEqual(self.rating.value, updated_data['value'])

    def test_delete_rating(self):
        response = self.client.delete(f'/myapp/api/ratings/{self.rating.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Rating.objects.filter(id=self.rating.id).exists())
