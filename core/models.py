from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from portfolio_cemre.custom_storage import ImageSettingStorage, DocumentStorage, MediaStorage


# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )
    text_parameter = models.TextField(
        default='',
        blank=True,
        verbose_name='Text Parameter',
        help_text='',
    )

    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        storage=ImageSettingStorage(),
    )

    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    show_percentage = models.BooleanField(
        default=True,
        verbose_name='Show Percentage',
    )

    def __str__(self):
        return f"Skill: {self.name}"

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Company Name',
        help_text='',
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Title',
        help_text='',
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Job Location',
        help_text='',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f"Experience: {self.company_name}"

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('start_date',)


class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Name',
        help_text='',
    )
    major = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Major',
        help_text='',
    )
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Department',
        help_text='',
    )
    school_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='School Location',
        help_text='',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f"Education: {self.school_name}"

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('start_date',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
        help_text='',

    )
    icon = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Icon',
        help_text='',
    )

    def __str__(self):
        return f"Social Media: {self.name}"

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'
        ordering = ('order',)


class Project(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    image = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        storage=ImageSettingStorage(),
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Link',
        help_text='',
    )

    def __str__(self):
        return f"Project: {self.name}"

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('order',)

class Testimonial(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name='Description',
        help_text='',
    )

    star = models.IntegerField(
        default=5,
        verbose_name='Star',
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
    )

    def __str__(self):
        return f"Testimonial: {self.name}"

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ('order',)




class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='',
    )
    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Button Text',
        help_text='',
    )
    file = models.FileField(
        default='',
        verbose_name='File',
        help_text='',
        blank=True,
        storage=DocumentStorage(),
    )

    def __str__(self):
        return f"Document: {self.slug}"

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)
