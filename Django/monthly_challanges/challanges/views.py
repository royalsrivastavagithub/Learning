from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challanges = {
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
    'december': None,
}


def index(request):
    months = list(monthly_challanges.keys())
    return render(request, 'challanges/index.html', {
        'months': months
    })


def monthly_challange_by_number(request, month):
    months = list(monthly_challanges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid Month</h1>')
    forwarded_month = months[month-1]
    redirect_path = reverse('month-challange', args=[forwarded_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challange(request, month):
    try:
        challenge_text = monthly_challanges[month]
        return render(request, 'challanges/challange.html', {
            'text': challenge_text, 'month': month})
    except:
        raise Http404()
