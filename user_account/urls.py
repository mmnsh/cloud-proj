from django.urls import path
from django.conf.urls import url
from user_account import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API List",
        default_version='v1',
        description="List of APIs",
        terms_of_service="#",
        contact=openapi.Contact(email="#"),
        license=openapi.License(name=""),
    ),
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


app_name = 'user_account'

urlpatterns = [
    path('follow/', views.following),
    path('comment/', views.comment),
    path('search/keyword=<str:keyword>/', views.search),
    path('setAppointment/', views.set_appointment),
    path('showTimes/date=<str:date>/id=<int:doctorID>/', views.show_times),
    path('registerinfo/', views.register_userinfo),
    path('editinfo/user_id=<str:user_id>', views.edit_userinfo),
    path('doctorinfo/doctorid=<str:doctorid>/', views.doctorinfo),
    url(r'^getlist(?:/city=(?P<city>[a-zA-Z]+))?(?:/education=(?P<education>[a-zA-Z]+))?(?:/field=(?P<field>[a-zA-Z]+))?/$',views.filter),
    path('', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]