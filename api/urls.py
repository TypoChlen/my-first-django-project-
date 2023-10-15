from django.urls import path, include
from api.models import CategoryResource, CourseResource
from tastypie.api import Api


api = Api(api_name='v1')
courseresource = CourseResource()
categoryresource = CategoryResource()
api.register(courseresource)
api.register(categoryresource)


# Key: Authorization
# Value: ApiKey roma:asdhfsafjsakdf3400945

urlpatterns = [
     path('', include(api.urls), name='index')
]