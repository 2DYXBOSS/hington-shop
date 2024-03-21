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


class Ajouter(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(15), unique = False , nullable = False)
    description = db.Column(db.String(100), unique = True , nullable = False)
    couleur = db.Column(db.String(100), unique = True , nullable = False)
    categorie = db.Column(db.String(100), unique = True , nullable = False)
    taille = db.Column(db.String(100), unique = True , nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
    
   
   
    def __init__(self,nom,description,couleur,categorie,taille,image):
        self.nom = nom
        self.description = description
        self.couleur = couleur
        self.categorie = categorie
        self.taille = taille
        self.image = image
        


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
            "couleur": self.couleur,
            "categorie": self.categorie,
            "taille": self.taille,
            "image": self.image,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(15), unique = False , nullable = False)
    mail = db.Column(db.String(100), unique = True , nullable = False)
    message = db.Column(db.String(50), unique = True , nullable = False)
   
   
    def __init__(self,nom,mail,message):
        self.nom = nom
        self.mail = mail
        self.message = message
        


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, mail: {self.mail}, age: {self.age})"
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "mail": self.mail,
            "message": self.message,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")




@app.route('/commentaire', methods=['POST'])
def commentaire():
    nom = request.form.get("nom")
    mail = request.form.get("mail")
    message = request.form.get("message")

    envoyer = Comment(nom=nom, message=message,mail=mail)

        
    db.session.add(envoyer)
    db.session.commit()
             
    return redirect('/')

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
        image = request.form.get("image")      
        couleur = request.form.get('couleur')
        taille = request.form.get('taille')
        categorie = request.form.get('categorie')
         

        pani = Ajouter(nom=nom,description=description,couleur=couleur,categorie=categorie,taille=taille,image=image)
        # pani = Panier(nom = nom, description = description , prix = prix)
        
        db.session.add(pani)
        db.session.commit()
             

        return redirect("/")
    except :
        return render_template("/boutique.html")
    
@app.route("/vente")
def acc():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementHomme':
            data.append(i)
    return render_template("/vente.html", data = data)
@app.route("/montre")
def montre():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'Montre':
            data.append(i)
    
    return render_template("/montre.html", data = data)


# FIN AJOUTER IMAGES DES ARTICLES{}
    

# @app.route("/")
# def acc():
#     return render_template("/vente.html", data = data)

# @app.route("/")
# def acc():
#     return render_template("/acceuil.html")

@app.route("/ajou")
def ajou():
   
    eude = Ajouter.query.all()
    return render_template("/ajoufini.html")

@app.route('/montres/<int:id>')
def montres(id):
    
    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                data.append(i)
        return render_template('montrederail.html',user = user,data=data)
    print("MO")

    return redirect("/montre")
@app.route('/info/<int:id>')
def info(id):
    
    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                data.append(i)
        return render_template('info.html',user = user,data=data)
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
    return redirect(f"https://api.whatsapp.com/send/?phone=2250787022061&text={ms}&type=phone_number&app_absent=0")
    # return redirect("/vente")
    




@app.route("/administa")
def administa():

    administa = Ajouter.query.all()

    return render_template("administa.html",administa=administa)

@app.route("/indisponible")
def indisponible():

    return render_template("indiso.html")

@app.route("/")
def acceuil():
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    print(commenta[0].mail)
    
    return render_template("acceuil.html",commenta=commenta)


@app.route("/Suppesz/<int:id>")
def Suppesz(id):

    adm= Ajouter.query.get(id)
    db.session.delete(adm)
    db.session.commit()
    
    

    return redirect("/administa")


@app.route("/informsa")
def informsa():

    # return redirect(f"image/{id}") dans le html
    return render_template("informate.html")

 


@app.route("/image/<int:id>")
def image(id):

    return render_template("selectimage.html")



# AJOUTER IMAGES DES ARTICLES{}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_objetwere', methods=['POST'])
def add_objetwere():
    try :
        if 'file' not in request.files:
            flash('No file part')
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file.filename)
        if file.filename == '':
            flash('Aucune image sélectionnée pour le téléchargement')
            print('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print('upload_image filename: ' + filename)
            flash('Image téléchargée avec succès et affichée ci-dessous')
            print('Image téléchargée avec succès et affichée ci-dessous')
            return render_template('selectimage.html', filename=file.filename)
            # return render_template('boutique.html', filename=filename)
    except:
        flash('Les types dimages autorisés sont - png, jpg, jpeg, gif')
        print('eerrr')
        return redirect(request.url)

        # uploads.image
 
# @app.route('/display/<filename>')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename = 'uploads/' + filename), code=301)
# FIN AJOUTER IMAGES DES ARTICLES{}




if __name__ == '__main__' :
    app.run(debug=True,port=5004)
