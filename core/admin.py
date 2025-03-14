from django.contrib import admin
from core.models import *


# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter','text_parameter',]
    list_editable = ['description', 'parameter',]

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting


@admin.register(Skill)
class SkillSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'show_percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage', 'show_percentage']

    class Meta:
        model = Skill


@admin.register(Experience)
class ExperienceSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_title', 'job_location', 'start_date', 'end_date', 'updated_date',
                    'created_date']
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date']

    class Meta:
        model = Experience


@admin.register(Education)
class EducationSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'major', 'department','school_location', 'start_date', 'end_date', 'updated_date',
                    'created_date']
    search_fields = ['school_name', 'major', 'department','school_location',]
    list_editable = ['school_name', 'major', 'department','school_location', 'start_date', 'end_date']

    class Meta:
        model = Education


@admin.register(SocialMedia)
class SocialMediaSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'link', 'icon', 'updated_date', 'created_date']
    search_fields = ['name', 'link', 'icon']
    list_editable = ['order', 'name', 'link', 'icon']

    class Meta:
        model = SocialMedia

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'description', 'image', 'link', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'url']
    list_editable = ['order', 'name', 'description', 'image', 'link']

    class Meta:
        model = Project

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'description', 'star', 'link', 'updated_date', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['order', 'name', 'description', 'star', 'link']

    class Meta:
        model = Testimonial

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file', 'updated_date', 'created_date']
    search_fields = ['slug', 'button_text', ]
    list_editable = ['order', 'slug', 'button_text', 'file']

    class Meta:
        model = Document