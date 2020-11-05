from django.contrib import admin

from ..admin_site import flourish_caregiver_admin
from ..forms import EnrollmentForm
from ..models import Enrollment
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Enrollment, site=flourish_caregiver_admin)
class EnrollmentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = EnrollmentForm
    search_fields = ['subject_identifier']

    fields = ('enrollment_identifier',
              'report_datetime',
              'have_child',
              'child_age')
    
    radio_fields = {'have_child': admin.VERTICAL,
                    'child_age': admin.VERTICAL,}
                    
    
    list_display = ('subject_identifier', 'have_child', 'child_age')
