from django.db import models

from edc_constants.choices import YES_NO_NA

from .model_mixins import CrfModelMixin
from .list_models import WcsDxAdult


class MaternalDiagnoses(CrfModelMixin):

    has_who_dx = models.CharField(
        verbose_name=(
            "During this pregnancy, did the mother have any new diagnoses "
            "listed in the WHO Adult/Adolescent HIV clinical staging document "
            "which  is/are NOT reported?"),
        max_length=3,
        choices=YES_NO_NA)

    who = models.ManyToManyField(
        WcsDxAdult,
        verbose_name='List any new WHO Stage III/IV diagnoses '
        'that are not reported in the Question above:'
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'flourish_caregiver'
        verbose_name = "Maternal Diagnosis"
        verbose_name_plural = "Maternal Diagnoses"
