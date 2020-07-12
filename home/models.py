from django.db import models

class Bio(models.Model):
    """
    Model template for Portfolio Bio Information Section
    """
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length = 200)
    short_description = models.CharField(max_length = 200)
    long_description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class WorkAcademics(models.Model):
    """
    Model template for Portfolio Work & Academics Information Section
    """
    template_name = models.CharField(max_length=100)
    undergraduation = models.TextField(max_length=500)
    postgraduation = models.TextField(max_length=500, blank=True)
    workexperience1 = models.TextField(max_length=500)
    workexperience2 = models.TextField(max_length=500, blank=True)
    workexperience3 = models.TextField(max_length=500, blank=True)
    workexperience4 = models.TextField(max_length=500, blank=True)
    workexperience5 = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.template_name

class Accomplishment(models.Model):
    """
    Model template for Portfolio Accomplishments Information Section
    """
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    link = models.URLField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    """
    Model template for Portfolio Projects Information Section
    """
    title = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    link = models.URLField()
    thumbnail = models.ImageField(upload_to='project/thumbnails/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    """
    Model template for Contacts Information Section
    """
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    linkedin = models.URLField()
    resume = models.FileField(upload_to="resume/%Y/%m/%d/")
    skype = models.CharField(max_length=100)
    twitter = models.URLField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    """
    Model template for Portfolio Information Section
    """
    name = models.CharField(max_length=200)
    git = models.URLField()
    hackerrank = models.URLField()
    datacamp = models.URLField()
    medium = models.URLField()
    hackerearth = models.URLField()
    codechef = models.URLField()

    def __str__(self):
        return self.name
