import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/'}
    ]
    
    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/'}
    ]
    
    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org'}
    ]
    
    cats = {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
    }

    
    for cat_name, cat_data in cats.items():
        category = add_category(cat_name, cat_data["views"], cat_data["likes"])
        for page in cat_data['pages']:
            add_page(category, page['title'], page['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c.name}: {p.title}')

def add_page(category, title, url, views=0):
    page, created = Page.objects.get_or_create(
        category=category, title=title, defaults={'url': url, 'views': views}
    )
    return page

def add_category(name, views=0, likes=0):
    category, created = Category.objects.get_or_create(
        name=name, defaults={'views': views, 'likes': likes}
    )
    return category


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    print('Database populated successfully!')
