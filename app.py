import json
from flask import Flask, send_from_directory, render_template, make_response

app = Flask(__name__)
content_directory = "content/"
content_root = content_directory + "cse116.json"


def load_content(content_filename):
    all_content = []
    with open(content_filename) as content_file:
        content = json.load(content_file)
        for week in content:
            with open(content_directory + week) as week_file:
                all_content.append(json.load(week_file))
    return all_content


@app.get('/')
def cse116():
    content = load_content(content_root)
    resp = make_response(render_template('cse116/cse116.html', weeks=content))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/hw/<hw_url>')
def hw(hw_url):
    resp = make_response(render_template('hw/' + str(hw_url)))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


@app.get('/static_files/<path:filename>')
def send_style(filename):
    resp = make_response(send_from_directory('static_files', filename))
    resp.headers["X-Content-Type-Options"] = "nosniff"
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
