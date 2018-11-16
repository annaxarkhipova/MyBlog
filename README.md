# ![MyBlog](http://annasblog.pythonanywhere.com/blog/) &middot; [![Python 3.7](https://www.python.org/)],[![Django2.0](https://www.djangoproject.com/)]

This project is a mix of aiming to level-up my knowledges about python abilities with a craving to make something bigger than I tried before

I will desribe the essentuals that I discovered for myself.

The instruments I used are Django 2.0 & Python 3.7(pls, pay attention - with the other versions settings can be different), Disqus,  and some airing of my CSS knoweledges.

## Installing
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

*mysite/urls.py*

That was a special point for me. Because of the conflict between versions of Dj & Py I scraped about a deep big problem following the instruction template and solve the bag:
"django.core.exceptions.ImproperlyConfigured: Passing a 3-tuple to include() is not supported. Pass a 2-tuple containing the list of patterns and app_name, and provide the namespace argument to include() instead."

The thing is, to set the url.py definetly in this way:
```
urlpatterns = [
    url(r'^admin/', admin.site.urls),
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
python manage.py makemigrations  
python manage.py migrate         
python manage.py createsuperuser
python manage.py runserver
```
If you're alright - congratulations - http://localhost:8000/admin/ 
Make some posts:
![MyBlog](https://github.com/annaxarkhipova/MyBlog/blob/master/mysite/Screenshot%202018-11-06%20at%2018.24.02.png)

## Step 2

Use Django documentation:
*blog/views.py*
```from blog.models import Post 
from django.views.generic import ListView, DetailView/Users/ana/MyBlog/README.md

class PostsListView(ListView):    #make post presented in the list
    model = Post                   #the model to present 

class PostDetailView(DetailView):  #our model detailed
    model = Post
```
 *mysite/urls.py*
 Add this line in urlpatterns:
 ```
url(r'^admin/', admin.site.urls),
 ```
 URLs  will process from /blog/, 
 So, create a new *urls.py* in the catalog /blog/ with:
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
 
 By default PostListView Django will make a search in blog/templates/blog/post_list.html So, I created that file just like a post_detail.html  later.
 
 ## Step 3
 
 Installing django disqus  there was no need for me after log in to point DISQUS_API_KEY and DISQUS_WEBSITE_SHORTNAME in the *settings.py*.
 
 ## Step 4
 
 *pythonanywhere.com*
 
1. Clone your rep in Console
2. Browse to your folder ```/home/user-name```
and then create ```myvenv``` defining the python version you use:
```
$ virtualenv --python=python3.7 myvenv

$ source myvenv/bin/activate

(myvenv) $  pip install django django-disqus
```
3. Creating a new Web App, choose Manual Configuration because in this way you can select the Python version
4. In the special selection enter   ```myvenv```  that will lead to your virtual env
5. Editing WSGI watch the path that should lead to your *settings.py*:

```path = os.path.expanduser('~/MyBlog/mysite/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
```
Additionally, I made changes there just align with the original file on my PC:
```DEBUG = False

ALLOWED_HOSTS = [
'annasblog.pythonanywhere.com'
]```
