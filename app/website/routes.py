from flask import render_template, request, jsonify, redirect, url_for
from app.website import website
import string
import random
from os.path import join, dirname, realpath

STORAGE_FOLDER = join(dirname(realpath(__file__)), 'storage/')
BASE_URL = 'http://127.0.0.1:5000/'

@website.route('/', methods=['GET', 'POST'])
def homepage():
    """
    Render the homepage templates on the / route
    """
    if request.method == 'POST':
        file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        file_path = STORAGE_FOLDER + file_name
        try:
            mode = 'w'
            file = open(file_path, mode)
            file.write(str(request.form['url']))
            file.close()
            return BASE_URL + file_name
        except Exception as e:
            print("Error Message : " + str(e.message))

    return render_template('website/index.html')


@website.route('/<filename>', methods=['GET', 'POST'])
def redirect_url(filename):
    """
    Redirect the page to the encrypted url
    """
    file_path = STORAGE_FOLDER + filename

    try:
        with open(file_path) as file:
            read_data = file.read()
        return redirect(read_data)
    except Exception as e:
        print("Error Message : " + str(e.message))

    return redirect(url_for('website.homepage'))