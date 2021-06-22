from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("templates/index.html", 'r',encoding='utf-8') as viz_file:
        return viz_file.read()
if __name__ == "__main__":
    app.run()
