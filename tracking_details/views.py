# from django.db.models import query
# from django.db.models.query_utils import Q
#from django.shortcuts import render
from django.views.generic import ListView
from .models import User_Package_Detail
from django.db.models import Q

# search result class...

class SearchClass(ListView):
    model = User_Package_Detail
    template_name = 'result.html'

    # defining quaryset
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User_Package_Detail.objects.filter(Q(tracker__icontains=query))
        return object_list
