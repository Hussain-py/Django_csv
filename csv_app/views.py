from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http import HttpResponse
from .forms import InputForm
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from .models import keyword_info, buisness_leads
import pandas as pd
import json
import csv
import re
import json
import time


def save_file(request):
   # data = open(os.path.join(settings.PROJECT_PATH,'data/table.csv'),'r').read()
    file_path =settings.MEDIA_ROOT +'/'+ 'links.csv'
    response = HttpResponse(file_path, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=links.csv'
    return response

# Simple CSV Read Operation
def Table(request):
    file_path = settings.MEDIA_ROOT + '/' + 'links.csv'
    df = pd.read_csv(file_path)
    # df = pd.read_csv("django_csv/media/links8.csv")
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table.html', context)


def home_view(request):
    context = {}
    context['form'] = InputForm()
    if request.method == "POST":
        # Get the posted form
        Form = InputForm(request.POST)
        if Form.is_valid():
            Skeyword = Form.cleaned_data['search_term']

            """Generate a url from search term"""
            url = "https://www.google.co.in/search?biw=1366&bih=657&ei=8wEHYJGGHb2f4-EPuo-N8AU&q={}"
            search_key = Skeyword.replace(' ', '+')
            # add term query to url
            url = url.format(search_key)
            r = requests.get(url)

        def get_phone(soup):
            try:
                phone = soup.select("a[href*=callto]")[0].text
                return phone
            except:
                pass
            try:
                phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
                return phone
            except:
                pass
            try:
                phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
                return phone
            except:
                # print('Phone number not found')
                phone = ''
                return phone

        def get_email(soup):
            try:
                email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
                return email
            except:
                pass
            try:
                email = soup.select("a[href*=mailto]")[-1].text
            except:
                # print('Email not found')
                email = ''
                return email

        data = BeautifulSoup(r.text, 'html.parser')
        tags = data.find_all("a")

        substr = "https"
        records = []
        for link in tags:
            link = link.get('href').replace('/url?q=', '')
            if link.__contains__(substr):
                records.append(link)
        print(records)

        list = []
        for item in records:
            try:
                response = requests.get(item)
                soup = BeautifulSoup(response.text, 'html.parser')
            except:
                print('Unsucessful: ' + str(response))
                continue
            phone = get_phone(soup)
            email = get_email(soup)
            data_instance = keyword_info.objects.create(number=phone, email=email, title=item)
            data_instance.save()
            # print('website:%s\nphone: %s\nemail: %s\n' % ( phone, email, item))
            results = (item, phone, email)

            print(results)
            for item in results:
                list.append(results)

                with open('media/links.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Url', 'Number', 'Email'])
                    writer.writerows(list)
    else:
        redirect('/forms')
    return render(request, "forms.html", context)


