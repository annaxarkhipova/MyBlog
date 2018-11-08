# MyBlog
This project is a mix of aiming to level-up my knowledges about python abilities with a craving to make something bigger than I tried before

The instruments I used are Django 2.0 & Python 3.7(pls, pay attention; all the commands used regarding these versions), Disqus, Bootstrap and some airing of my HTML knoweledges.

## Settings
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
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
```
    
*mysite/admin.py*

Register the blog here.
```
from blog.models import Post # наша модель из blog/models.py
admin.site.register(Post)
```
_____
To sum it up:

```
python manage.py makemigrations # make the site work properly
python manage.py migrate # point at the changes we put
python manage.py createsuperuser # signing up
python manage.py runserver

```
If you're alright - congratulations - http://localhost:8000/admin/ :
![MyBlog](https://github.com/annaxarkhipova/MyBlog/blob/master/mysite/Screenshot%202018-11-06%20at%2018.24.02.png)

## Step 2

      
