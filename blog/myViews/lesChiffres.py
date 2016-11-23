# coding: utf-8
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

def lesChiffres(request, kwargs):
    return render(request, "lesChiffres.html", kwargs)