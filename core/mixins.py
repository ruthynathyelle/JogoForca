from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProfessorContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['is_professor'] = user.is_authenticated and user.groups.filter(name='professores').exists()
        return context