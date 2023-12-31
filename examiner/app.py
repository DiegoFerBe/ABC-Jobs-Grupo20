from examiner import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from celery import Celery
import requests
import json


app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)