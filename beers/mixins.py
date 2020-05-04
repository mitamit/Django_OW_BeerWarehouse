

#mixins son pequeñas clases de las que pueden heredar cualquier funcion o clase y son para añadir contenido extra al contexto

class AddMyBirthdayToContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['b_day'] = "Mi cumpleaños es el 6 de Julio"
