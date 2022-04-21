from user_account.models import *
from user_account.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.db.models import Q

INVALID_DATA = status.HTTP_400_BAD_REQUEST
CREATED = status.HTTP_201_CREATED
SUCCEEDED_REQUEST = status.HTTP_200_OK


@api_view(['POST'])
def following(request):
    if request.method == 'POST':
        data = request.data
        favoriteObj = favoriteSerializer(data=data)

        if favoriteObj.is_valid():
            favoriteObj.save()
            return Response("Done", status=CREATED)
        else:
            return Response(favoriteObj.errors, status=INVALID_DATA)


@api_view(['POST'])
def comment(request):
    if request.method == 'POST':
        data = request.data
        commentObj = commentSerializer(data=data)

        if commentObj.is_valid():
            commentObj.save()
            return Response("Done", status=CREATED)
        else:
            return Response(commentObj.errors, status=INVALID_DATA)


@api_view(['GET'])
def search(request, keyword):
    if request.method == "GET":

        if keyword.isdigit():
            try:
                output = doctor.objects.get(dNumber=int(keyword))
                _output = doctorSerializer(output)
                return Response(_output.data, status=SUCCEEDED_REQUEST)
            except ObjectDoesNotExist:
                return Response("Not Found", status=SUCCEEDED_REQUEST)

        else:
            output = doctor.objects.filter(name__contains=keyword).all()
            _output = doctorSerializer(output, many=True)
            if not _output.data:
                return Response("Not Found", status=SUCCEEDED_REQUEST)
            return Response(_output.data, status=SUCCEEDED_REQUEST)


@api_view(['POST'])
def set_appointment(request):
    if request.method == 'POST':
        appointmentData = request.data
        day = datetime.strptime(appointmentData['date'], "%Y-%m-%d").date().strftime("%A")

        if working_time.objects.filter(doctor_id=appointmentData['doctor_id'],
                                       day=day,
                                       start_time__contains=appointmentData["time"]).exists():

            if not appointment.objects.filter(doctor_id=appointmentData['doctor_id'],
                                              date__contains=appointmentData['date'],
                                              time__contains=appointmentData["time"]).exists():

                appointmentObj = appointmentSerializer(data=appointmentData)

                if appointmentObj.is_valid():
                    appointmentObj.save()
                    return Response("Reserved successfully", status=CREATED)
                else:
                    return Response(appointmentObj.errors, status=INVALID_DATA)
            else:
                return Response("This time was reserved", status=INVALID_DATA)
        else:
            return Response("This time is not correct", status=INVALID_DATA)


@api_view(['GET'])
def show_times(request, date, doctorID):
    if request.method == 'GET':
        day = datetime.strptime(date, "%Y-%m-%d").date().strftime("%A")
        doctor_times = working_time.objects.filter(day=day, doctor_id=doctorID).all()
        appointment_times = appointment.objects.filter(date=date, doctor_id=doctorID).all()
        suggestion_times = []
        flag = 0
        for dt in doctor_times:
            dtime = dt.start_time
            for at in appointment_times:
                atime = at.time
                if dtime == atime:
                    flag = 1
                    break
            if flag != 1:
                suggestion_times.append(dt)
            else:
                flag = 0
        _suggestion_times = workingTimeSerializer(suggestion_times, many=True)
        if _suggestion_times is None:
            return Response("There is no time.", status=SUCCEEDED_REQUEST)
        return Response(_suggestion_times.data, status=SUCCEEDED_REQUEST)


@api_view(['POST'])
def register_userinfo(request):
    if request.method == 'POST':
        data = request.data
        infoObj = normalUserSerializer(data=data)

        if infoObj.is_valid():
            infoObj.save()
            return Response("Done", status=CREATED)
        else:
            return Response(infoObj.errors, status=INVALID_DATA)


@api_view(['PATCH'])
def edit_userinfo(request, user_id):
    if request.method == 'PATCH':
        try:
            found = normal_user.objects.get(user_id=user_id)
        except found.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        infoObj = normalUserSerializer(found, data=data, partial=True)

        if infoObj.is_valid():
            infoObj.save()
            return Response("Updated successfully", status=SUCCEEDED_REQUEST)
        else:
            return Response(infoObj.errors, status=INVALID_DATA)


@api_view(['GET'])
def filter(request, city='', education='', field=''):
    city = request.GET.get('city')
    education = request.GET.get('education')
    field = request.GET.get('field')
    if request.method == "GET":
        try:
            output = doctor.objects.all()
            _output = doctorSerializer(output, many=True)
            if city:
                output = output.filter(address__contains=city).all()
                _output = doctorSerializer(output, many=True)
            if education:
                output = output.filter(education=education).all()
                _output = doctorSerializer(output, many=True)
            if field:
                output = output.filter(field=field).all()
                _output = doctorSerializer(output, many=True)
            return Response(_output.data, status=SUCCEEDED_REQUEST)
        except ObjectDoesNotExist:
            return Response("Not Found", status=SUCCEEDED_REQUEST)


@api_view(['GET'])
def doctorinfo(request, doctorid):
    if request.method == "GET":
        try:
            output1 = doctor.objects.get(id=doctorid)
            _output1 = doctorSerializer(output1)
            output2 = working_time.objects.filter(doctor_id=doctorid).all()
            _output2 = workingTimeSerializer(output2, many=True)
            output = {'info': _output1.data, 'working_times': _output2.data}
            return Response(output, status=SUCCEEDED_REQUEST)
        except ObjectDoesNotExist:
            return Response("Not Found", status=SUCCEEDED_REQUEST)