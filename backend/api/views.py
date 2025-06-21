from rest_framework import viewsets, permissions

from .serializers import GeographySerializer
from quiz.models import Geophraphy

class GeophraphyView(viewsets.ModelViewSet):
    """ 
    View Geophraphy
    """
    queryset = Geophraphy.objects.all()
    serializer_class = GeographySerializer
    
    def get_queryset(self):
        print(self.kwargs)
        return super().get_queryset().filter(iso=self.kwargs['iso'])