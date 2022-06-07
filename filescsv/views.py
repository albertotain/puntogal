from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django_extensions import logging

from .models import Filescsv
import csv


def csv(request):         
    if request.method == "POST":
        # b = Filescsv(roid='Beatles Blog', domain_name='All the latest Beatles news.')
        # print(b)
        # b.save()
        
        try:
            csv_file = request.FILES["csv"]
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return HttpResponseRedirect(reverse("csv"))

            file_data = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            for line in lines:
                fields = line.split(",")
                # data_dict = {
                #     roid : fields[0],
                #     domain_name : fields[1]
                # }
                #data_dict["creation_date"] = fields[2]
                # form = Filescsv(data_dict)
                form = Filescsv(roid=fields[0], domain_name=fields[1])
                form.save()
            messages.success(request, "Datos cargado correctamente")

        except Exception as e:
            #messages.error(request, "Incapaz de cargar o arquivo. " + repr(e))
            messages.error(request, "Incapaz de cargar o arquivo.")
        # print(request.FILES['csv'].read())
        # reader=request.FILES['csv'].read()
        # print(reader)
        # for row in reader:
        #     print(row)
        # return redirect(reverse('csv'))
    return render(request, "admin/csv.html")
