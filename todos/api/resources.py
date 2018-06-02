from tastypie.resources import ModelResource
from todos.models import todo

class getTodoResource(ModelResource):
    class Meta:
        queryset = todo.objects.all()
        resource_name = 'Todo'