from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

def lesChiffres(request):
    return render(request, "lesChiffres.html", locals())