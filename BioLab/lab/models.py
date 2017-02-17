from django.db import models

# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField()
    affiliation = models.CharField()
    status = models.CharField()
    office = models.CharField(blank=True)
    interest = models.TextField()
    intro_msg = models.TextField(verbose_name="Introduction Message")
    education = models.TextField()
    pub_info = models.ManyToManyField(
        Pub,
        through='Authorship'
    )

class Pub(models.Model):
    JOURNAL = 'JR'
    CONFERENCE = 'CF'
    PUB_TYPE_CHOICES = (
        (JOURNAL, 'Journal'),
        (CONFERENCE, 'conference'),
    )
    pub_type = models.CharField(max_length=2, choices=PUB_TYPE_CHOICES, default=JOURNAL)
    authors = models.ManyToManyField(
        Members,
        through='Authorship'
    )
    year = models.PositiveSmallIntegerField()
    pub_info = models.CharField()
    title = models.CharField()
    abstract = models.TextField(blank=True)
    url = models.URLField()


class Authorship(models.Model):
    pub = models.ForeignKey(Pub, on_delete=models.CASCADE)
    members = models.ForeignKey(Members, on_delete=models.CASCADE)


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField()
    subject = models.CharField(max_length=200)
    CATEGORY1 = "C1"
    CATEGORY2 = "C2"
    CATEGORY_TYPE_CHOICES = (
        (CATEGORY1, 'category1'),
        (CATEGORY2, 'category2'),
    )
    category = models.CharField(max_length=2, choices=CATEGORY_TYPE_CHOICES, default=CATEGORY1)
    msg = models.TextField()