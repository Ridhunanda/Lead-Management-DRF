from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from LeadApp.models import Lead
from LeadApp.serializer import LeadSerializer
from rest_framework import authentication,permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=['status','source']
    search_fields=['name','email','status','source']
    Ordering_fields=['name','added_date']

class LeadRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    # lookup_url_kwarg=""   # if we want to use other than pk

# class FilterBySource(APIView):
#     serializer_class=LeadSerializer
#     authentication_classes = [authentication.BasicAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self,request,*args,**kwargs):
#         Walk_in=Lead.objects.filter(source="Walk-in")
#         Call=Lead.objects.filter(source="Call")
#         Referral=Lead.objects.filter(source="Referral")
#         Website=Lead.objects.filter(source="Website")
#         Walk_in_ser=LeadSerializer(Walk_in)
#         Call_ser=LeadSerializer(Call)
#         Referral_ser=LeadSerializer(Referral)
#         Website_ser=LeadSerializer(Website)

#         result={
#             "Walk-in":Walk_in_ser,
#             "Call":Call_ser,
#             "Referral":Referral_ser,
#             "Website":Website_ser
#         }
#         return Response(result)

# class FilterByStatus(APIView):
#     serializer_class=LeadSerializer
#     authentication_classes = [authentication.BasicAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self,request,*args,**kwargs):
#         New=Lead.objects.filter(status="New")
#         Contacted=Lead.objects.filter(status="Contacted")
#         Converted=Lead.objects.filter(status="Converted")
#         Lost=Lead.objects.filter(status="Lost")

#         New_ser=LeadSerializer(New)
#         Contacted_ser=LeadSerializer(Contacted)
#         Converted_ser=LeadSerializer(Converted)
#         Lost_ser=LeadSerializer(Lost)

#         result={
#             "New":New_ser,
#             "Contacted":Contacted_ser,
#             "Converted":Converted_ser,
#             "Lost":Lost_ser
#         }
#         return Response(result)

class FilterByStatus(APIView):            #   onother way to filter, got from gemini
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        statuses = ["New", "Contacted", "Converted", "Lost"]

        data = {
            status: LeadSerializer(
                Lead.objects.filter(status=status),
                many=True
            ).data
            for status in statuses
        }

        return Response(data)

