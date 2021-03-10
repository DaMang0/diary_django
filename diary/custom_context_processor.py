from datetime import date

today = date.today()
year = today.year
month = today.month
day = today.day
def date_renderer(request):
  return {
    'day': day,
    'month': month,
    'year': year,
  }