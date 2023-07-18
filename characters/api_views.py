from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Character
from .serializers import CharacterSerializer

class CharacterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CharacterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]
