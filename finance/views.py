from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .permissions import IsAdminOrAnalystReadOnly

class FinancialRecordViewSet(viewsets.ModelViewSet):
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAdminOrAnalystReadOnly] 

    def get_queryset(self):
        """
        This allows us to filter the URL like: 
        /api/finance/records/?transaction_type=EXPENSE&category=Food
        """
        queryset = FinancialRecord.objects.all()
        transaction_type = self.request.query_params.get('transaction_type')
        category = self.request.query_params.get('category')
        
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)
        if category:
            queryset = queryset.filter(category=category)
            
        return queryset

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)


class DashboardSummaryView(APIView):
    
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        
        income_agg = FinancialRecord.objects.filter(transaction_type='INCOME').aggregate(total=Sum('amount'))
        expense_agg = FinancialRecord.objects.filter(transaction_type='EXPENSE').aggregate(total=Sum('amount'))
        
        
        total_income = income_agg['total'] or 0
        total_expenses = expense_agg['total'] or 0
        net_balance = total_income - total_expenses
        
        return Response({
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_balance": net_balance
        })