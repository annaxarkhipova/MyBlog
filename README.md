# MyBlog
This project is a mix of aiming to level-up my knowledges about python abilities with a craving to make something bigger than I tried before

The instruments I used are Django 2.0 & Python 3.7(pls, pay attention - with the other versions settings can be different), Disqus, Bootstrap and some airing of my HTML knoweledges.

## Installings
The first step to me is to activate the virtualenv in the terminal:
```
source env/bin/activate
```
and to install framework Django for helpin to create othe skeleton of our blog (do not forget to check if your Python & Django versions are matched):
```
pip install django
```

We will start a new project naming it as'mysite' and create a directory with the name 'blog':
```
django-admin.py startproject mysite
python manage.py startapp blog
```

## Step 1
*mysite/settings.py*

Edit TIME_ZONE and LANGUAGE_CODE (I did not change that lines).
Add a line 'blog,' into a tuple INSTALLED_APPS for Django to recognize.

*mysite/urls.py*

That was a special point for me. Because of the conflict between versions of Dj & Py I scraped about a deep big problem following the instruction template and solve the bag:
"django.core.exceptions.ImproperlyConfigured: Passing a 3-tuple to include() is not supported. Pass a 2-tuple containing the list of patterns and app_name, and provide the namespace argument to include() instead."

The thing is, to set the url.py like this:
```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
```
*my/site/models.py*

Read clearly the Dj documentation that is not coprehensive and build the module:

```
class Post(models.Model):
    title = models.CharField(max_length=255)       #post title
    datetime = models.DateTimeField(u'Дата публикации')  #post date
    content = models.TextField(max_length=10000)           #post text

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
```
    
*mysite/admin.py*

Register the blog here.
```
from blog.models import Post  #read our blog/models.py
admin.site.register(Post)
```
_____
To sum it up:
```
python manage.py makemigrations  #make the site work properly
python manage.py migrate         #point at the changes we put
python manage.py createsuperuser #signing up
python manage.py runserver
```
If you're alright - congratulations - http://localhost:8000/admin/ 
Make some posts:
![MyBlog](https://github.com/annaxarkhipova/MyBlog/blob/master/mysite/Screenshot%202018-11-06%20at%2018.24.02.png)

## Step 2

Use Django documentation here:
*blog/views.py*
```from blog.models import Post 
from django.views.generic import ListView, DetailView

class PostsListView(ListView):    #make post presented in the list
    model = Post                   #the model to present 

class PostDetailView(DetailView):  #our model detailed
    model = Post
```
 *mysite/urls.py*
 Add the line in urlpatterns:
 ```
url(r'^admin/', admin.site.urls),
 ```
 URLs in the /blog/ will process from /blog/, 
 create a new *urls.py* in the catalog /blog/ with:
```
#coding: utf-8
from django.conf.urls import patterns, url

from blog.views import PostsListView, PostDetailView 

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'), #URL http://name/blog/ 
                                               #we will see the list of the posts
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), #а по URL http://name/blog/number/ 
                                              #the posts with the defenite number

)
```
 
