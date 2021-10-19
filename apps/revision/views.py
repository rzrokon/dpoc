from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PageSerializer
from .models import Page

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all().order_by('name')
    serializer_class = PageSerializer



# from django.shortcuts import render
# from django.http import HttpResponse
# import json
# from rest_framework import viewsets
# from .serializers import PageSerializer
# from .models import Page, Ticket

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from reversion.models import Version
from django.db.models import F

class PageHistoryView(APIView):

    def get(self, request, page_id):

        data = '[][]][][][]'

        page = Page.objects.get(id=page_id)
        print(page)
        versions = Version.objects.get_for_object(page)
        print(versions)

        data = versions.values('pk',
                            'revision__date_created',
                            'revision__comment',
                            'revision__id',
                            'revision__user',
                            'revision__user_id',
                            'revision__version',
                            'pk')

        return Response({"data": data})