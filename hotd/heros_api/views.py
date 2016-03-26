import json
import os

from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HotdAPI(APIView):

	renderer_classes = [JSONRenderer]

	def get(self, request, format=None):
		data = request.query_params
		try:
			return Response(data=data, status=status.HTTP_200_OK)
		except:
			return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
