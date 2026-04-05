from rest_framework import permissions

class IsAdminOrAnalystReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admin can Create, Read, Update, Delete (CRUD).
    - Analyst can only Read (GET).
    - Viewer cannot access at all.
    """
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False
            
        
        if request.method in permissions.SAFE_METHODS:
            return request.user.role in ['ADMIN', 'ANALYST']
            
        
        return request.user.role == 'ADMIN'