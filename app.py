from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import os
import datetime

data = datetime.date.today()
dataheure = datetime.datetime.now()
formatted_time = dataheure.strftime('%H')
formatted = dataheure.strftime('%M')
print(formatted_time)
print(formatted)
print(dataheure)


from flask import Flask, request, render_template, redirect, url_for,send_file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# import pywhatkit

# Configurations pour le serveur SMTP


app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'BONJOUR'


app.config['SECRET_KEY'] = 'sdfgghjklhkj'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '0streamblay@gmail.com'
app.config['MAIL_PASSWORD'] = 'vgux fpjq qyqr nxem'
app.config['MAIL_DEFAULT_SENDER'] = '0streamblay@gmail.com'



SMTP_SERVER = 'smtp.googlemail.com'  # Remplacez par l'adresse de votre serveur SMTP
SMTP_PORT = 587  # Port SMTP (généralement 587 pour TLS)
SMTP_USERNAME = 'pythonanywhere225@gmail.com'
SMTP_PASSWORD = 'tdqn cklm uvjd aonn'
# Clé secrète pour sécuriser l'application
app.secret_key = os.urandom(24)
mail = Mail(app)
# fin

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


db = SQLAlchemy(app)



debug = True

class Maboutik(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    prix = db.Column(db.Integer,nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)
    like = db.Column(db.Integer, unique = False , nullable = False)
   
    def __init__(self,nom,description,prix,image,categorie,like):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.image = image
        self.categorie = categorie
        self.like = like


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "description": self.description,
            "prix": self.prix,
            "image": self.image,
            "categorie": self.categorie,
            "like": self.like
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")





# AJOUTER IMAGES DES ARTICLES{}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/add_objet')
def add_objet():
    
    return render_template("boutique.html")

@app.route('/add_objet', methods=['POST'])
def upload_image():
    try :
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            flash('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            flash('Image téléchargée avec succès et affichée ci-dessous')
            return render_template('boutique.html', filename=file.filename)
            # return render_template('boutique.html', filename=filename)
    except:
        flash('Les types dimages autorisés sont - png, jpg, jpeg, gif')
        return redirect(request.url)

        # uploads.image
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = 'uploads/' + filename), code=301)
# FIN AJOUTER IMAGES DES ARTICLES{}










# AJOUTER DES ARTICLES{}

@app.route('/objet',methods = ["POST"])
def objet(): 
    
    try :
        nom = request.form.get("nom")
        description = request.form.get("description")
        prix = request.form.get("prix")
        image = request.form.get("image") 
        like = 0 
        
        print('recu1')      
        categorie = request.form.get('selectOptione')
        print('recu2',categorie)      

        pani = Maboutik(nom = nom, description = description , prix = prix, image = image, categorie = categorie ,like=like)
        # pani = Panier(nom = nom, description = description , prix = prix)
        
        db.session.add(pani)
        db.session.commit()
             

        return redirect("/vente")
    except :
        return render_template("/boutique.html")
    
@app.route("/vente")
def acc():
    data = Maboutik.query.all()
    return render_template("/vente.html", data = data)


# FIN AJOUTER IMAGES DES ARTICLES{}
    

# @app.route("/")
# def acc():
#     return render_template("/vente.html", data = data)

# @app.route("/")
# def acc():
#     return render_template("/acceuil.html")

@app.route("/ajou")
def ajou():
   
    eude = Maboutik.query.all()
    return render_template("/ajoufini.html")

@app.route('/info/<int:id>')
def info(id):
    
    user = Maboutik.query.filter_by(id=id).first()
    if user :

        return render_template('info.html',user = user)
    print("MO")
    return redirect("/vente")

# @app.route('/zet/<int:id>')
# def zet(id):
    
#     user = Maboutik.query.filter_by(id=id).first()
#     return render_template('info.html',user = user)

# @app.route('/info/<int:id>',methods=["POST"])
# def info(id):
#     if request.method == "POST" :
#         user = Maboutik.query.filter_by(id=id).first()
#         return render_template('info.html',user = user)
#     print("MO")
#     return redirect("/vente")



from urllib.parse import quote
@app.route('/ssm/<int:id>', methods=["POST"])
def ssm(id):
    a = str(id)

    tabNum = "+2250787022061"
    ms = "https://hington-shop.onrender.com/info/" + a

    # Encode the message string before passing it to the quote function
    # encoded_message = ms.encode('utf-8')
    # pywhatkit.sendwhats_image("+2250787022061", "bonjou", formatted_time, 45)
    # pywhatkit.sendwhats_image("+2250787022061", "https://web.whatsapp.com/send?phone=+22578587708&text={ms}", formatted_time, formatted)
    # return redirect(f"https://web.whatsapp.com/send?phone=+22578587708&text={ms}")
    return redirect(f"https://api.whatsapp.com/send/?phone=22578587708&text={ms}&type=phone_number&app_absent=0")
    # return redirect("/vente")
    
if __name__ == '__main__' :
    app.run(debug=True,port=5004)
