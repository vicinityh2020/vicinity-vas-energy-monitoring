import json

import pendulum
from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from application.models import SensorUsage, Settings
from django.views.decorators.csrf import csrf_exempt
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import UserSerializer, LoginUserSerializer


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid()
        if is_valid:
            user = serializer.validated_data
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)
            })
        else:
            return Response({
                "error": "Wrong username or password"
            })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def water_threshold(request):
    response_obj = {
        'value': None
    }

    setting_name = 'WaterThreshold'

    threshold = Settings.get_threshold_value(setting_name=setting_name)
    response_obj['value'] = threshold.value

    return JsonResponse(status=200, data=response_obj)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def power_threshold(request):
    response_obj = {
        'value': None
    }

    setting_name = 'PowerThreshold'

    threshold = Settings.get_threshold_value(setting_name=setting_name)
    response_obj['value'] = threshold.value

    return JsonResponse(status=200, data=response_obj)


@csrf_exempt
def water_usage(request, **kwargs):
    response_obj = {
        "units": "l",
        "data": [],
        "labels": []
    }
    period = kwargs['period']

    dt = pendulum.from_timestamp(kwargs['timestamp'])

    if period == 'day':
        objects = SensorUsage.get_usage_by_day(dt, "W")
        for obj in objects:
            response_obj["data"].append(obj.value)
            response_obj["labels"].append(f"{obj.datetime.hour}:{obj.datetime.minute}")

        return JsonResponse(response_obj)
    elif period == "month":
        observations = SensorUsage.get_usage_by_month(dt, "W")
        results = {
            "data": {},
        }
        for observation in observations:
            if observation.datetime.day not in results["labels"]:
                results["labels"][observation.datetime.day] = observation.value
            else:
                results["labels"][observation.datetime.day] += observation.value
    else:
        return JsonResponse({
            "error": "unknown period given, only day or month is supported"
        })

    return JsonResponse({
        "Success": False,
        "Error": "Unknown error"
    })

@csrf_exempt
def energy_usage(request, **kwargs):
    response_obj = {
        "units": "l",
        "data": [],
        "labels": []
    }
    period = kwargs['period']

    dt = pendulum.from_timestamp(kwargs['timestamp'])

    if period == 'day':
        objects = SensorUsage.get_usage_by_day(dt, "P")
        for obj in objects:
            response_obj["data"].append(obj.value)
            response_obj["labels"].append(f"{obj.datetime.hour}:{obj.datetime.minute}")

        return JsonResponse(response_obj)
    elif period == "month":
        observations = SensorUsage.get_usage_by_day(dt, "P")
        results = {
            "data": {},
        }
        for observation in observations:
            if observation.datetime.day not in results["labels"]:
                results["labels"][observation.datetime.day] = observation.value
            else:
                results["labels"][observation.datetime.day] += observation.value
    else:
        return JsonResponse({
            "error": "unknown period given, only day or month is supported"
        })

    return JsonResponse({
        "Success": False,
        "Error": "Unknown error"
    })