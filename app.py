import os

from requests_html import HTMLSession
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/<path:url>")
def index(url):
    if url:
        s = HTMLSession()
        try:
            r = s.get(url)
        except:
            abort(404)
        results = r.html.find("meta")
        r_list = [result.attrs for result in results]
        return render_template("index.html", results=r_list)
    else:
        return render_template("error.html")


@app.errorhandler(404)
@app.errorhandler(405)
def general_error(e):
    """404 & 405 page custom error handler
    Returns the general.html template and 405 status
    """

    return render_template("error.html", error=e), e.code


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(
        os.getenv("PORT", "5000")), debug=False)
