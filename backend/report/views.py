from rest_framework import generics
from django.db import connection
from django.db.utils import OperationalError
from django.http.response import JsonResponse


from report import models
from report import serializers



class MaterialTransactionListView(generics.ListCreateAPIView):
    serializer_class = serializers.MaterialTransactionSerializer

    def get_queryset(self):
        # Order the queryset by the created_at field in descending order
        queryset = models.MaterialTransaction.objects.order_by('-id')

        # Limit the result to just one item
        return queryset[:1]
    

def check_database_connection(request):
    try:
        with connection.cursor():
            # Try to execute a simple query to check the database connection
            pass
        return JsonResponse({'message': 'Database connected.'})
    except OperationalError as e:
        # Handle the database connection error
        error_message = str(e)
        return JsonResponse({'error': 'Database connection error', 'message': error_message}, status=500)