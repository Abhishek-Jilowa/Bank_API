from rest_framework import generics
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer
from rest_framework.renderers import JSONRenderer

class BankList(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchDetail(generics.RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'
