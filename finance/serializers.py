from rest_framework import serializers
from .models import FinancialRecord

class FinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = ['id', 'user', 'amount', 'transaction_type', 'category', 'date', 'notes', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']