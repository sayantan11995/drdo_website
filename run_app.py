
# from flask import Flask, render_template, request, redirect, url_for, session
# import os
# import random
# import pickle
# from threading import Lock

# app = Flask(__name__)
# # app.secret_key = 'your_secret_key'
# app.secret_key = os.urandom(24)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

