from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
# Create your views here.

monthly_challanges_dict = {
    'january': 'Eat no meat for this month',
    'february': 'Exercise for 30 minutes each day',
    'march': 'Learn Django for at least 1 hour each day',
    'april': 'Eat one piece of fruit for breakfast',
    'may': 'Read 1 book',
    'june': 'Take a 10 minutes walk after dinner',
    'july': 'Write 3 pages of journal each day',
    'august': 'Practice Yoga for 30 minutes each day',
    'september': 'Donate 1 dollar to a charity',
    'october': 'Say thank you to someone you appreciate',
    'november': 'Write 3 thank you letters to someone you appreciate',
    'december': 'Eat one piece of fruit for breakfast',
}

def index( request ):
    list_items = ''
    months = list(monthly_challanges_dict.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challange', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid Month</h1>')
    forwarded_month = months[month-1]
    redirect_path = reverse('month-challange', args=[forwarded_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challanges(request, month):
    challange_text = monthly_challanges_dict.get(month)
    if challange_text is None:
        return HttpResponseNotFound('<h1>Not Found</h1>')
    return HttpResponse(f'<h1>{challange_text}</h1>')

