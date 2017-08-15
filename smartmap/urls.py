from django.conf.urls import url, include
from django.conf import settings

from . import views

from tastypie.api import Api
from smartmap.api import LocationResource

api_v1 = Api(api_name='v1')
api_v1.register(LocationResource(table_id=settings.FUSION_TABLE_ID))

urlpatterns = [
    url(r'^$', views.smartmap, name='smartmap'),
    url(r'^api/', include(api_v1.urls)),

]
