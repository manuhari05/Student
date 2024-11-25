# these are django imports
from django.urls import path

# these are local imports
from .views import StudentView , TopperView , HaveCut_off ,PassOrNot, HaveAvg ,TeacherPerformance ,TeacherView

'''
This is the url patterns for the MyApp app
'''
urlpatterns = [
    path('',StudentView.as_view(),name='student_view'),
    path('<int:rollno>',StudentView.as_view(), name='student_view'),
    path('top/', TopperView.as_view(), name='topper_view'),
    path('have/<str:cutoff>/', HaveCut_off.as_view(), name='have_cut_off'),
    path('have/<str:nocutoff>/', HaveCut_off.as_view(), name='have_cut_off'),
    path('pass/<str:spass>/', PassOrNot.as_view(), name='pass_or_not'),
    path('pass/<str:spass>/<int:rollno>/', PassOrNot.as_view(), name='pass_or_not'),
    path('avg/<str:avg>/',HaveAvg.as_view(), name='have_avg'),
    path('avg/<str:avg>/<int:rollno>/', HaveAvg.as_view(), name='have_avg'),
    path('teacherperformance/', TeacherPerformance.as_view(), name='teacher_performance'),
    path('teacher',TeacherView.as_view(),name='teacher_view'),
    path('teacher/<int:empid>', TeacherView.as_view(), name='teacher_view'),
    

]   