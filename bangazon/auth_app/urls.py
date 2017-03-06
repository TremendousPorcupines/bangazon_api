from django.conf.urls import url

urlpatterns = [
    url(r'^login/', views.login_user, namespace='login'),
    url(r'^register/', views.register_user, namespace='register'),
    url(r'logout/', views.logout_user, namespace='logout')
]
