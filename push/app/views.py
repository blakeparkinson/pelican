from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from push.app.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apns2.client import APNsClient
from apns2.payload import Payload


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view()
def push(request):
    #fcm_device = GCMDevice.objects.create(registration_id="e--N1a4DuTg:APA91bGrwQnf8h5o3UHrVPx3PTkTVumOEfHP5dfAdvFDuBA2h6QZVG0MYuQtGRH21nvdnb44sThudENkAeEtrmBND3g1gv2A0IlLW4ZMsCGl_AsBDWCR4FJm6s57pf-PPz5BGTkIWCbw", cloud_message_type="FCM", user='bill')
    #device = GCMDevice.objects.get(registration_id="e--N1a4DuTg:APA91bGrwQnf8h5o3UHrVPx3PTkTVumOEfHP5dfAdvFDuBA2h6QZVG0MYuQtGRH21nvdnb44sThudENkAeEtrmBND3g1gv2A0IlLW4ZMsCGl_AsBDWCR4FJm6s57pf-PPz5BGTkIWCbw")

    token_hex = '106ececed6c5985efb2afd75618a41120086e7e93488315dc03ccd9eff0be257'
    payload = Payload(alert="Hello World!", sound="default", badge=1)
    topic = 'com.example.App'
    client = APNsClient('https://s3-us-west-1.amazonaws.com/blake-deets/aps_development.cer', use_sandbox=False, use_alternative_port=False)
    client.send_notification(token_hex, payload, topic)
