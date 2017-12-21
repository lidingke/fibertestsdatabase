from rest_framework import serializers
from producer.models import Result,ResultColumns

# from producer.models import


class ResultSerializer(serializers.ModelSerializer):


    owner = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = (
            'owner','corediameter', 'claddiameter',
            'coreroundness', 'cladroundness', 'concentricity', 'add_time'
        )


    def get_owner(self,obj):
        name = "%s" % obj.owner
        return name.upper()


class ResultColumnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultColumns
        # fields = ('id', 'owner')
        exclude = ('id',)

