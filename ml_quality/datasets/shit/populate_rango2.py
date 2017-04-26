import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('Python', 128, 64)

    add_page(c_id=3,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/",
             views=800)

    add_page(c_id=3,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/",
             views=700)

    add_page(c_id=3,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/",
             views=600)

    django_cat = add_cat("Django", 64, 32)

    add_page(c_id=4,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
             views=1000)

    add_page(c_id=4,
             title="Django Rocks",
             url="http://www.djangorocks.com/",
             views=500)

    add_page(c_id=4,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/",
             views=900)

    frame_cat = add_cat("Other Frameworks", 32, 16)

    add_page(c_id=5,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/",
             views=400)

    add_page(c_id=5,
             title="Flask",
             url="http://flask.pocoo.org",
             views=300)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(c_id=c.c_id):
            print "- {0} - {1}".format(str(c), str(p))


def add_page(c_id, title, url, views=0):
    p = Page.objects.get_or_create(c_id=c_id, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
