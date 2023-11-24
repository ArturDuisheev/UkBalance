from rest_framework import serializers

from main_page import models as mod_main_page


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod_main_page.SectionInCard
        fields = ('id', 'section_text_up', 'section_text_down')


class CardSerializer(serializers.ModelSerializer):
    section_text = SectionSerializer(many=True)

    class Meta:
        model = mod_main_page.Card
        fields = ('id', 'logo_company', 'title_company', 'section_text')

    def create(self, validated_data):
        section_many = validated_data.pop('section_text', [])
        card = mod_main_page.Card.objects.create(**validated_data)
        for section_i in section_many:
            section = mod_main_page.SectionInCard.objects.get_or_create(**section_i)
            card.section_text.add(section)

        return card
