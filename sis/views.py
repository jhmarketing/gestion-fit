from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import PlanEntrenamiento

class PlanEntrenamientoDetailView(DetailView):
    model = PlanEntrenamiento
    template_name = 'plan_entrenamiento_detail.html'

    def get_object(self, queryset=None):
        plan_id = self.kwargs.get('plan_id')
        obj = get_object_or_404(PlanEntrenamiento, id=plan_id)
        return obj