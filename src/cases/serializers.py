from rest_framework import serializers

from .models import Case, CasePerson


class CasePersonSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField()

    class Meta:
        model = CasePerson
        fields = ["id", "person", "role"]


class CaseSerializer(serializers.ModelSerializer):
    parties = CasePersonSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = ["id", "number", "title", "status", "filed_on", "parties"]
