

from django.urls import path
from personal_portfolio import settings
from django.conf.urls.static import static


from . import views
urlpatterns = [
    path('',views.project_index,name='project_index'),
    path('<int:pk>',views.project_detail,name='project_detail')
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 




