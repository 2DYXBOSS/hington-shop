from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template , redirect , request,url_for,flash,Response
from flask import render_template , redirect , request,url_for,flash,session ,Response
from sqlalchemy import ARRAY
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
import os
import datetime

data = datetime.date.today()
dataheure = datetime.datetime.now()
formatted_time = dataheure.strftime('%H')
formatted = dataheure.strftime('%M')
print(data)
print(dataheure)
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

class Adminit(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(100), unique = False , nullable = False) 
    description = db.Column(db.String(100), unique = False , nullable = False) 
    nom = db.Column(db.String(100), unique = False , nullable = False) 
    derfjj = db.Column(db.String(), unique = False , nullable = False)
    
   
    def __init__(self,nom,numero,tags):
        self.nom = nom
        self.numero = numero
        self.tags = tags
       
       
    def __repr__(self):
        
        return {
            "nom": self.nom,
            "numero": self.numero,
            "tags": self.tags,
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

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
    description = db.Column(db.String(100), unique = False , nullable = False)
    prix = db.Column(db.String(100), unique = False , nullable = False)
    porce = db.Column(db.String(100), unique = False , nullable = False)
    porceprix = db.Column(db.String(100), unique = False , nullable = False)
    categorie = db.Column(db.String(100), unique = False , nullable = False)
    image = db.Column(db.String(100), unique = True , nullable = False)
    twoimage = db.Column(db.String(100), unique = False , nullable = False)
    threeimage = db.Column(db.String(100), unique = False , nullable = False)
    forimage = db.Column(db.String(100), unique = False , nullable = False)
    xs = db.Column(db.String(100), unique = False , nullable = False)
    s = db.Column(db.String(100), unique = False , nullable = False)
    m = db.Column(db.String(100), unique = False , nullable = False)
    l = db.Column(db.String(100), unique = False , nullable = False)
    xl = db.Column(db.String(100), unique = False , nullable = False)
    xxl = db.Column(db.String(100), unique = False , nullable = False)
    rouge = db.Column(db.String(100), unique = False , nullable = False)
    blanc = db.Column(db.String(100), unique = False , nullable = False)
    noir = db.Column(db.String(100), unique = False , nullable = False)
    jaune = db.Column(db.String(100), unique = False , nullable = False)
    vert = db.Column(db.String(100), unique = False , nullable = False)
    orange = db.Column(db.String(100), unique = False , nullable = False)
    bleu = db.Column(db.String(100), unique = False , nullable = False)
    rose = db.Column(db.String(100), unique = False , nullable = False)
    marron = db.Column(db.String(100), unique = False , nullable = False)
    violet = db.Column(db.String(100), unique = False , nullable = False)
    gris = db.Column(db.String(100), unique = False , nullable = False)
    tranwite = db.Column(db.String(100), unique = False , nullable = False)
    tranneuf = db.Column(db.String(100), unique = False , nullable = False)
    karente = db.Column(db.String(100), unique = False , nullable = False)
    tranwiteun = db.Column(db.String(100), unique = False , nullable = False)
    tranwitedeux = db.Column(db.String(100), unique = False , nullable = False)
    tranwitrois = db.Column(db.String(100), unique = False , nullable = False)
    tranwitekate = db.Column(db.String(100), unique = False , nullable = False)
   
   
   
    def __init__(self,nom,description,prix,porce,porceprix,categorie,image,twoimage,threeimage,forimage,xs,s,m,l,xl,xxl,rouge,blanc,noir,jaune,vert,orange,bleu,rose,marron,violet,gris,tranwite,tranneuf,karente,tranwiteun,tranwitedeux,tranwitrois,tranwitekate):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.porce = porce
        self.porceprix = porceprix
        self.categorie = categorie
        self.image = image
        self.twoimage = twoimage
        self.threeimage = threeimage
        self.forimage = forimage
        self.xs = xs
        self.s = s
        self.m = m
        self.l = l
        self.xl = xl
        self.xxl = xxl
        self.rouge = rouge
        self.blanc = blanc
        self.noir = noir
        self.jaune = jaune
        self.vert = vert
        self.orange = orange
        self.bleu = bleu
        self.rose = rose
        self.marron = marron
        self.violet = violet
        self.gris = gris
        self.tranwite = tranwite
        self.tranneuf = tranneuf
        self.karente = karente
        self.tranwiteun = tranwiteun
        self.tranwitedeux = tranwitedeux
        self.tranwitrois = tranwitrois
        self.tranwitekate = tranwitekate
      
        


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
            "porceprix": self.porceprix,
            "porce": self.porce,
            "categorie": self.categorie,
            "image": self.image,
            "twoimage": self.twoimage,
            "threeimage": self.threeimage,
            "forimage": self.forimage,
            "xs": self.xs,
            "s": self.s,
            "m": self.m,
            "l": self.l,
            "xl": self.xl,
            "xxl": self.xxl,
            "rouge": self.rouge,
            "blanc": self.blanc,
            "noir": self.noir,
            "jaune": self.jaune,
            "vert": self.vert,
            "orange": self.orange,
            "bleu": self.bleu,
            "rose": self.rose,
            "marron": self.marron,
            "violet": self.violet,
            "gris": self.gris,
            "tranwite" : self.tranwite ,
            "tranneuf" : self.tranneuf,
            "karente" : self.karente,
            "tranwiteun" : self.tranwiteun,
            "tranwitedeux" : self.tranwitedeux,
            "tranwitrois" : self.tranwitrois,
            "tranwitekate" : self.tranwitekate,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")

class Profil(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique = False , nullable = False)
    last_name = db.Column(db.String(20), unique = True , nullable = False)
    age = db.Column(db.String(8),nullable = False)

    # achat = db.relationship('Panier',back_populates='prendre')
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # db.init_app(app)
    # with app.app_context() :
    #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(first_name: {self.first_name}, last_name: {self.last_name}, age: {self.age})"
    def __repr__(self):
        
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
    
class Comment(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nom = db.Column(db.String(15), unique = False , nullable = False)
    mail = db.Column(db.String(100), unique = False, nullable = False)
    message = db.Column(db.String(50), unique = False, nullable = False)
    heure = db.Column(db.String(50), unique = False, nullable = False)
   
   
    def __init__(self,nom,mail,message,heure):
        self.nom = nom
        self.mail = mail
        self.message = message
        self.heure = heure
        


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
            "heure": self.heure,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


class Panieruser(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    identifiant = db.Column(db.String(15), unique = False , nullable = False)
    image = db.Column(db.String(15), unique = False , nullable = False)
    produite = db.Column(db.String(15), unique = False , nullable = False)
    prixtottal = db.Column(db.String(100), unique = False , nullable = False)
    quantiteto = db.Column(db.String(100), unique = False , nullable = False)
    tailed = db.Column(db.String(100), unique = False , nullable = False)
    xs = db.Column(db.String(100), unique = False , nullable = False)
    xsn = db.Column(db.String(100), unique = False , nullable = False)
    s = db.Column(db.String(100), unique = False , nullable = False)
    sn = db.Column(db.String(100), unique = False , nullable = False)
    m = db.Column(db.String(100), unique = False , nullable = False)
    mn = db.Column(db.String(100), unique = False , nullable = False)
    l = db.Column(db.String(100), unique = False , nullable = False)
    ln = db.Column(db.String(100), unique = False , nullable = False)
    xl = db.Column(db.String(100), unique = False , nullable = False)
    xln = db.Column(db.String(100), unique = False , nullable = False)
    xxl = db.Column(db.String(100), unique = False , nullable = False)
    xxln = db.Column(db.String(100), unique = False , nullable = False)
    tranwite = db.Column(db.String(100), unique = False , nullable = False)
    tranwiten = db.Column(db.String(100), unique = False , nullable = False)
    tranneuf = db.Column(db.String(100), unique = False , nullable = False)
    tranneufn = db.Column(db.String(100), unique = False , nullable = False)
    karente = db.Column(db.String(100), unique = False , nullable = False)
    karenten = db.Column(db.String(100), unique = False , nullable = False)
    tranwiteun = db.Column(db.String(100), unique = False , nullable = False)
    tranwiteunn = db.Column(db.String(100), unique = False , nullable = False)
    tranwitedeux = db.Column(db.String(100), unique = False , nullable = False)
    tranwitedeuxn = db.Column(db.String(100), unique = False , nullable = False)
    tranwitrois = db.Column(db.String(100), unique = False , nullable = False)
    tranwitroisn = db.Column(db.String(100), unique = False , nullable = False)
    tranwitekate = db.Column(db.String(100), unique = False , nullable = False)
    tranwitekaten = db.Column(db.String(100), unique = False , nullable = False)
   
   
   
    def __init__(self,identifiant,tailed,image,produite,prixtottal,quantiteto,xs,xsn,s,sn,m,mn,l,ln,xl,xln,xxl,xxln,tranwite,tranwiten,tranneuf,tranneufn,karente,karenten,tranwiteun,tranwiteunn,tranwitedeux,tranwitedeuxn,tranwitrois,tranwitroisn,tranwitekate,tranwitekaten):
        self.identifiant = identifiant
        self.image = image
        self.produite = produite
        self.tailed = tailed
        self.prixtottal = prixtottal
        self.quantiteto = quantiteto
        self.xs = xs
        self.xsn = xsn
        self.s = s
        self.sn = sn
        self.m = m
        self.mn = mn
        self.l = l
        self.ln = ln
        self.xl = xl
        self.xln = xln
        self.xxl = xxl
        self.xxln = xxln
        self.tranwite = tranwite
        self.tranwiten = tranwiten
        self.tranneuf = tranneuf
        self.tranneufn = tranneufn
        self.karente = karente
        self.karenten = karenten
        self.tranwiteun = tranwiteun
        self.tranwiteunn = tranwiteunn
        self.tranwitedeux = tranwitedeux
        self.tranwitedeuxn = tranwitedeuxn
        self.tranwitrois = tranwitrois
        self.tranwitroisn = tranwitroisn
        self.tranwitekate = tranwitekate
        self.tranwitekaten = tranwitekaten
      
        


    # db.init_app(app)
    # with app.app_context() :
    # #     db.create_all()
    # def __str__(self):
    #     # Renvoie une chaîne de caractères représentant l'objet
    #     return f"Person(nom: {self.nom}, description: {self.description}, age: {self.age})"
    def __repr__(self):
        
        return {
            "identifiant": self.identifiant,
            "image": self.image,
            "produite": self.produite,
            "tailed": self.tailed,
            "prixtottal": self.prixtottal,
            "quantiteto": self.quantiteto,
            "xs": self.xs,
            "xsn": self.xsn,
            "s": self.s,
            "sn": self.sn,
            "m": self.m,
            "mn": self.mn,
            "l": self.l,
            "ln": self.ln,
            "xl": self.xl,
            "xln": self.xln,
            "xxl": self.xxl,
            "xxln": self.xxln,
            "tranwite" : self.tranwite ,
            "tranwiten" : self.tranwiten ,
            "tranneuf" : self.tranneuf,
            "tranneufn" : self.tranneufn,
            "karente" : self.karente,
            "karenten" : self.karenten,
            "tranwiteun" : self.tranwiteun,
            "tranwiteunn" : self.tranwiteunn,
            "tranwitedeux" : self.tranwitedeux,
            "tranwitedeuxn" : self.tranwitedeuxn,
            "tranwitrois" : self.tranwitrois,
            "tranwitroisn" : self.tranwitroisn,
            "tranwitekate" : self.tranwitekate,
            "tranwitekaten" : self.tranwitekaten,
            
        }
    

with app.app_context() :
    try :
        db.create_all()
    except Exception as e:
        print("error de creation de la table")


@app.route('/commentaire', methods=['POST'])
def commentaire():
    print(formatted_time)
    print(formatted)
    nom = request.form.get("nom")
    mail = request.form.get("mail")
    message = request.form.get("message")
    heure = f"Le {data} depuis Abidjan,CI à {formatted_time}h{formatted}"

    envoyer = Comment(nom=nom, message=message,mail=mail,heure=heure)

        
    db.session.add(envoyer)
    db.session.commit()
             
    return redirect('/')

# AJOUTER IMAGES DES ARTICLES{}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/add_objet')
def add_objet():
    
    return render_template("image.html")

@app.route('/add_objet', methods=['POST'])
def upload_image():
    try :
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        cheki1 = request.form.get("cheki1",'')
        print(cheki1)
        cheki2 = request.form.get("cheki2",'')
        print(cheki2)
        cheki3 = request.form.get("cheki3",'')
        print(cheki3)
        cheki4 = request.form.get("cheki4",'')
        print(cheki4)
        file = request.files['file']
        file1 = request.files['file1']
        file2 = request.files['file2']
        file3 = request.files['file3']
        print(file.filename)
        if file.filename == '' :
            flash('Aucune image sélectionnée pour le téléchargement')
            return redirect(request.url)
        if file1.filename == '' :
            flash('Aucune image sélectionnée pour le téléchargement')
            filename1 = 'vide'
        if file2.filename == '' :
            flash('Aucune image sélectionnée pour le téléchargement')
            filename2 = 'vide'
        if file3.filename == '' :
            flash('Aucune image sélectionnée pour le téléchargement')
            filename3 = 'vide'


        if file and allowed_file(file.filename):
            filenamea1 = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea1))
            #print('upload_image filename: ' + filename)
            flash('Image téléchargée avec succès et affichée ci-dessous')
            filename=file.filename
            # return render_template('boutique.html', filename=filename)
        if file1 and allowed_file(file1.filename):
            filenamea2 = secure_filename(file1.filename)
            file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea2))
            #print('upload_image filename: ' + filename)
            flash('Image téléchargée avec succès et affichée ci-dessous')
            filename1=file1.filename
            
            # return render_template('boutique.html', filename=filename)
        if file2 and allowed_file(file2.filename):
            filenamea3 = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea3))
            #print('upload_image filename: ' + filename)
            filename2=file2.filename
            flash('Image téléchargée avec succès et affichée ci-dessous')

            # return render_template('boutique.html', filename=filename)
        if file3 and allowed_file(file3.filename):
            filenamea4 = secure_filename(file3.filename)
            file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filenamea4))
            #print('upload_image filename: ' + filename)
            filename3=file3.filename
            flash('Image téléchargée avec succès et affichée ci-dessous')
           
        print(f'premier{filename},deux{filename1},trois{filename2},quatre{filename3}')


        cheki1 = request.form.get("cheki1",'')
        print(cheki1)
        cheki2 = request.form.get("cheki2",'')
        print(cheki2)
        cheki3 = request.form.get("cheki3",'')
        print(cheki3)
        cheki4 = request.form.get("cheki4",'')
        print(cheki4)

        if cheki1 != '' :
            return render_template('boutique.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3)
        elif cheki2 != '' or cheki3 != '':
            return render_template('ajchausee.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3)
        elif cheki4 != '':
            return render_template('ajmontre.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3)
        # return render_template('boutique.html', filename1=filename1 , filename=filename ,filename2=filename2 , filename3=filename3)
            # return render_template('boutique.html', filename=filename)
        # if not file and not allowed_file(file.filename) :
        #     return render_template('boutique.html', filename=filename , filename1=file1.filename ,filename2=file2.filename , filename3=file3.filename)
        # if not file2 and not allowed_file(file2.filename) :
        #     return render_template('boutique.html', filename2=filename2 , filename1=file1.filename ,filename=file.filename , filename3=file3.filename)
        # if not file3 and not allowed_file(file3.filename) :
        #     return render_template('boutique.html', filename3=filename3 , filename1=file1.filename ,filename2=file2.filename , filename=file.filename)
        # if not file1 and not allowed_file(file1.filename) :
        #     return render_template('boutique.html', filename1=filename1 , filename=file.filename ,filename2=file2.filename , filename3=file3.filename)
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
        porce = request.form.get("porce","0")
        porceprix = str(int(int(prix)-(int(prix) * (int(porce)/100))))
        image = request.form.get("image")      
        categorie = request.form.get('categorie')
        twoimage = request.form.get('twoimage')
        threeimage = request.form.get('threeimage')
        forimage = request.form.get('forimage')
        xs = request.form.get("xs","rien")
        s = request.form.get("s","rien")
        m = request.form.get("m","rien")
        l = request.form.get("l","rien")
        xl = request.form.get("xl","rien")
        xxl = request.form.get("xxl","rien")
        rouge = request.form.get("rouge","rien")
        blanc = request.form.get("blanc","rien")
        noir = request.form.get("noir","rien")
        jaune = request.form.get("jaune","rien")
        vert = request.form.get("vert","rien")
        orange = request.form.get("orange","rien")
        bleu = request.form.get("bleu","rien")
        rose = request.form.get("rose","rien")
        marron = request.form.get("marron","rien")
        violet = request.form.get("violet","rien")
        gris = request.form.get("gris","rien")
        tranwite = request.form.get("tranwite","rien")
        tranneuf = request.form.get("tranneuf","rien")
        karente = request.form.get("karente","rien")
        tranwiteun = request.form.get("tranwiteun","rien")
        tranwitedeux = request.form.get("tranwitedeux","rien")
        tranwitrois = request.form.get("tranwitrois","rien")
        tranwitekate = request.form.get("tranwitekate","rien")
        


        pani = Ajouter(nom=nom,description=description,prix=prix,porceprix=porceprix,porce=porce,categorie=categorie,image=image,twoimage=twoimage,threeimage=threeimage,forimage=forimage,xs=xs,s=s,l=l,m=m,xl=xl,xxl=xxl,rouge=rouge,blanc=blanc,noir=noir,jaune=jaune,vert=vert,orange=orange,bleu=bleu,rose=rose,marron=marron,violet=violet,gris=gris,tranwite=tranwite,tranneuf=tranneuf,karente=karente,tranwiteun=tranwiteun,tranwitedeux=tranwitedeux,tranwitrois=tranwitrois,tranwitekate=tranwitekate)
        # pani = Panier(nom = nom, description = description , prix = prix)
        
        db.session.add(pani)
        db.session.commit()
             
        
        return redirect("/")
    except :
        print(nom,'1',description,'2',image,'3',categorie,'4',twoimage,
        '5',threeimage
        ,'6',forimage
        ,'7',xs
        ,'8',s
        ,'9',m
        ,'10',l
        ,'11',xl
        ,'12',xxl
        ,'13',rouge
        ,'14',blanc
        ,'15',noir
        ,'16',jaune
        ,'17',vert
        ,'18',orange
        ,'19',bleu
        ,'20',rose
        ,'21',marron
        ,'22',violet
        ,'23',gris
        ,'24',tranwite
        ,'25',tranneuf
        ,'26',karente
        ,'27',tranwiteun
        ,'28',tranwitedeux
        ,'29',tranwitrois
        ,'30',tranwitekate)
        return render_template("boutique.html")
@app.route('/sacs/<int:id>')
def sacs(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect(f'/pre/sac')
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    conueww = len(gdhsuud) 
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "chaussure" :
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]
 



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('sacinfo.html',user = user,data=data,commenta=commenta,conueww=conueww)
    print("MO")

    return redirect("/sac")
    
@app.route("/sac")
def sac():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre/sac')
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'chaussure':
            data.append(i)
    

    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    conueww = len(gdhsuud)    
    somme = 0     
    for i in gdhsuud :
        somme += int(i["pource"])  
    return render_template("sac.html", data = data ,conueww=conueww,somme=somme)
@app.route('/homme/<int:id>')
def homme(id):
    
    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementHomme" :
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]
 


    
    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('hommeinfo.html',user = user,data=data,commenta=commenta)
    print("MO")

    return redirect("/hommes")
    
   
@app.route("/hommes")
def hommes():

    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementHomme':
            data.append(i)
    
    return render_template("/homme.html", data = data)
@app.route("/vente")
def acc():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre/vente')
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementFemme':
            data.append(i)

    
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    conueww = len(gdhsuud)    
    somme = 0     
    for i in gdhsuud :
        somme += int(i["pource"])  
    return render_template("vente.html", data = data , conueww=conueww,somme=somme)
@app.route("/montre")
def montre():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/montrels')
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'Montre':
            data.append(i)
    

    
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    conueww = len(gdhsuud)  
    somme = 0     
    for i in gdhsuud :
        somme += int(i["pource"])  
    return render_template("montre.html", data = data,conueww=conueww,somme=somme)
@app.route("/montrels")
def montrels():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'Montre':
            data.append(i)
    

    return render_template("montrels.html", data = data)
   

@app.route('/mesrecherches',methods = ["POST"])
def rechepo():
    recherches = {
        'montres': '/montre',
        'montre': '/montre',
        'robes': '/vente',
        'robe': '/vente',
        'habit femme': '/vente',
        'femmes': '/vente',
        'femme': '/vente',
        'chaussures': '/sac',
        'chaussure': '/sac',
        'chaussures femmes': '/sac',
        'chaussure femmes': '/sac',
        'chaussures femme': '/sac',
        'chaussure femme': '/sac'
    }

    recher = request.form.get('recher', '').lower()
    redirection = recherches.get(recher)

    if redirection:
        return redirect(redirection)
    else:
        return redirect('/indisponible')

    # recher = request.form.get('recher')
    # if recher.lower() == 'montres' or recher.lower() == 'montre' :
    #     return redirect('/montre')
    # if recher.lower() == 'robe' or recher.lower() == 'robes' or recher.lower() == 'habit femme' or recher.lower() == 'femmes' or recher.lower() == 'femme':
    #     return redirect('/vente')
    # if recher.lower() == 'chaussures' or recher.lower() == 'chaussure' or recher.lower() == 'chaussures femmes' or recher.lower() == 'chaussure femmes' or recher.lower() == 'chaussures femme' or recher.lower() == 'chaussure femme':
    #     return redirect('/sac')
    # return redirect('/indisponible')
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
    return render_template("ajoufini.html")
import json
@app.route('/montres/<int:id>')
def montres(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else :
        return redirect(f'/pre/montre')
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    conueww = len(gdhsuud)   



    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "Montre" :
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]




    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('montrederail.html',user = user,data=data,commenta=commenta,conueww=conueww)
    print("MO")

    return redirect("/montre")
  
    


@app.route('/montredetls/<int:id>')
def montredetls(id):
    
    # useruo = Profil.query.get(useru.id)
    # tableaus = Panieruser.query.all()
    # gdhsuud = []
    
    # for i in tableaus : 
        
    #     if int(i.identifiant) == useruo.id :
    #         print('prevdg', i.identifiant , 'prevdg' , useruo.id)
    #         hdhdud = Ajouter.query.get(i.produite)
    #         gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    # conueww = len(gdhsuud)   



    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "Montre" :
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]
 



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('montredetls.html',user = user,data=data,commenta=commenta)
    print("MO")

    return redirect("/montrels")

    
@app.route('/info/<int:id>')
def info(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        
        return redirect(f'/pre/vente')
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})

    conueww = len(gdhsuud) 
    

    commenta = []
    recupe = Ajouter.query.all()
    
    for i in recupe:
        if i.categorie == "VetementFemme" :
            commenta.append(i)

    if len(commenta)>10 :
        commenta = commenta[:10]
 



    
    user = Ajouter.query.filter_by(id=id).first()
    if user :
        data = [user.image,user.twoimage,user.threeimage,user.forimage]
        # a = Ajouter.query.all()
        # for i in a:
        #     if i.categorie == 'VetementFemme':
        #         data.append(i)
        return render_template('info.html',user = user,data=data,commenta=commenta , useru=useru,conueww=conueww)
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

@app.route('/commandeznow', methods=["POST"])
def commandeznow():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    else:
        return redirect('/pre/monpanier')
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    gdhsuud = []
    macommande = []
    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            if hdhdud.categorie == 'VetementFemme' :
                macommande.append({"lien":f"Le lien : https://hington-shop.onrender.com/info/{i.produite} ","Categorie":hdhdud.categorie,"Nom":hdhdud.nom,"Reduction":hdhdud.porce,"Prixbarré":hdhdud.prix,"Prix final":hdhdud.porceprix,"Quantité":i.quantiteto,"taille":i.tailed})
            if hdhdud.categorie == 'Montre' :
                macommande.append({"lien":f"Le lien : https://hington-shop.onrender.com/montres/{i.produite} ","Categorie":hdhdud.categorie,"Nom":hdhdud.nom,"Reduction":hdhdud.porce,"Prixbarré":hdhdud.prix,"Prix final":hdhdud.porceprix,"Quantité":i.quantiteto})
            if hdhdud.categorie == 'chaussure' :
                macommande.append({"lien":f"Le lien : https://hington-shop.onrender.com/sacs/{i.produite} ","Categorie":hdhdud.categorie,"Nom":hdhdud.nom,"Reduction":hdhdud.porce,"Prixbarré":hdhdud.prix,"Prix final":hdhdud.porceprix,"Quantité":i.quantiteto,"taille":i.tailed})

    somme = 0
    
    for i in macommande :
        print(int(i["Prix final"]))
        print(i["Prix final"])
        somme += int(i["Prix final"])
    
    macommande.append({"Somme totale" : somme})


    ms = macommande
    tableauser = Adminit.query.all()
    pani = Panieruser(nom="nom",numero = "numero",tags=ms)
            
    db.session.add(tableauser)
    db.session.commit()
    
    return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")
  
[{'lien': 'Le lien : https://hington-shop.onrender.com/info/9 ', 'Categorie': 'VetementFemme', 'Nom': 'robe simple', 'Reduction': '48', 'Prixbarré': '2500', 'Prix final': '1300', 'Quantité': '2', 'taille': 's'}, {'lien': 'Le lien : https://hington-shop.onrender.com/info/9 ', 'Categorie': 'VetementFemme', 'Nom': 'robe simple', 'Reduction': '48', 'Prixbarré': '2500', 'Prix final': '1300', 'Quantité': '2', 'taille': 'xxl'}, {'Somme totale': 2600}]




@app.route('/Supprimer/<int:id>')
def Supprimer(id):
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    # else:
    #     return redirect(f'/pre/Supprimer/{id}')
    
    useruo = Profil.query.get(useru.id)
    tableaus = Panieruser.query.all()
    
    ior =0
    for i in tableaus : 
        ior+=1
        print('produit,',ior)
        if int(i.identifiant) == useruo.id :
            user = Panieruser.query.filter_by(produite = id, identifiant = useruo.id).first()
            zerre = Panieruser.query.get(id)
            db.session.delete(zerre)
            db.session.commit()
            return redirect('/monpanier')
            print('produit supprimer')

    print('NON supprimer')  
    return redirect('/monpanier')


from urllib.parse import quote
@app.route('/ssm', methods=["POST"])
def ssm():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
    # else :
    #     return redirect('/pre/')
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    image = request.form.get("image")
    noumeme = request.form.get("noumeme")
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplos")
    hfshggf = Ajouter.query.get(int(noumeme))
    print("le voivi gegeghhdhjhdjhdjh",noumeme)
    
  

        


        

    # eudeyyt = Profil.query.all()
    if hfshggf.categorie == "Montre":
        print("les identifiants articles ",image,noumeme,prix,quantite)
        print("les identifiants  ",noumeme,useru.id)
        
        # derst = Panieruser.query.filter_by(identifiant=useru.id,produite=int(noumeme))
        derst = Panieruser.query.all()
        for i in derst :
            
            if int(i.produite) == int(noumeme) and int(i.identifiant)==int(useru.id):
                print("les articles ",i.produite,i.identifiant)
                dhher = Panieruser.query.get(i.id)

               
                dhher.quantiteto = int(dhher.quantiteto) + int(quantite)
                db.session.commit()
                return redirect("/monpanier")

        pani = Panieruser(image=image,tailed = "",identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=quantite,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
            
        db.session.add(pani)
        db.session.commit()
        return redirect("/monpanier")


    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) > 0 :
        xs = "xs"
        
        pani = Panieruser(image=image,tailed =xs,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=xsnum,xs=xs,xsn=xsnum,s="",sn=snum,l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""


    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) > 0 :
        s = "s"
        
        pani = Panieruser(image=image,tailed =s,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=snum,xs="",xsn="",s=s,sn=snum,l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) > 0 :
        m = "m"
        
        pani = Panieruser(image=image,tailed =m,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=mnum,xs="",xsn="",s="",sn="",l="",ln="",m=m,mn=mnum,xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) > 0 :
        l = "l"
        
        pani = Panieruser(image=image,tailed =l,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=lnum,xs="",xsn="",s="",sn="",l=l,ln=lnum,m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) > 0 :
        xl = "xl"
        
        pani = Panieruser(image=image, tailed = xl,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=xlnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl=xl,xln=xlnum,xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) > 0 :
        xxl = "xxl"
        
        pani = Panieruser(image=image, tailed = xxl,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=xxlnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl=xxl,xxln=xxlnum,tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(xxlnum) == 0 :
        xxl = ""
        xxlnum = ""

    
    # rouge = request.form.get("rouge","")
    # blanc = request.form.get("blanc","")
    # noir = request.form.get("noir","")
    # jaune = request.form.get("jaune","")
    # vert = request.form.get("vert","")
    # orange = request.form.get("orange","")
    # bleu = request.form.get("bleu","")
    # rose = request.form.get("rose","")
    # marron = request.form.get("marron","")
    # violet = request.form.get("violet","")
    # gris = request.form.get("gris","")
    tranwite = request.form.get("tranwite","")
    tranwitenum = request.form.get("tranwitenum","0")
    if int(tranwitenum) > 0 :
        tranwite = "38 -> "
        tranwitenum = tranwitenum
        
        pani = Panieruser(image=image,tailed = tranwite,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitenum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite=tranwite,tranwiten=tranwitenum,tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
    
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) > 0 :
        tranneuf = "39 -> "
        tranneufnum = tranneufnum
        
        pani = Panieruser(image=image,tailed = tranneuf,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranneufnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf=tranneuf,tranneufn=tranneufnum,karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) > 0 :
        karente = "40 -> "
        karentenum = karentenum
        
        pani = Panieruser(image=image,tailed = karente,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=karentenum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente=karente,karenten=karentenum,tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) > 0 :
        tranwiteun = "41 -> "
        tranwiteunnum = tranwiteunnum
        
        pani = Panieruser(image=image,tailed =tranwiteun ,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwiteunnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun=tranwiteun,tranwiteunn=tranwiteunnum,tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) > 0 :
        tranwitedeux = "42 -> "
        tranwitedeuxnum = tranwitedeuxnum
        
        pani = Panieruser(image=image,tailed = tranwitedeux ,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitedeuxnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux=tranwitedeux,tranwitedeuxn=tranwitedeuxnum,tranwitrois="",tranwitroisn="",tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) > 0 :
        tranwitrois = "43 -> "
        tranwitroisnum = tranwitroisnum
        
        pani = Panieruser(image=image,tailed = tranwitrois,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitroisnum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois=tranwitrois,tranwitroisn=tranwitroisnum,tranwitekate="",tranwitekaten="")
        
        db.session.add(pani)
        db.session.commit()
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) > 0 :
        tranwitekate = "44 -> "
        tranwitekatenum = tranwitekatenum
        
        pani = Panieruser(image=image,tailed = tranwitekate,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=tranwitekatenum,xs="",xsn="",s="",sn="",l="",ln="",m="",mn="",xl="",xln="",xxl="",xxln="",tranwite="",tranwiten="",tranneuf="",tranneufn="",karente="",karenten="",tranwiteun="",tranwiteunn="",tranwitedeux="",tranwitedeuxn="",tranwitrois="",tranwitroisn="",tranwitekate=tranwitekate,tranwitekaten=tranwitekatenum)
        
        db.session.add(pani)
        db.session.commit()
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
    
    

    # pani = Panieruser(image=image,identifiant=useru.id,produite=noumeme,prixtottal=prix,quantiteto=quantite,xs=xs,xsn=xsnum,s=s,sn=snum,l=l,ln=lnum,m=m,mn=mnum,xl=xl,xln=xlnum,xxl=xxl,xxln=xxlnum,tranwite=tranwite,tranwiten=tranwitenum,tranneuf=tranneuf,tranneufn=tranneufnum,karente=karente,karenten=karentenum,tranwiteun=tranwiteun,tranwiteunn=tranwiteunnum,tranwitedeux=tranwitedeux,tranwitedeuxn=tranwitedeuxnum,tranwitrois=tranwitrois,tranwitroisn=tranwitroisnum,tranwitekate=tranwitekate,tranwitekaten=tranwitekatenum)
        
    # db.session.add(pani)
    # db.session.commit()

    # tou = Ajouter.query.get(id)
    # import urllib.parse
    
    # if tou.categorie == 'VetementFemme' :
    #     quantite = quantite
    #     if int(quantite) < 1 :
    #         flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
    #         return redirect(f'/info/{id}#formuhfh1')
    
    #     ms = f"Le lien : https://hington-shop.onrender.com/info/{a} , Quantite = {quantite} , Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero} , Taille = {xs}{xsnum} {s}{snum} {l}{lnum} {m}{mnum} {xxl}{xxlnum} {xl}{xlnum} "
        
    #     return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")

    # if tou.categorie == 'chaussure' :
    #     quantite = quantite
    #     if int(quantite) < 1 :
    #         flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
    #         return redirect(f'/sacs/{id}#formuhfh1')
    #     ms = f"Le lien : https://hington-shop.onrender.com/sacs/{a} , Quantite = {quantite} , Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero} , Taille = {tranwite}{tranwitenum} {tranneuf}{tranneufnum} {karente}{karentenum} {tranwiteun}{tranwiteunnum} {tranwitedeux}{tranwitedeuxnum} {tranwitrois}{tranwitroisnum} {tranwitekate}{tranwitekatenum} "

    #     return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")
    
    # if tou.categorie == 'Montre' :
    #     quantite = quantite
    #     if int(quantite) < 1 :
    #         flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
    #         return redirect(f'/montres/{id}#formuhfh1')
    #     ms = f"Le lien : https://hington-shop.onrender.com/montres/{a} , Quantite = {quantite} ,Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero}  "
        

    #     return redirect(f"https://api.whatsapp.com/send/?phone=2250101678809&text={ms}&type=phone_number&app_absent=0")

    # ms_encoded = urllib.parse.quote(ms)
    # print(ms)
    # print(ms_encoded)

    # Encode the message string before passing it to the quote function
    # encoded_message = ms.encode('utf-8')
    # pywhatkit.sendwhats_image("+2250787022061", "bonjou", formatted_time, 45)
    # pywhatkit.sendwhats_image("+2250787022061", "https://web.whatsapp.com/send?phone=+22578587708&text={ms}", formatted_time, formatted)
    # return redirect(f"https://web.whatsapp.com/send?phone=+22578587708&text={ms}")
    # return redirect("/vente")
    

    # 
    return redirect("/monpanier")

        
    

    

# @app.route('/dataze', methods=["POST"])
# def dataze():
#     data = {"image":"image","tailed" : "","produite":"noumeme","prixtottal":"prix","quantiteto":"quantite","xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
#     des = {"image":"image","tailed" : "","dee":"fggh"}    
#     print(data)
#     return des
@app.route('/ssme', methods=["POST"])
def ssme():
    
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    image = request.form.get("image")
    noumeme = request.form.get("noumeme")
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplos")

        # eudeyyt = Profil.query.all()
    if 1==1:
        
        print("les identifiants articles non connecter",image,noumeme,prix,quantite)
    
        data = {"image":image,"tailed" : "","produite":noumeme,"prixtottal":prix,"quantiteto":quantite,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
            
        print(data)
        detr = {
            "image": "pho1.jpg",
            "karente": "",
            "karenten": "",
            "l": "",
            "ln": "",
            "m": "",
            "mn": "",
            "prixtottal": "4800",
            "produite": "1",
            "quantiteto": "3",
            "s": "",
            "sn": "",
            "tailed": "",
            "tranneuf": "",
            "tranneufn": "",
            "tranwite": "",
            "tranwitedeux": "",
            "tranwitedeuxn": "",
            "tranwitekate": "",
            "tranwitekaten": "",
            "tranwiten": "",
            "tranwiteun": "",
            "tranwiteunn": "",
            "tranwitrois": "",
            "tranwitroisn": "",
            "xl": "",
            "xln": "",
            "xs": "",
            "xsn": "",
            "xxl": "",
            "xxln": ""
            }
        return data


    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) > 0 :
        xs = "xs"
        
        data = {"image":image,"tailed" :xs,"produite":noumeme,"prixtottal":prix,"quantiteto":xsnum,"xs":xs,"xsn":xsnum,"s":"","sn":snum,"l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""


    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) > 0 :
        s = "s"
        
        data = {"image":image,"tailed" :s,"produite":noumeme,"prixtottal":prix,"quantiteto":snum,"xs":"","xsn":"","s":s,"sn":snum,"l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) > 0 :
        m = "m"
        
        data = {"image":image,"tailed" :m,"produite":noumeme,"prixtottal":prix,"quantiteto":mnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":m,"mn":mnum,"xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) > 0 :
        l = "l"
        
        data = {"image":image,"tailed" :l,"produite":noumeme,"prixtottal":prix,"quantiteto":lnum,"xs":"","xsn":"","s":"","sn":"","l":l,"ln":lnum,"m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) > 0 :
        xl = "xl"
        
        data = {"image":image, "tailed" : xl,"produite":noumeme,"prixtottal":prix,"quantiteto":xlnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":xl,"xln":xlnum,"xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) > 0 :
        xxl = "xxl"
        
        data = {"image":image, "tailed" : xxl,"produite":noumeme,"prixtottal":prix,"quantiteto":xxlnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":xxl,"xxln":xxlnum,"tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(xxlnum) == 0 :
        xxl = ""
        xxlnum = ""

    tranwite = request.form.get("tranwite","")
    tranwitenum = request.form.get("tranwitenum","0")
    if int(tranwitenum) > 0 :
        tranwite = "38 -> "
        tranwitenum = tranwitenum
        
        data = {"image":image,"tailed" : tranwite,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitenum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":tranwite,"tranwiten":tranwitenum,"tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
    
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) > 0 :
        tranneuf = "39 -> "
        tranneufnum = tranneufnum
        
        data = {"image":image,"tailed" : tranneuf,"produite":noumeme,"prixtottal":prix,"quantiteto":tranneufnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":tranneuf,"tranneufn":tranneufnum,"karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) > 0 :
        karente = "40 -> "
        karentenum = karentenum
        
        data = {"image":image,"tailed" : karente,"produite":noumeme,"prixtottal":prix,"quantiteto":karentenum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":karente,"karenten":karentenum,"tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) > 0 :
        tranwiteun = "41 -> "
        tranwiteunnum = tranwiteunnum
        
        data = {"image":image,"tailed" :tranwiteun ,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwiteunnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":tranwiteun,"tranwiteunn":tranwiteunnum,"tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) > 0 :
        tranwitedeux = "42 -> "
        tranwitedeuxnum = tranwitedeuxnum
        
        data = {"image":image,"tailed" : tranwitedeux ,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitedeuxnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":tranwitedeux,"tranwitedeuxn":tranwitedeuxnum,"tranwitrois":"","tranwitroisn":"","tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) > 0 :
        tranwitrois = "43 -> "
        tranwitroisnum = tranwitroisnum
        
        data = {"image":image,"tailed" : tranwitrois,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitroisnum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":tranwitrois,"tranwitroisn":tranwitroisnum,"tranwitekate":"","tranwitekaten":""}
        print(data)
        return data
        
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) > 0 :
        tranwitekate = "44 -> "
        tranwitekatenum = tranwitekatenum
        
        data = {"image":image,"tailed" : tranwitekate,"produite":noumeme,"prixtottal":prix,"quantiteto":tranwitekatenum,"xs":"","xsn":"","s":"","sn":"","l":"","ln":"","m":"","mn":"","xl":"","xln":"","xxl":"","xxln":"","tranwite":"","tranwiten":"","tranneuf":"","tranneufn":"","karente":"","karenten":"","tranwiteun":"","tranwiteunn":"","tranwitedeux":"","tranwitedeuxn":"","tranwitrois":"","tranwitroisn":"","tranwitekate":tranwitekate,"tranwitekaten":tranwitekatenum}
        print(data)
        return data
        
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
    # sizes = ["xs", "s", "m", "l", "xl", "xxl", "tranwite", "tranneuf", "karente", "tranwiteun", "tranwitedeux", "tranwitrois", "tranwitekate"]
    # size_suffixes = {"tranwite": "38 -> ", "tranneuf": "39 -> ", "karente": "40 -> ", "tranwiteun": "41 -> ", "tranwitedeux": "42 -> ", "tranwitrois": "43 -> ", "tranwitekate": "44 -> "}
    
    # image = request.form.get("image", "")
    # noumeme = request.form.get("noumeme", "")
    # prix = request.form.get("prix", "")
    
    # for size in sizes:
    #     num_key = f"{size}num"
    #     size_value = request.form.get(size, "")
    #     num_value = request.form.get(num_key, "0")
        
    #     if int(num_value) > 0:
    #         tailed = size_suffixes.get(size, size)
    #         data = {
    #             "image": image,
    #             "tailed": tailed,
    #             "produite": noumeme,
    #             "prixtottal": prix,
    #             "quantiteto": num_value,
    #             "xs": "",
    #             "xsn": "",
    #             "s": "",
    #             "sn": "",
    #             "l": "",
    #             "ln": "",
    #             "m": "",
    #             "mn": "",
    #             "xl": "",
    #             "xln": "",
    #             "xxl": "",
    #             "xxln": "",
    #             "tranwite": "",
    #             "tranwiten": "",
    #             "tranneuf": "",
    #             "tranneufn": "",
    #             "karente": "",
    #             "karenten": "",
    #             "tranwiteun": "",
    #             "tranwiteunn": "",
    #             "tranwitedeux": "",
    #             "tranwitedeuxn": "",
    #             "tranwitrois": "",
    #             "tranwitroisn": "",
    #             "tranwitekate": "",
    #             "tranwitekaten": ""
    #         }
    #         data[size] = tailed
    #         data[num_key] = num_value
    #         print(data)
    #         return data
    
    return redirect("/monpanierls")

    


@app.route("/administa")
def administa():
    try :
        administa = Ajouter.query.all()
        pofil = Profil.query.all()
        VetementHomme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementHomme':
                VetementHomme.append(i)
        VetementFemme = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'VetementFemme':
                VetementFemme.append(i)
        Montre = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'Montre':
                Montre.append(i)
        sac = []
        a = Ajouter.query.all()
        for i in a:
            if i.categorie == 'chaussure':
                sac.append(i)

        return render_template("administa.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac,pofil=pofil)

    except :
        return render_template("administa.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac)

@app.route("/indisponible")
def indisponible():

    return render_template("indiso.html")


# @app.route("/pacceuil",methods=["POST","GET"])
# def pacceuil():
#     if 'utilisateur_id' in session:
#         useru = Profil.query.get(session['utilisateur_id'])
#         data = request.get_json()
#         print(data)
#         pani = Panieruser(image=data.image,tailed =data.tailed,identifiant=useru.id,produite=data.produite,prixtottal=data.prixtottal,quantiteto=data.quantiteto,xs=data.xs,xsn=data.xsn,s=data.s,sn=data.sn,l=data.l,ln=data.ln,m=data.m,mn=data.mn,xl=data.xl,xln=data.xln,xxl=data.xxl,xxln=data.xxln,tranwite=data.tranwite,tranwiten=data.tranwiten,tranneuf=data.tranneuf,tranneufn=data.tranneufn,karente=data.karente,karenten=data.karenten,tranwiteun=data.tranwiteun,tranwiteunn=data.tranwiteunn,tranwitedeux=data.tranwitedeux,tranwitedeuxn=data.tranwitedeuxn,tranwitrois=data.tranwitrois,tranwitroisn=data.tranwitroisn,tranwitekate=data.tranwitekate,tranwitekaten=data.tranwitekaten)
            
#         db.session.add(pani)
#         db.session.commit()

        
#         return redirect("/")
#     return redirect("/pre")



# CONNEXION {}
@app.route('/pre/<routeure>')
def pree(routeure):
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    # print(commenta[0].mail)
    
    return render_template("connexion.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure,routeure=routeure)

    # return render_template('connexion.html')
@app.route('/sprome/<routeure>',methods = ["GET","POST"])
def sprome(routeure) :
   
    user = Profil.query.filter_by(last_name = request.form.get("last_name"),age = request.form.get("age")).first()

    if user :
        
      
        
        print(f"vous etes connecter{user.first_name}{user.id}")
        

        session['utilisateur_id'] = user.id
        # return redirect('/pacceuil')
        return redirect(f"/rediriger/{routeure}")

    else :

        flash("Email ou Mot de passe invalide")
        return redirect(f"/pre/{routeure}")
    
    
@app.route('/dedyiez/<routeure>',methods = ["GET","POST"])
def dedyiez(routeure) :
   
    return redirect(f"{routeure}")
    
    


# @app.route('/song',methods = ["GET","POST"])
# def song() :
   
#     return {"nom": "cabri","prenom":"mamoud"}


# FIN CONNEXION {}


@app.route("/deconn")
def deconn():
    if 'utilisateur_id' in session:
       
        session.pop('utilisateur_id', None)
        return redirect("/pre/deconn")
    return redirect("/")

@app.route("/rediriger/<routeure>")
def rediriger(routeure):
 
    return render_template("rediriger.html",routeure=routeure)
@app.route("/redsete", methods=["POST"])
def redsete():
    data = request.get_json()['data']
    print("voivi les ",data)
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        print("je suis llllllll")
        for i in data:
            
            b = i["data"]
            pani = Panieruser(
                image=b['image'],
                tailed=b['tailed'],
                identifiant=useru.id,
                produite=b['produite'],
                prixtottal=b['prixtottal'],
                quantiteto=b['quantiteto'],
                xs=b['xs'],
                xsn=b['xsn'],
                s=b['s'],
                sn=b['sn'],
                l=b['l'],
                ln=b['ln'],
                m=b['m'],
                mn=b['mn'],
                xl=b['xl'],
                xln=b['xln'],
                xxl=b['xxl'],
                xxln=b['xxln'],
                tranwite=b['tranwite'],
                tranwiten=b['tranwiten'],
                tranneuf=b['tranneuf'],
                tranneufn=b['tranneufn'],
                karente=b['karente'],
                karenten=b['karenten'],
                tranwiteun=b['tranwiteun'],
                tranwiteunn=b['tranwiteunn'],
                tranwitedeux=b['tranwitedeux'],
                tranwitedeuxn=b['tranwitedeuxn'],
                tranwitrois=b['tranwitrois'],
                tranwitroisn=b['tranwitroisn'],
                tranwitekate=b['tranwitekate'],
                tranwitekaten=b['tranwitekaten']
            )

            derst = Panieruser.query.all()
            crte = 0
            for p in derst :
                
                if int(p.produite) == int(b['produite']) and int(p.identifiant)==int(useru.id):

                    print("fghger",int(p.produite),"==",int(b['produite']))
                    print("hger",int(p.identifiant),"==",int(int(useru.id)))

                    crte +=1
                    dhher = Panieruser.query.get(p.id)

                
                    dhher.quantiteto = int(dhher.quantiteto) + int(b['produite'])
                    db.session.commit()
            if crte == 0 :
                print("on passe")
                 
                db.session.add(pani)
                db.session.commit()
        
    return {"message":"enregistrement reussi"}



@app.route("/pacceuil", methods=["POST"])
def pacceuil():
    print("je suis la 2")
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        print("je suis la 1")
        # if request.method == 'POST':
        #     data = request.get_json()['data']
        #     for i in data:
        #         pani = Panieruser(
        #             image=data['image'],
        #             tailed=data['tailed'],
        #             identifiant=useru.id,
        #             produite=data['produite'],
        #             prixtottal=data['prixtottal'],
        #             quantiteto=data['quantiteto'],
        #             xs=data['xs'],
        #             xsn=data['xsn'],
        #             s=data['s'],
        #             sn=data['sn'],
        #             l=data['l'],
        #             ln=data['ln'],
        #             m=data['m'],
        #             mn=data['mn'],
        #             xl=data['xl'],
        #             xln=data['xln'],
        #             xxl=data['xxl'],
        #             xxln=data['xxln'],
        #             tranwite=data['tranwite'],
        #             tranwiten=data['tranwiten'],
        #             tranneuf=data['tranneuf'],
        #             tranneufn=data['tranneufn'],
        #             karente=data['karente'],
        #             karenten=data['karenten'],
        #             tranwiteun=data['tranwiteun'],
        #             tranwiteunn=data['tranwiteunn'],
        #             tranwitedeux=data['tranwitedeux'],
        #             tranwitedeuxn=data['tranwitedeuxn'],
        #             tranwitrois=data['tranwitrois'],
        #             tranwitroisn=data['tranwitroisn'],
        #             tranwitekate=data['tranwitekate'],
        #             tranwitekaten=data['tranwitekaten']
        #         )
        #         db.session.add(pani)
        #         db.session.commit()
        #     return jsonify({'status': 'success'}), 200
            
        return redirect("/")
    return redirect("/pre/acceuilconnect")

@app.route("/")
def acceuil():
    
   
    
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    print(commenta[0].mail)
    
    return render_template("acceuil.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure)
@app.route("/acceuilconnect")
def acceuilconnect():
    
   
    
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    print(commenta[0].mail)
    
    return render_template("acceuil.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure)


@app.route("/Suppesss/<int:id>")
def Suppesss(id):
    try :
        adm= Profil.query.get(id)
        db.session.delete(adm)
        db.session.commit()

        return redirect("/administa")
    
    except :

        return redirect("/administa")
@app.route("/Suppesz/<int:id>")
def Suppesz(id):
    try :
        adm= Ajouter.query.get(id)
        db.session.delete(adm)
        db.session.commit()
        
        wer1 = adm.image
        wer2 = adm.twoimage
        wer3 = adm.threeimage
        wer4 = adm.forimage
        chemin_image1 = os.path.join(app.config['UPLOAD_FOLDER'], wer1)
        chemin_image2 = os.path.join(app.config['UPLOAD_FOLDER'], wer2)
        chemin_image3 = os.path.join(app.config['UPLOAD_FOLDER'], wer3)
        chemin_image4 = os.path.join(app.config['UPLOAD_FOLDER'], wer4)

        # filename = secure_filename(file.filename)
        # file.save(os.path.join(, filename))
        os.remove(chemin_image1)
        os.remove(chemin_image2)
        os.remove(chemin_image3)
        os.remove(chemin_image4)

        return redirect("/administa")
    
    except :

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

@app.route('/monpanier')
def panierus():
    if 'utilisateur_id' in session:
        useru = Profil.query.get(session['utilisateur_id'])
        
    else:
        return redirect('/pre/monpanier')
    
    useruo = Profil.query.get(useru.id)
    eudeyyt = Profil.query.all()
    tableaus = Panieruser.query.all()
    catefemme = []
    montre = []
    gdhsuud = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    articeldd = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in eudeyyt:
        articeldd.append(i)

    
    for i in tableaus : 
        
        if int(i.identifiant) == useruo.id :
            print('prevdg', i.identifiant , 'prevdg' , useruo.id)
            hdhdud = Ajouter.query.get(i.produite)
            gdhsuud.append({"id":i.id,"element":i.produite,"prix":hdhdud.prix,"image":i.image,"quantite":i.quantiteto,"taille":i.tailed,"nom":hdhdud.nom,"description":hdhdud.description,"pource":hdhdud.porceprix,"porce":hdhdud.porce ,"tailed":i.tailed,"categorie":hdhdud.categorie})


    conueww = len(gdhsuud)    
    somme = 0     
    for i in gdhsuud :
        somme += int(i["pource"])*int(i["quantite"])
    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)
        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    print(commenta[0].mail)
    
    return render_template("panierus.html",gdhsuud=gdhsuud,commenta=commenta,catefemme=catefemme,montre=montre,id=id,chaussure=chaussure,somme=somme,conueww=conueww,useruo=useruo.id)
@app.route('/monpanierls')
def monpanierls():
    
    # data = request.get_json()
   
    # if not data:
    #     return jsonify({"error": "No data received"}), 400
    # print(data)  
    # return jsonify({"message": "Data received successfully", "data": data}), 200
    gdhsuud = "data"
    conueww = len(gdhsuud)  
    eudeyyt = Profil.query.all()
    
    catefemme = []
    montre = []
 
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    articeldd = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in eudeyyt:
        articeldd.append(i)

  
    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)
        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    print(commenta[0].mail)
    
    return render_template("panierls.html",commenta=commenta,conueww=conueww,gdhsuud=gdhsuud,catefemme=catefemme,montre=montre,chaussure=chaussure)

  
@app.route('/mofiedd/<int:id>')
def mofiedd(id):
    
    return render_template("modifier.html",id=id)
@app.route('/mofie/<int:id>',methods = ["POST"])
def mofie(id):

    reu = Ajouter.query.get(id)
    reu.xs = request.form.get("xs",'')
    reu.porce = request.form.get("porce",'')
    reu.prix = reu.prix
    reu.porceprix = str(int(int(reu.prix)-(int(reu.prix) * (int(reu.porce)/100))))
    reu.s = request.form.get("s",'')
    reu.m = request.form.get("m",'')
    reu.l = request.form.get("l",'')
    reu.xl = request.form.get("xl",'')
    reu.xxl = request.form.get("xxl",'')
    reu.rouge = request.form.get("rouge",'')
    reu.blanc = request.form.get("blanc",'')
    reu.noir = request.form.get("noir",'')
    reu.jaune = request.form.get("jaune",'')
    reu.vert = request.form.get("vert",'')
    reu.orange = request.form.get("orange",'')
    reu.bleu = request.form.get("bleu",'')
    reu.rose = request.form.get("rose",'')
    reu.marron = request.form.get("marron",'')
    reu.violet = request.form.get("violet",'')
    reu.gris = request.form.get("gris",'')
    reu.tranwite = request.form.get("tranwite",'')
    reu.tranneuf = request.form.get("tranneuf",'')
    reu.karente = request.form.get("karente",'')
    reu.tranwiteun = request.form.get("tranwiteun",'')
    reu.tranwitedeux = request.form.get("tranwitedeux",'')
    reu.tranwitrois = request.form.get("tranwitrois",'')
    reu.tranwitekate = request.form.get("tranwitekate",'')
    
    db.session.commit()
    return redirect('/administa')











@app.route('/add_data')
def add_data():
    catefemme = []
    montre = []
    chaussure = []
    tout = Ajouter.query.all()
    commenta = []
    recupe = Comment.query.all()
    
    for i in recupe:
        commenta.append(i)

    for i in tout:
        if i.categorie == "VetementFemme" :
            catefemme.append(i)

        if i.categorie == "Montre" :
            montre.append(i)

        if i.categorie == "chaussure" :
            chaussure.append(i)
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]
    if len(chaussure) >10 :
        chaussure = chaussure[:10]


    print(commenta[0].mail)
    
    return render_template("add_profile.html",commenta=commenta,catefemme=catefemme,montre=montre,chaussure=chaussure)

   

@app.route('/add',methods = ["POST"])
def profile() :
    
    
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    age = request.form.get("age")
    conf = request.form.get("conf")
    

    if conf != age :
        flash("Entrez le meme mot de passe")
        return redirect("/add_data")
    
    for i in range (len(last_name)) :
        if last_name[i] == "@" :

            if "moc.liamg" == last_name[:i:-1]:

                pass
            else :
                flash("Email ou Mot de passe invalide")
                return redirect("/add_data")
            



    user = Profil.query.filter_by(last_name = request.form.get("last_name")).first()
    if user :
        flash("Ce compte existe deja") 
        return redirect(url_for("add_data"))
    else :
        if first_name != " " and last_name != " " and age is not None and len(age)== 8 :
            p = Profil(first_name = first_name, last_name = last_name , age = age)

            db.session.add(p)
            db.session.commit()
            return redirect("/pre/acceuilconnect")
        else :
            return redirect("/add_data")
        
# FIN AJOUTER DES USER{} 









# @app.route('/receive_data', methods=['POST'])
# def receive_data():
#     data = request.json  # Receives JSON data sent from JavaScript
#     data_from_js = data['data']
    
#     # Now you can use data_from_js as needed in your Python application
#     print('Data received from JavaScript:', data_from_js)
    
#     # Optionally, you can send a response back to JavaScript
#     response = {'message': 'Data received successfully'}
#     return jsonify(response)





if __name__ == '__main__' :
    app.run(debug=True,port=5005)
