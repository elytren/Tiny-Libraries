from .models import Library
from rest_framework import generics
from .serializers import LibrarySerializer

# Create your views here.

class LibraryList(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer