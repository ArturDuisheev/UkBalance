from rest_framework import serializers

from form import models


class DropDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DropDownSide
        fields = (
            'id',
            'not_required_sum_investments',
            'not_required_term'
        )


class FormSerializer(serializers.ModelSerializer):
    drop_down_info = DropDownSerializer(many=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = models.Form
        fields = (
            'id',
            'name',
            'surname',
            'email',
            'code_country',
            'phone_number',
            'drop_down_info',
            'created_at'
        )

    def create(self, validated_data):
        many_drop_down_inf = validated_data.pop('drop_down_info', [])
        form = models.Form.objects.create(**validated_data)
        for drop_down in many_drop_down_inf:
            drop_down_inf = models.DropDownSide.objects.get_or_create(**drop_down)
            form.drop_down_info.add(drop_down_inf[0])

        return form
