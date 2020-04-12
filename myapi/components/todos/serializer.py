from .serializer_unrelated import TodoSerializerUnrelated
from ..tasks.serializer_unrelated import TaskSerializerUnrelated

class TodoSerializer(TodoSerializerUnrelated):
    included_serializers = {
        'tasks': TaskSerializerUnrelated,
    }

    class Meta(TodoSerializerUnrelated.Meta):
        fields = [*TodoSerializerUnrelated.Meta.fields, 'tasks']

    class JSONAPIMeta:
        select_related = ['tasks']

