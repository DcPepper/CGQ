from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import GeographySerializer
from quiz.models import Geophraphy
from rest_framework.decorators import api_view, permission_classes

@permission_classes((permissions.IsAuthenticated,))
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

class GeophraphyView(viewsets.ModelViewSet):
    """ 
    View Geophraphy
    """
    queryset = Geophraphy.objects.all()
    serializer_class = GeographySerializer
    
    def get_queryset(self):
        q = self.request.query_params.get('q') 
        query_set = super().get_queryset()
        if q:
            query_set = query_set.filter(iso__icontains=q)
        return query_set