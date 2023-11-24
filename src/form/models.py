from django.db import models

from django.utils.translation import gettext_lazy as _


class DropDownSide(models.Model):
    not_required_sum_investments = models.CharField(
        _('not required sum investments'),
        max_length=50
    )
    not_required_term = models.CharField(
        _('not required term'),
        max_length=40
    )


class Form(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=70,
    )
    surname = models.CharField(
        _('Surname'),
        max_length=70,
    )
    email = models.EmailField(
        _('Email')
    )
    code_country = models.CharField(
        _('Code country'),
        max_length=5,
    )
    phone_number = models.CharField(
        _('number'),
        max_length=20,
    )
    drop_down_info = models.ManyToManyField(DropDownSide, verbose_name='drop down data')
    created_at = models.DateTimeField(
        _('Created at application: '),
        auto_now_add=True
    )



    def __str__(self) -> str:
        return f'form: {self.name}.{self.surname[0]}, phone: {self.code_country}{self.phone_number}'

    class Meta:
        verbose_name = _('Form data')
        verbose_name_plural = _('Forms data')


