from django.db import models
from django.core.validators import FileExtensionValidator


class material(models.Model):
    """Model representing academic materials."""
    title = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=500, default="", blank=True)
    subject_choices = [
        ("PHY", "Physics"),
        ("MAT", "Maths"),
        ("BEE", "BEE"),
        ("ECO", "Ecology & Environment"),
        ("SOC", "Sociology & Professional Ethics")
    ]
    subject = models.CharField(max_length=40, choices=subject_choices, default="null")
    types_choices = [
        ("SYL", "Syllabus"),
        ("NOT", "Class Notes"),
        ("BKS", "Books"),
        ("PYQ", "Previous Year Questions"),
        ("OTH", "Other")
    ]
    types = models.CharField(max_length=40, choices=types_choices, default="OTH")
    file = models.FileField(upload_to="pdf/", validators=[FileExtensionValidator(['pdf'])], null=True, blank=True)

class notice(models.Model):
    """Model representing notices."""
    title = models.CharField(max_length=80)
    timestamp = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=500, default="", blank=True)
    file = models.FileField(upload_to="pdf/", validators=[FileExtensionValidator(['pdf'])], null=True, blank=True)