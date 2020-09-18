from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('view-pdf/',views.view_pdf,name='view'),
   path('download-pdf/',views.download_pdf,name='download')
]
