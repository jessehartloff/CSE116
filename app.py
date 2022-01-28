from flask import Flask, send_from_directory, render_template, make_response, redirect

app = Flask(__name__)


# @app.route('/final')
# def final_exam():
#     return redirect("https://docs.google.com/document/d/10oHZKDJSkDNhF-UCUAPZvx3zlR6Q_-ZurJCMymz3x90/edit?usp=sharing")


@app.route('/')
def cse116():
    resp = make_response(render_template('CSE116.html'))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.route('/static_files/<path:filename>')
def send_style(filename):
    resp = make_response(send_from_directory('static_files', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
