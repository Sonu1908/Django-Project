from django.urls import path
from .views import home,about,delete_professor,update_professor

urlpatterns = [
    path("",home,name="home"),
    path("about",about,name="about"),
    path("delete-professor/<int:id>",delete_professor, name="delete_professor"),
    path("update-professor/<int:id>",update_professor, name="update_professor"),
    
]
