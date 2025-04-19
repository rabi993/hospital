

from django.contrib import admin
from . import models

admin.site.register(models.AvailableTime)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Designation, DesignationAdmin)
admin.site.register(models.Specialization, SpecializationAdmin)

# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ['get_full_name','designation','specialization', 'get_email', 'mobile_no','available_time','fee', 'image']

#     def get_full_name(self, obj):
#         return f"{obj.user.first_name} {obj.user.last_name}"
#     get_full_name.short_description = 'Name'

#     def get_email(self, obj):
#         return obj.user.email
#     get_email.short_description = 'Email'
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'get_designations', 'get_specializations', 'get_email', 'get_mobile_no', 'get_available_times', 'fee', 'image']

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_mobile_no(self, obj):
        return obj.user.username  # Or wherever you're storing the mobile number
    get_mobile_no.short_description = 'Mobile No'

    def get_designations(self, obj):
        return ", ".join([d.name for d in obj.designation.all()])
    get_designations.short_description = 'Designations'

    def get_specializations(self, obj):
        return ", ".join([s.name for s in obj.specialization.all()])
    get_specializations.short_description = 'Specializations'

    def get_available_times(self, obj):
        return ", ".join([t.name for t in obj.available_time.all()])
    get_available_times.short_description = 'Available Times'

admin.site.register(models.Doctor, DoctorAdmin)
