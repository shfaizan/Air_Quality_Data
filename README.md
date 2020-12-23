## For  ActiveBuildings Assignments

## Task
1.  Here is a link of real time air quality data source [https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us](https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us)
    
2.  Use the link mentioned in the point above, scrape all the pollutants readings from the web page.
    
3.  Create a rest api using the Django framework to fetch the scraped pollutant data. The pollutant data should be returned as a simple key value pair, you can use any keys of your choice to represent the data.
4. Host this service on netlify/heroku or your local machine.
5. Share your code with the necessary documentation.

So for this assignment I have created a RestAPI along with the HTML template to render the data of the pollutant.

## My method

1. First of all create a django project using 
```
 django-admin startproject Airquality 
```
Now I create a django app
```
python manage.py Scrape
```

2. I understand that the data on the website contains data about different pollutant so I use the beautiful-soap to Scrape the data.
```angular2html
pollutants = dict()
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.findAll("div", {"class": "pollutant-item odd"})
        for result in results:
            name = result.find('div', attrs={'class': 'name'}).text
            value = result.find('div', attrs={'class': 'value'}).text
            pollutants[name] = value
        results = soup.findAll("div", {"class": "pollutant-item even"})
        for result in results:
            name = result.find('div', attrs={'class': 'name'}).text
            value = result.find('div', attrs={'class': 'value'}).text
            pollutants[name] = value
        return pollutants
```
3. I created the HTML template to render the data as a key-value pair
```angular2html
{% for k , v in dict.items %}
        <li>{{ k }} : {{ v}}</li>
```

4. I configure the URl and views to get the pollutant data of gurugam
<br> URL:
```angular2html
urlpatterns = [
  path('', Fetch.as_view(), name='search_view'),
  ]
```
 View:
```angular2html
class Fetch(APIView):
    def get(self, request):
        data = get_gurugram_pollutants()
        return Response(data=data, status=status.HTTP_200_OK)
```

5. Now I had deployed the project on heroku For this I use the Huroku CLI to login and do the following steps for the deployment
```angular2html
heroku login 
heroku create
heroku git:remote -a Project_name 
```
Git initialize
```angular2html
git init 
git add .
git commit -m "message"
```
6. Now Create a proper requirements.txt file and a Procfile this will contain the code that will deploy our code in the Production environment.
```angular2html
web: gunicorn Airquality.wsgi
```
For windows, we can use the alternate library named waitress for testing.

7. Now we will push our code to heroku 
```angular2html
git push heroku master
```

## Testing 

For the restapi tested on Insomnia/Postman:
```angular2html
https://pure-sierra-88686.herokuapp.com/fetch
```
Test the api on HTML template
```angular2html
https://pure-sierra-88686.herokuapp.com
```
<br><br>
**************** THANK YOU ********************

