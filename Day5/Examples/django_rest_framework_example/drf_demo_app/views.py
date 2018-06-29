from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from json import loads
from .models import DemoTable

class DemoTableView(APIView):

    def put(self, request):
        try:
            dt = DemoTable(attr1=request.data.get('attr1'),
                           attr2=request.data.get('attr2'))
            dt.save()
            return Response({'response': 'created'})
        except Exception as e:
            # Exception will occur that PUT doesnt exist
            print('Exception occured !', e)
            # If any exception occured then it would mean creation was unsuccessful
            return Response({'response': 'create_failed'})

    def get(self, request):
        try:
            dts = DemoTable.objects.filter(attr1=request.query_params.get('attr1'))
            print(request.query_params.get('attr1'))
            json_dts = serializers.serialize('json', dts )
            return Response({'response': loads(json_dts)})
        except Exception as e:
            print(e)
            return Response({'response': 'read_failed'})

    def post(self, request):
        try:
            change_from = request.data.get('attr1_from')
            change_to = request.data.get('attr1_to')
            dt = DemoTable.objects.get(attr1=change_from)
            dt.attr1 = change_to
            dt.save()
            return Response({'response': 'update_ok'})
        except Exception as e:
            print(e)
            return Response({'response': 'update_failed'})

    def delete(self, request):
        try:
            dts = DemoTable.objects.filter(attr1=request.data.get('attr1'))
            len_dts = len(dts)
            dts.delete()
            return Response({'response': f'del {len_dts}'})
        except Exception as e:
            # Exception will occur that DELETE doesnt exist
            print('Exception Occured!', e)
            return Response({'response': 'delete_failed'})