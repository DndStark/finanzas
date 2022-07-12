from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("static/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def index(request):
    resgistration  = ['drdl4JErS7uIJkyVEN0Lmh:APA91bHnIDGlzi1WSW4lQzJB_iNo0wIbzNkOsE8QbrBuCsrzxat7OsdRe29tNTj5sQdlb0kywMQv-K-AZUD5hUgin3zBfUU2IRlYbYL-Ut05HgDHMYroz3_ua_-V3tH2XV6b_rhMesK6']
    #message = send_notification(resgistration , 'Test tittle' , 'Hola, solo estamos haciendo pruebas de notificación',)
    return render(request, 'index.html', {'message' : "Sending Message"})

def send_notification(registration_tokens , message_title , message_body, dataObject = None):
    message = messaging.MulticastMessage(
        notification = messaging.Notification(
            title = message_title,
            body = message_body
        ),
        data = dataObject,
        tokens = registration_tokens        
    )
    
    response = messaging.send_multicast(message)

    return "Successfully sent message " + str(response)


def send(request):
    resgistration  = ['drdl4JErS7uIJkyVEN0Lmh:APA91bHnIDGlzi1WSW4lQzJB_iNo0wIbzNkOsE8QbrBuCsrzxat7OsdRe29tNTj5sQdlb0kywMQv-K-AZUD5hUgin3zBfUU2IRlYbYL-Ut05HgDHMYroz3_ua_-V3tH2XV6b_rhMesK6']
    send_notification(resgistration, request.GET["messaget"], request.GET["messageb"],)
    return HttpResponse("index.html")
