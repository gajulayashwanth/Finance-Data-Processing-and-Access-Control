from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FinancialRecordViewSet, DashboardSummaryView


router = DefaultRouter()
router.register(r'records', FinancialRecordViewSet, basename='records')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]