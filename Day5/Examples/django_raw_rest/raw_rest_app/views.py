from django.http import JsonResponse
from django.core import serializers
from .models import DemoTable
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def demo_table_handler(request):
    # If request has method PUT then create a new DemoTable
    if request.method == "PUT":
        try:
            dt = DemoTable(attr1=request.PUT.get('attr1'),
                       attr2=request.PUT.get('attr2'))
            dt.save()
            return JsonResponse({'response': 'created'})
        except Exception as e:
            # Exception will occur that PUT doesnt exist
            print('Exception occured !', e)
            # If any exception occured then it would mean creation was unsuccessful
            return JsonResponse({'response': 'create_failed'})
    elif request.method == "GET":
        try:
            dts = DemoTable.objects.filter(attr1=request.GET.get('attr1'))
            json_dts = serializers.serialize('json', dts )
            return JsonResponse({'response': json_dts})
        except Exception as e:
            print(e)
            return JsonResponse({'response': 'read_failed'})
    elif request.method == "POST":
        try:
            change_from = request.POST.get('attr1_from')
            change_to = request.POST.get('attr1_to')
            dt = DemoTable.objects.get(attr1=change_from)
            dt.attr1 = change_to
            dt.save()
            return JsonResponse({'response': 'update_ok'})
        except Exception as e:
            print(e)
            return JsonResponse({'response': 'update_failed'})
    elif request.method == "DELETE":
        try:
            dts = DemoTable.objects.filter(attr1=request.DELETE.get('attr1'))
            return JsonResponse({'response': f'del {len(dts)}'})
        except Exception as e:
            # Exception will occur that DELETE doesnt exist
            print('Exception Occured!', e)
            return JsonResponse({'response': 'delete_failed'})

# By default django only uses POST and GET
# In order to be able to parse parameters from PUT and DELETE as well
# we need to use some other resource in django
# we will use django-rest-framework for this purpose