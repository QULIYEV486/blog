from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename
from sqlalchemy import desc

UPLOAD_FOLDER = './static/uploads'
db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///newsssh.db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)



class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(1000), nullable = True)
    content = db.Column(db.String(10000), nullable = True)
   
    
    def __init__(self, title, image, content):
        self.title = title
        self.image = image
        self.content = content        


@app.route("/news/<int:id>/")
def news(id):
    news = News.query.get(id)
    next = News.query.order_by(desc(News.id))[:3]
   
    return render_template('detail.html', news=news, next=next)



 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)


 








