from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import CaregiverClinicalMeasurements


class CaregiverClinicalMeasurementsForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = CaregiverClinicalMeasurements
        fields = '__all__'
