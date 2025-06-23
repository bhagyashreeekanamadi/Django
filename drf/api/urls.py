from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('students/',views.studentsView),
    path('student/<int:pk>/',views.studentDetailView),

    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
        path('comments/<int:pk>/',views.CommentDetailView.as_view()),

]