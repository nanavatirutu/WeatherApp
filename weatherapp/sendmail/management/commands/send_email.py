"""
Filename:send_email.py
Created on: Oct 18, 2019

Details: 
Fetches information from the database and passes location to client OpenWeather API in order to fetch current and forecasted weather information to create subject line and body of email which is sent to sendgrid api that sends messages.
"""

from django.core.management.base import BaseCommand, CommandError
from ....subscribe.models import UserDetail
import os
from ...SendGrid_Client import *
from weatherapp.sendmail import OpenWeather_Client as a



class Command(BaseCommand):
    help = 'Sends email to each subscribed user'

    def getSubjectLine(todayWeather, tomorrowWeather, weather_desc):
        """
        name: send_email_notification
        Input:
            email: email from the dataset
            location: location from the dataset

        details: 
        This function uses weather features to create personalized subject line.

        """

        if((todayWeather - tomorrowWeather > 5) or (weather_desc.lower() == 'clear sky') ):
            return " It's nice out! Enjoy a discount on us." 

        elif((tomorrowWeather - todayWeather > 5) or ('rain' in weather_desc.lower() )):
            return "Not so nice out? That's okay, enjoy a discount on us."

        else:
            return "Enjoy a discount on us!"

    


    def send_email_notification(self,email,location):
        """
        name: send_email_notification
        Input:
            email: email from the dataset
            location: location from the dataset

        details: 
        This function uses email and location passed by the handle function to generate personalized body and subject line for weather powered email newsletter. 
        It calls openweather API to obtain current weather and weather forecast and sends email using sendgrid API
        """
        todayWeather, weather_desc = a.getWeatherInCity(location)
     
        tommorowWeather = a.getForecast(location)

        subject = Command.getSubjectLine(todayWeather, tommorowWeather, weather_desc)


        email_1 = open("weatherapp/static/email_1.txt","r+")
        email_2 = open("weatherapp/static/email_2.txt","r+")

        email_1 = email_1.read()
        email_2 = email_2.read()

        temp  = round((todayWeather-273.15)*1.8+32.0)
        message = email_1 + " " + str(temp) +"<strong>&#176;</strong>F, " + weather_desc +" in "+ location + email_2
        
        send_email(email, subject, message)

    def handle(self, *args, **options):
      	users = UserDetail.objects.all()
      	for u in users:
      		print(u.email)
      		self.send_email_notification(u.email,u.location)


