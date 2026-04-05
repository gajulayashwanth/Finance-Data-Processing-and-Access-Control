from django.contrib import admin
from .models import FinancialRecord

@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'transaction_type', 'category', 'amount', 'date')
    
    
    list_filter = ('transaction_type', 'date', 'category')
    
    
    search_fields = ('category', 'notes', 'user__username')