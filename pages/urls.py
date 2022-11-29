from django.urls import path
from .views import blog, blogdetail, contact, index,blog,blog_create,blog_update

urlpatterns = [
    path("", index, name="index"),
    path("blogs/", blog, name="blogs"),
    path("blogdetail/<int:id>",blogdetail,name='blogdetail'),
    path("contact/",contact,name='contact'),
    # ath("update/",blogupdate,name='update'),p
    path("create/",blog_create,name="create"),
    path('blog_update/<int:id>', blog_update, name="blog_update"),
]
