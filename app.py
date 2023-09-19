from flask import Flask, send_from_directory, render_template, make_response

app = Flask(__name__)


@app.get('/')
def cse116():
    resp = make_response(render_template('CSE116.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/quiz')
def task1():
    resp = make_response(render_template('quiz.html'))
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


@app.get('/static_files/<path:filename>')
def send_style(filename):
    resp = make_response(send_from_directory('static_files', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
