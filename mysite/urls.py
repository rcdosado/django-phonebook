from django.conf.urls import include, url
from django.contrib import admin
from phonebook import views

urlpatterns = [

    #Admin
    url(r'^admin/', include(admin.site.urls),name='adminpage'),

    #custom
    url(r'^$', views.ListContactView.as_view(), name='contacts-list', ),
    url(r'^new$', views.create_contact, name='contacts-new', ),
    url(r'^contact/(?P<pk>[-\w]+)/$',  views.ContactDetail.as_view(), name='contact-details',),

]
