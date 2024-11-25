from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('leave_application/',leaveApplication,name='leave_application'),
    path('leave_history/',leaveHistory,name='leave_history'),
    path('report_generator',reportGenerator,name='report_generator'),
    path('requests_received',requestsReceived,name='requests_received'),
    path('approve/',approve,name='approve'),
    path('reject/',reject,name='reject'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
