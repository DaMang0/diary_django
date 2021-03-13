# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, DeleteView, TemplateView
# from django.http import HttpResponse
# from .models import Quote

# # Create your views here.
# def Index(request):
#   return HttpResponse("<h1>Index Page</h1>")

# class QuoteListView(ListView):

#   model = Quote
#   template_name = 'quotes/quotes_listview.html'
#   queryset = Quote.objects.all().order_by('-created')
  
#   context_object_name = 'quote_list'

# class QuoteCreateView(CreateView):

#   model = Quote
#   fields = ['message']
#   template_name = 'quotes/quotes_createform.html'

# class QuoteDeleteView(DeleteView):
#   model = Quote
#   success_url = reverse_lazy('quotes:index')

#   def get_object(self):
#     pk_ = self.kwargs.get("pk")
#     return get_object_or_404(Quote, pk=pk_)

# class ValueTemplateView(TemplateView):
#   template_name = 'quotes/values.html'