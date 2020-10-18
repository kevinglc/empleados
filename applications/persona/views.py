from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Empleado

# Create your views here.
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm


class InicioView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'inicio.html'
    

class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by=4
    ordering='first_name'
    model=Empleado
    context_object_name='empleados'
    def get_queryset(self):
        
        palabra_clave=self.request.GET.get("kword",'')
        
        lista=Empleado.objects.filter(
            
                first_name__icontains=palabra_clave
        )
        print('lista resultado :',lista)
        return lista


class ListbyArea(ListView):
    """Lista empleados de un Area"""
    template_name='persona/list_by_area.html'
    context_object_name='empleados'     

    def get_queryset(self):
        area=self.kwargs['shor_name']
        lista=Empleado.objects.filter(
            departamento__shor_name =area
        )	
        return lista  


class listEmpleadoByKword(ListView):
    """Lista empleados por palabra clave"""
    template_name='persona/by_kword.html'
    context_object_name='empleados'

    def get_queryset(self):
        print('*****************************')
        palabra_clave=self.request.GET.get("kword",'')
        print('=======',palabra_clave)
        lista=Empleado.objects.filter(
            first_name =palabra_clave
        )
        print('lista resultado :',lista)
        return lista



class HabilidadesEmpleado(ListView):
    
    template_name = "persona/habilidades.html"
    context_object_name='habilidades'

    def get_queryset(self):
        empleado=Empleado.objects.get(id=1)
        print(empleado.habilidades.all())
        
        return empleado.habilidades.all()



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self,**kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)

        context['titulo']='Empleado del Mes'
        return context


 
class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class=EmpleadoForm
    
    success_url= reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        """Aca validamos los datos del form. si queremos algo mas despues del guardado"""
        
        empleado = form.save(commit=False)
        print(empleado)
        empleado.full_name= empleado.first_name+ ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields=['first_name','last_name','job','departamento','habilidades']
    success_url= reverse_lazy('persona_app:empleados_admin')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('****************+++++MENTODO POST++++++++*********************')
        print('**************************************************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        """Aca validamos los datos del form. si queremos algo mas despues del guardado"""
        print('****************+++++MENTODO FORM_VALID++++++++*********************')
        print('**************************************************************')
        
        return super(EmpleadoUpdateView,self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    
    fields=['first_name','last_name','job','departamento','habilidades']
    success_url= reverse_lazy('persona_app:empleados_admin')


class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by=10
    ordering='first_name'
    model=Empleado
    context_object_name='empleados'
    
