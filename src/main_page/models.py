from django.db import models

from django.utils.translation import gettext_lazy as _


class Card(models.Model):
    logo_company = models.ImageField(
        _('Логотип компании'),
        upload_to='cards/logos/'
    )
    section_text = models.ManyToManyField('SectionInCard', verbose_name=_('секция по тексту '))

    def __str__(self):
        return f'Здесь что то должно быть'


class SectionInCard(models.Model):
    section_text_up = models.TextField(
        _('Text to the left of the logo: '),
    )
    section_text_down = models.TextField(
        _('Text to the below the logo: '),
    )

    def __str__(self) -> str:
        return f'text: {self.section_text_up[:5]}..., text: {self.section_text_down[:5]}...'

    class Meta:
        verbose_name = _('Section in card')
        verbose_name_plural = _('Sections in cards')
