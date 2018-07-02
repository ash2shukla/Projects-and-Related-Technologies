from rest_framework.views import APIView
from rest_framework.response import Response


class secure_methods(APIView):
    def post(self, request):
        print(dir(request))
        return Response({'asd':'asd'})