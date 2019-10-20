from flask import Flask, request, url_for, render_template, jsonify
from twilio.jwt.access_token.grants import ConversationsGrant, VideoGrant

from db_access import *
from twilio.rest import Client
import twilio
import json


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('video.html')

@app.route('/login', methods=["GET", 'POST'])
def login():
    error = None
    if request.method == 'POST' :
        if get_user(request.form['username']).password == request.form['password']:
            session['logged_in'] = True
            session['user'] = 'username'
    if request.method == 'GET' :
        return "yeet"

@app.route('/token')
def generate_token():
    account_sid = 'ACdf34a74e96d1bda2b4463304b8ff0079'
    api_key = 'SKb4ab64c42d3ff80bcd4992e41a7f8195'
    api_secret = 'RX47EgPCyWa7yxrK4oUlyBB2V4SZXDOb'

    # Create an Access Token
    token = twilio.jwt.access_token.AccessToken(account_sid, api_key, api_secret)

    # Set the Identity of this token
    token.identity = "Langston Nashold"

    # Grant access to Conversations
    video_grant = VideoGrant(room='NiceRoom')
    token.add_grant(video_grant)

    # Return token info as JSON
    print(str(token.to_jwt())[2:-1])
    return json.dumps({'identity' : token.identity, 'token' : str(token.to_jwt())[2:-1] })

if __name__ == '__main__':
    app.run()
