#You need to create a class and add 'generic.FormView'
#You can put any name in this case 'CreateUser'

from django.urls import reverse_lazy

class CreateUser(generic.FormView):
    template_name = 'register/register.html' # Template's name  
    success_url = reverse_lazy('usersaved:newprofile') #Where to go after to create the user

#Django already has a create user, you only have to call it with this function
    def form_valid(self, form):
        user = form.save()
        return super(Register, self).form_valid(form)

