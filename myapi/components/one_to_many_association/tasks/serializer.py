from .serializer_unrelated import TaskSerializerUnrelated
from ..todos.serializer_unrelated import TodoSerializerUnrelated


class TaskSerializer(TaskSerializerUnrelated):
    included_serializers = {
        'todo': TodoSerializerUnrelated
    }

    class Meta(TaskSerializerUnrelated.Meta):
        fields = [*TaskSerializerUnrelated.Meta.fields, 'todo']

    class JSONAPIMeta:
        select_related = ['todo']
