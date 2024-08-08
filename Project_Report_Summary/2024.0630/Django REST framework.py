from django.db import models

class Book(models.Model): # Define a model class named Book to represent books
    title = models.CharField(max_length=200) # Define the book title, using CharField for a character field with a maximum length of 200
    
    author = models.ForeignKey('Author', on_delete=models.CASCADE) # Define the book author, using ForeignKey to link to the Author model
    published_date = models.DateField() # Define the publication date, using DateField for a date field

    # Define the __str__ method to return the string representation of the object
    # This makes it easier to view objects in the admin interface and shell
    def __str__(self):
        return self.title

class Author(models.Model): # Define a model class named Author to represent authors
    name = models.CharField(max_length=100) # Define the author's name, using CharField for a character field with a maximum length of 100
    
    # Define the __str__ method to return the string representation of the object
    def __str__(self):
        return self.name

from rest_framework import serializers # Import the serializers module from Django REST framework
from .models import Author, Book # Import the Author and Book models from the previously created models module

class BookSerializer(serializers.ModelSerializer): # Define the BookSerializer class, inheriting from serializers.ModelSerializer
    class Meta: # Define the Meta inner class to specify serializer metadata
        model = Book # Specify that the serializer corresponds to the Book model
        fields = ['id','title','author','published_date'] # Specify the list of fields to include in the serializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author # Specify that the serializer corresponds to the Author model
        fields = ['id','name']

from rest_framework import viewsets # Import the viewsets module from Django REST framework
from .models import Author, Book # Import the Author and Book models from the current application's models module
from .serializers import AuthorSerializer, BookSerializer # Import the AuthorSerializer and BookSerializer from the current application's serializers module

class BookViewSet(viewsets.ModelViewSet): # Define a viewset class named BookViewSet, inheriting from viewsets.ModelViewSet
    queryset = Book.objects.all() # Define the dataset to query for the viewset
    serializer_class = BookSerializer # Specify the serializer class to use for the viewset
    
class AuthorViewSet(viewsets.ModelViewSet): # Define a viewset class named AuthorViewSet, inheriting from viewsets.ModelViewSet
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

from rest_framework.routers import DefaultRouter # Import the DefaultRouter module from Django REST framework
from .views import AuthorViewSet, BookViewSet # Import the AuthorViewSet and BookViewSet from the current application's views module

router = DefaultRouter() # Create an instance of DefaultRouter
router.register(r'authors', AuthorViewSet) # Register AuthorViewSet with the router, using 'authors' as the URL prefix
router.register(r'books', BookViewSet) # Register BookViewSet with the router, using 'books' as the URL prefix

urlpatterns = router.urls # Set urlpatterns to include all URLs automatically generated by the router