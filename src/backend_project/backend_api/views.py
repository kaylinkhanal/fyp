from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import (
                       User,
                       Student,
                       Faculty,
                       Subject,
                       SelectedSubject,
                       AttendanceRecord,
                       Notice,
                       StudentOfTheYear,
                       FacultyOfTheYear,
                       Assignment,
                       GradedAssignment
)
from .serializers import (
                          UserSerializer,
                          StudentSerializer,
                          FacultySerializer,
                          SubjectSerializer,
                          SelectedSubjectSerializer,
                          AttendanceRecordSerializer,
                          NoticeSerializer,
                          StudentOfTheYearSerializer,
                          FacultyOfTheYearSerializer,
                          AssignmentSerializer,
                          GradedAssignmentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'user'

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})


class StudentOfTheYearViewSet(viewsets.ModelViewSet):
    serializer_class = StudentOfTheYearSerializer
    queryset = StudentOfTheYear.objects.all()
    lookup_field = 'username'

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})


class FacultyOfTheYearViewSet(viewsets.ModelViewSet):
    serializer_class = FacultyOfTheYearSerializer
    queryset = FacultyOfTheYear.objects.all()
    lookup_field = 'student'

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})




class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    lookup_field = 'id'

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})






class FacultyViewSet(viewsets.ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()
    lookup_field = 'user'
    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})



class SelectedSubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SelectedSubjectSerializer
    queryset = SelectedSubject.objects.all()

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})



class AttendanceRecordViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceRecordSerializer
    queryset = AttendanceRecord.objects.all()

    def put(self, request, pk=None):
        """Handles updating the object"""
        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request, pk=None):
        """Deletes the object."""
        return Response({'method':'delete'})



class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class GradedAssignmentListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        queryset = GradedAssignment.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(student__username=username)
        return queryset


class GradedAssignmentCreateView(CreateAPIView):
    serializer_class = GradedAssignmentSerializer
    queryset = GradedAssignment.objects.all()

    def post(self, request):
        print(request.data)
        serializer = GradedAssignmentSerializer(data=request.data)
        serializer.is_valid()
        graded_assignment = serializer.create(request)
        if graded_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
