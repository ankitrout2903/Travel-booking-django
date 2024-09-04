from django.contrib import admin
from .models import *

class PackageEventInline(admin.TabularInline):
    model           = PackageEvent
    list_display    = ['title','description','created_date','updated_date']
    list_editable   = ("__all__")
    extra           = 1 

class PackageGalleryInline(admin.TabularInline):
    model           = PackageGallery
    list_display    = ['title','image','created_date','updated_date']
    list_editable   = ("__all__")
    extra           = 1 

class PackageAdmin(admin.ModelAdmin):
    list_display    = ['title','days','nights','available','updated_at']
    list_filter     = ['available','updated_at']
    search_fields   = ['title','departure','days','nights']
    list_per_page   = 20
    inlines         = [PackageEventInline,PackageGalleryInline]

class BlogEventInline(admin.TabularInline):
    model           = BlogEvent
    list_display    = ['title','description','created_date','updated_date']
    list_editable   = ("__all__")
    extra           = 1 

class BlogGalleryInline(admin.TabularInline):
    model           = BlogGallery
    list_display    = ['title','image','created_date','updated_date']
    list_editable   = ("__all__")
    extra           = 1 

class BlogAdmin(admin.ModelAdmin):
    list_display    = ['title','updated_at']
    list_filter     = ['updated_at']
    search_fields   = ['title']
    list_per_page   = 20
    inlines         = [BlogEventInline,BlogGalleryInline]

class ReviewGalleryInline(admin.TabularInline):
    model           = ReviewGallery
    list_display    = ['image','review','updated_date']
    extra           = 1 

class ReviewAdmin(admin.ModelAdmin):
    list_display    = ['package','user','facilities','comfort','experience','location','updated_date']
    list_filter     = ['package','updated_date']
    search_fields   = ['user','facilities','comfort','experience','location']
    list_per_page   = 20
    inlines         = [ReviewGalleryInline]


admin.site.register(UserProfile)
admin.site.register(Package,PackageAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(PackageEvent)
admin.site.register(PackageGallery)
admin.site.register(Gallery)
admin.site.register(Review,ReviewAdmin)
# admin.site.register(ReviewGallery)
admin.site.register(Driver)
admin.site.register(VehicleGallery)
admin.site.register(Order)
admin.site.register(Feedback)
admin.site.register(BookDriver)
admin.site.register(CarCharge)
admin.site.register(Contact)
