import json
from tastypie.authorization import Authorization
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.resources import ModelResource

from django.http import HttpResponse

from smartmap.managers import GoogleFusionTableManager
from models import Location


class LocationResource(ModelResource):
    def __init__(self, table_id):
        self.table_id = table_id
        super(LocationResource, self).__init__()

    class Meta:
        object_class = Location
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()
        allowed_methods = ['post', 'get', 'delete']
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        if Location.objects.filter(address=bundle.data['address']).exists():
            errors = {'error': 'Marker with this address already exist'}
            raise ImmediateHttpResponse(response=HttpResponse(content=json.dumps(errors), status=409))

        manager = GoogleFusionTableManager(table_id=self.table_id)
        # TODO: handle error from Manager
        manager.create(address=bundle.data['address'])

        return super(LocationResource, self).obj_create(bundle, **kwargs)

    def obj_delete_list(self, bundle, **kwargs):
        manager = GoogleFusionTableManager(table_id=self.table_id)
        # TODO: handle error from Manager
        manager.delete_all()
        return super(LocationResource, self).obj_delete_list(bundle, **kwargs)
