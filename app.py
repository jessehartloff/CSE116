from flask import Flask, send_from_directory, render_template, make_response

app = Flask(__name__)


@app.get('/')
def cse116():
    resp = make_response(render_template('CSE116.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task1')
def task1():
    resp = make_response(render_template('hw/task1.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task2')
def task2():
    resp = make_response(render_template('hw/task2.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task3')
def task3():
    resp = make_response(render_template('hw/task3.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task4')
def task4():
    resp = make_response(render_template('hw/task4.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task5')
def task5():
    resp = make_response(render_template('hw/task5.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task6')
def task6():
    resp = make_response(render_template('hw/task6.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task7')
def task7():
    resp = make_response(render_template('hw/task7.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/task8')
def task8():
    resp = make_response(render_template('hw/task8.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/ao1')
def ao1():
    resp = make_response(render_template('hw/ao1.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp



@app.get('/quiz1/1')
def quiz1_1():
    resp = make_response(render_template('quiz/v1.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/2')
def quiz1_2():
    resp = make_response(render_template('quiz/v2.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/3')
def quiz1_3():
    resp = make_response(render_template('quiz/v3.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/4')
def quiz1_4():
    resp = make_response(render_template('quiz/v4.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/5')
def quiz1_5():
    resp = make_response(render_template('quiz/v5.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/6')
def quiz1_6():
    resp = make_response(render_template('quiz/v6.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/7')
def quiz1_7():
    resp = make_response(render_template('quiz/v7.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/8')
def quiz1_8():
    resp = make_response(render_template('quiz/v8.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/9')
def quiz1_9():
    resp = make_response(render_template('quiz/v9.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/10')
def quiz1_10():
    resp = make_response(render_template('quiz/v10.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/11')
def quiz1_11():
    resp = make_response(render_template('quiz/v11.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/12')
def quiz1_12():
    resp = make_response(render_template('quiz/v12.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/13')
def quiz1_13():
    resp = make_response(render_template('quiz/v13.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/14')
def quiz1_14():
    resp = make_response(render_template('quiz/v14.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/15')
def quiz1_15():
    resp = make_response(render_template('quiz/v15.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/16')
def quiz1_16():
    resp = make_response(render_template('quiz/v16.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/17')
def quiz1_17():
    resp = make_response(render_template('quiz/v17.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/18')
def quiz1_18():
    resp = make_response(render_template('quiz/v18.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/19')
def quiz1_19():
    resp = make_response(render_template('quiz/v19.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp

@app.get('/quiz1/20')
def quiz1_20():
    resp = make_response(render_template('quiz/v20.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp



@app.get('/static_files/<path:filename>')
def send_style(filename):
    resp = make_response(send_from_directory('static_files', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
