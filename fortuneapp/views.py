from django.shortcuts import render
import random
import pyaztro
from datetime import datetime

fortunes = [
    "All will go well with your new project",
    "If you continually give, you will continually have.",
    "Self-knowledge is a life long process.",
    "You are busy, but you are happy.",
    "Your abiliteis are unparalleled.",
    "Those who care will make the effort.",
    "Now is the time to try something new.",
    "Miles are covered one step at a time"
]

def index(request):
    fortune = random.choice(fortunes)
    context = {"fortune": fortune}
    return render(request, "fortuneapp/index.html", context)

def horoscope(request):
    today_horoscope = pyaztro.Aztro(sign='aries')
    current_date = datetime.now()
    current_date_format = current_date.strftime(" %b %d %Y")
    horoscope_description = today_horoscope.description
    horoscope_luckynumber = today_horoscope.lucky_number
    horoscope_mood = today_horoscope.mood
    return render(request, "fortuneapp/horoscope.html", {
        'today_date' : current_date_format,
        'description' : horoscope_description,
        'mood' : horoscope_mood,
        'lucky_number' : horoscope_luckynumber
    })