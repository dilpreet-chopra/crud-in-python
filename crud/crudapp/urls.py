from django.conf.urls import url
from crudapp import crudcontroller

urlpatterns = [
url(r'^sidebar/',crudcontroller.fn_sidebar),
# url(r'^retrieve/',crudcontroller.fn_selectdata),
url(r'^retrieveTable/$',crudcontroller.fn_retrieveTable, name='retrieve'),
url(r'^insert/$',crudcontroller.fn_insert),
url(r'^insertTable/(?P<up_id>[0-9]*)/$',crudcontroller.fn_insertTable, name='insert'),
url(r'^deleteTable/(?P<del_id>[0-9]+)/$',crudcontroller.fn_deleteTable),
]