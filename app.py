from flask import Flask, request
import json
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def studentNumber():
    dictionary =  {"Student Number" : "200511517"}
    return json.dumps(dictionary)

@app.route('/webhook',methods=['POST'])
def index():
    #Get the formula1-gossip entity from the dialogflow fullfilment request.
    body = request.json
    drink_name = body['queryResult']['parameters']['Drink']

    #Connect to the API anf get the JSON file.
    api_url = 'http://www.thecocktaildb.com/api/json/v1/1/search.php?s='+drink_name+''
    response = requests.get(api_url) #Connect to f1 API and read the JSON response.
    r=response.json() #Convert the JSON string to a dict for easier parsing.
    
    #Extract weather data we want from the dict and conver to strings to make it easy to generate the dialogflow reply.
    drink = str(r['drinks'][0]['strDrink'])
    

    #Build the Dialogflow reply.
    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The most famous drink with '+drink_name+' is ' + drink + '"] } } ]}'
    return reply
