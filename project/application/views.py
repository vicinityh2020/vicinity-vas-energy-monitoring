import pendulum
from django.http import JsonResponse

# Create your views here.
from application.models import SensorUsage


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