from django.urls import path, include

urlpatterns = [
    path('api/', include('library_app.urls')),
]
