import re
from django.shortcuts import render
from django.http import JsonResponse


def getRoute(request):

    routes=[
        {
            'Endpoint':'/notes/',
            'methods':'GET',
            'body':'None',
            'description':'Return an array of notes',
        },
         {
            'Endpoint':'/notes/id',
            'methods':'GET',
            'body':'None',
            'description':'Return an single not object',
        },
         {
            'Endpoint':'/notes/create/',
            'methods':'POST',
            'body':{'body':''},
            'description':'Create new notes',
        },
         {
            'Endpoint':'/notes/id/update',
            'methods':'PUT',
            'body':{'body':''},
            'description':'Updating a note',
        },
         {
            'Endpoint':'/notes/id/delete',
            'methods':'GET',
            'body':'None',
            'description':'Delete an exixting note',
        },
    ]

    return JsonResponse(routes,safe=False)

# Create your views here.
