from flask import render_template
from app import app
from app import dao


@app.route('/')
def index():
    categories=dao.load_categories()
    return render_template("index.html", categories=categories)

if __name__=='__main__':
    print(app.root_path)
    app.run(debug=True)