from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def static_page():
    return render_template('selfi_page.html')


if __name__ == '__main__':
    app.run()
