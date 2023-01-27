import datetime
import time
import os

from flask import Flask, send_from_directory, render_template, make_response, redirect, request, url_for
import bcrypt

app = Flask(__name__)


# @app.route('/final')
# def final_exam():
#     return redirect("https://docs.google.com/document/d/10oHZKDJSkDNhF-UCUAPZvx3zlR6Q_-ZurJCMymz3x90/edit?usp=sharing")


@app.get('/')
def cse116():
    resp = make_response(render_template('CSE116.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

# @app.get('/teach')
# def ta_a():
#     return redirect("https://docs.google.com/forms/d/e/1FAIpQLScFJ8afYq0RU9o4aZ7YeFVVCnqGbBDdE-EP3VJPUt8o3_77sQ/viewform?usp=sf_link")
#
# @app.get('/apply')
# def ta_b():
#     return redirect("https://docs.google.com/forms/d/e/1FAIpQLScN6jXy7qWTgD0WTfa132Vffa6gYaKNhneKUAoaLOwhwkUBPg/viewform?usp=sf_link")


@app.get('/static_files/<path:filename>')
def send_style(filename):
    resp = make_response(send_from_directory('static_files', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


######### Lecture Question Paths #########

lecture_question_switch = "off"
time_of_latest_turn_off = 0.0  # remember when the question was last turned off to allow for a delay in actually turing it off
turn_off_delay_in_second = 35  # accept submission this long after the question is turned off. This makes up for the delay in AutoLab
hashed_password = b'$2b$12$ttSdEPdcXqGzuLZxtqUQN.1lCj0CM0GORvaCZLqEFTrEvw.88e2eq'  # try and hack me
hashed_token = b'$2b$12$vr9AFns4hEWtRXR.pmoaG.4bbTt553ck9sm5tPXnUJzeMFs35qDFi'
the_token = os.environ.get('token', "oops. Forgot to set envvar for token")
forever = datetime.datetime(3005, 5, 15)

@app.get('/lq')
def lecture_questions():
    token = request.cookies.get('token', "not_the_token")
    authenticated = authenticate(token)
    if authenticated:
        resp = make_response(render_template('lq.html'))
        resp.headers["X-Content-Type-Options"] = "nosniff"
        return resp
    else:
        resp = make_response(render_template('lq_login.html'))
        resp.headers["X-Content-Type-Options"] = "nosniff"
        return resp


@app.post('/lq')
def lecture_questions_login():
    resp = make_response(redirect('/lq'))

    password = request.form.get('password')
    we_good = bcrypt.checkpw(password.encode(), hashed_password)

    if we_good:
        resp.set_cookie('token', the_token, expires=forever)

    return resp


@app.get('/lq_switch')
def get_lecture_question_switch():
    switch = lecture_question_switch
    current_time = time.time()
    if switch == "off" and (current_time - time_of_latest_turn_off < turn_off_delay_in_second):
        switch = "on"
    return switch


@app.post('/lq_switch')
def change_lecture_question_switch():
    global lecture_question_switch
    global time_of_latest_turn_off

    token = request.cookies.get('token')
    authenticated = authenticate(token)

    if not authenticated:
        return "Nice try"
    else:
        if lecture_question_switch == "off":
            lecture_question_switch = "on"
        elif lecture_question_switch == "on":
            lecture_question_switch = "off"
            time_of_latest_turn_off = time.time()
        return lecture_question_switch


def authenticate(token):
    return bcrypt.checkpw(token.encode(), hashed_token)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
