from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Client

def new_client_signup(request, client_name):
    return HttpResponse("Thank you for partnering with us, %s." % client_name)

@csrf_exempt
def client(request, client_name):
    if request.method == 'POST':
#        client = request.POST['client']
#        try:
#            client_exists = Client.objects.get(client_name=client)
#            return HttpResponse(status=409, content="Client %s already exists.")
#        except:
        name = request.POST.get('client')
        address = request.POST.get('address')
        num = request.POST.get('phone')
        c = Client(client_name = client, client_address = address, client_phone = phone)
        c.save()
        new_client_id = c.id
        response = HttpResponse(status=201)
        response['Location'] = '/client/%d' % new_client_id
        return response
    elif request.method == 'GET':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
