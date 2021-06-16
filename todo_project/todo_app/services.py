from todo_app.models import Todo


class TodosService:
    def __init__(self, state):
        self.state = state

    def get_by_state(self):
        if self.state == 'N':
            return Todo.objects.filter(is_done=False)
        elif self.state == 'D':
            return Todo.objects.filter(is_done=True)
        else:
            return Todo.objects.all()
