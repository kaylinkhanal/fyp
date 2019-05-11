from rest_framework.routers import DefaultRouter
from .views import (
                  UserViewSet,
                  StudentViewSet,
                  FacultyViewSet,
                  SubjectViewSet,
                  SelectedSubjectViewSet,
                  AttendanceRecordViewSet,
                  NoticeViewSet,
                  FacultyOfTheYearViewSet,
                  StudentOfTheYearViewSet
  )


router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'student', StudentViewSet, base_name='student')
router.register(r'faculty', FacultyViewSet, base_name='faculty')
router.register(r'subject', SubjectViewSet, base_name='subject')
router.register(r'foty', FacultyOfTheYearViewSet, base_name='facultyftheyear')
router.register(r'soty', StudentOfTheYearViewSet, base_name='studentoftheyear')
router.register(r'notice', NoticeViewSet, base_name='notice')
router.register(r'selectedsubject', SelectedSubjectViewSet, base_name='selectedsubject')
router.register(r'attendancerecord', AttendanceRecordViewSet, base_name='attendancerecord')
urlpatterns = router.urls
