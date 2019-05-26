from flask import render_template, request, jsonify, redirect, url_for
from app.website import website
import string
import random
from os.path import join, dirname, realpath

STORAGE_FILE = join(dirname(realpath(__file__)), 'storage/shorten_urls')
BASE_URL = 'http://127.0.0.1:5000/'

@website.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage templates on the / route
    """
    if request.method == 'POST':
        url = request.form['url']
        url_mappings = {}
        with open(STORAGE_FILE, "r") as ins:
            for line in ins:
                if '==' in line:
                    data = line.split('==')
                    url_mappings[data[1].replace('\n', '')] = data[0]

        if request.form['url'] in url_mappings.keys():
            return BASE_URL + url_mappings[url]

        short_url = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        try:
            mode = 'a'
            file = open(STORAGE_FILE, mode)
            file.write(short_url+'=='+str(url+'\n'))
            file.close()
            return BASE_URL + short_url
        except Exception as e:
            print("Error Message : " + str(e.message))

    return render_template('website/index.html')


@website.route('/<url_key>', methods=['GET', 'POST'])
def redirect_url(url_key):
    """
    Redirect the page to the encrypted url
    """

    try:
        with open(STORAGE_FILE, "r") as ins:
            for line in ins:
                data = line.split('==')
                if data[0] == url_key:
                    return redirect(data[1].replace('\n', ''))
    except Exception as e:
        print("Error Message : " + str(e.message))

    return redirect(url_for('website.homepage'))