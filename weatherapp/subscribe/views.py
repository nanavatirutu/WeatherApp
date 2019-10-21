from django.shortcuts import render
from .forms import AddressForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import redirect


class AddressFormView(FormView):
	form_class = AddressForm
	success_url = reverse_lazy('success')
	
	



	def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
		obj = UserDetail()
		obj.email = form.cleaned_data['email'].lower()
		obj.location = form.cleaned_data['location']
		try:
			obj.save()
		except:
			return redirect("/enrolled")

		return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'success.html'   

class EnrollView(TemplateView):
    template_name = 'enrolled.html'    