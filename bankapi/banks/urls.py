from django.urls import path
from .views import BankList, BranchDetail

urlpatterns = [
    path('banks/', BankList.as_view(), name='bank-list'),
    path('branches/<str:ifsc>/', BranchDetail.as_view(), name='branch-detail'),
]
