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
        return render_template('sacinfo.html',user = user,data=data,commenta=commenta)
    print("MO")

    return redirect("/sac")
    
@app.route("/sac")
def sac():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'chaussure':
            data.append(i)
    
    return render_template("sac.html", data = data)
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
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'VetementFemme':
            data.append(i)
    return render_template("vente.html", data = data)
@app.route("/montre")
def montre():
    data = []
    a = Ajouter.query.all()
    for i in a:
        if i.categorie == 'Montre':
            data.append(i)
    
    return render_template("montre.html", data = data)

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

@app.route('/montres/<int:id>')
def montres(id):
    
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
        return render_template('montrederail.html',user = user,data=data,commenta=commenta)
    print("MO")

    return redirect("/montre")

    
@app.route('/info/<int:id>')
def info(id):
    
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
        return render_template('info.html',user = user,data=data,commenta=commenta)
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
    xs = request.form.get("xs","")
    xsnum = request.form.get("xsnum","0")
    if int(xsnum) > 0 :
        xs = "xs"
    if int(xsnum) == 0 :
        xs = ""
        xsnum = ""

   
    s = request.form.get("s","")
    snum = request.form.get("snum","0")
    if int(snum) > 0 :
        s = "s"
    if int(snum) == 0 :
        s = ""
        snum = ""
    m = request.form.get("m","")
    mnum = request.form.get("mnum","0")
    if int(mnum) > 0 :
        m = "m"
    if int(mnum) == 0 :
        m = ""
        mnum = ""
    l = request.form.get("l","")
    lnum = request.form.get("lnum","0")
    if int(lnum) > 0 :
        l = "l"
    if int(lnum) == 0 :
        l = ""
        lnum = ""
    xl = request.form.get("xl","")
    xlnum = request.form.get("xlnum","0")
    if int(xlnum) > 0 :
        xl = "xl"
    if int(xlnum) == 0 :
        xl = ""
        xlnum = ""
    xxlnum = request.form.get("xxlnum","0")
    xxl = request.form.get("xxl","")
    if int(xxlnum) > 0 :
        xxl = "xxl"
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
    if int(tranwitenum) == 0 :
        tranwite = ""
        tranwitenum = ""
       
    tranneuf = request.form.get("tranneuf","")
    tranneufnum = request.form.get("tranneufnum","0")
    if int(tranneufnum) > 0 :
        tranneuf = "39 -> "
        tranneufnum = tranneufnum
    if int(tranneufnum) == 0 :
        tranneuf = ""
        tranneufnum = ""
    karente = request.form.get("karente","")
    karentenum = request.form.get("karentenum","0")
    if int(karentenum) > 0 :
        karente = "40 -> "
        karentenum = karentenum
    if int(karentenum) == 0 :
        karente = ""
        karentenum = ""
    tranwiteun = request.form.get("tranwiteun","")
    tranwiteunnum = request.form.get("tranwiteunnum","0")
    if int(tranwiteunnum) > 0 :
        tranwiteun = "41 -> "
        tranwiteunnum = tranwiteunnum
    if int(tranwiteunnum) == 0 :
        tranwiteun = ""
        tranwiteunnum = ""
    tranwitedeux = request.form.get("tranwitedeux","")
    tranwitedeuxnum = request.form.get("tranwitedeuxnum","0")
    if int(tranwitedeuxnum) > 0 :
        tranwitedeux = "42 -> "
        tranwitedeuxnum = tranwitedeuxnum
    if int(tranwitedeuxnum) == 0 :
        tranwitedeux = ""
        tranwitedeuxnum = ""
    tranwitrois = request.form.get("tranwitrois","")
    tranwitroisnum = request.form.get("tranwitroisnum","0")
    if int(tranwitroisnum) > 0 :
        tranwitrois = "43 -> "
        tranwitroisnum = tranwitroisnum
    if int(tranwitroisnum) == 0 :
        tranwitrois = ""
        tranwitroisnum = ""
    tranwitekate = request.form.get("tranwitekate","")
    tranwitekatenum = request.form.get("tranwitekatenum","0")
    if int(tranwitekatenum) > 0 :
        tranwitekate = "44 -> "
        tranwitekatenum = tranwitekatenum
    if int(tranwitekatenum) == 0 :
        tranwitekate = ""
        tranwitekatenum = ""
    
    nom = request.form.get("nom")
    livraison = request.form.get("livraison")
    numero = request.form.get("numero")
    prix = request.form.get("prix")
    quantite = request.form.get("quantiteplos")
    
    tou = Ajouter.query.get(id)
    import urllib.parse
    
    if tou.categorie == 'VetementFemme' :
        quantite = quantite
        if int(quantite) < 1 :
            flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
            return redirect(f'/info/{id}#formuhfh1')
      
        ms = f"Le lien : https://hington-shop.onrender.com/info/{a} , Quantite = {quantite} , Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero} , Taille = {xs}{xsnum} {s}{snum} {l}{lnum} {m}{mnum} {xxl}{xxlnum} {xl}{xlnum} "
        # ms_encoded = urllib.parse.quote(ms)
        # print(ms)
        # print(ms_encoded)
        return redirect(f"https://api.whatsapp.com/send/?phone=2250778587708&text={ms}&type=phone_number&app_absent=0")

    if tou.categorie == 'chaussure' :
        quantite = quantite
        if int(quantite) < 1 :
            flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
            return redirect(f'/sacs/{id}#formuhfh1')
        ms = f"Le lien : https://hington-shop.onrender.com/sacs/{a} , Quantite = {quantite} , Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero} , Taille = {tranwite}{tranwitenum} {tranneuf}{tranneufnum} {karente}{karentenum} {tranwiteun}{tranwiteunnum} {tranwitedeux}{tranwitedeuxnum} {tranwitrois}{tranwitroisnum} {tranwitekate}{tranwitekatenum} "

        return redirect(f"https://api.whatsapp.com/send/?phone=2250778587708&text={ms}&type=phone_number&app_absent=0")
    
    if tou.categorie == 'Montre' :
        quantite = quantite
        if int(quantite) < 1 :
            flash("Veuillez choisir la taille de l'article avant de commander svp ! ")
            return redirect(f'/montres/{id}#formuhfh1')
        ms = f"Le lien : https://hington-shop.onrender.com/montres/{a} , Quantite = {quantite} ,Prix = {int(quantite)*int(prix)} , Nom = {nom} , Livraison = {livraison} , Numero = {numero}  "
        

        return redirect(f"https://api.whatsapp.com/send/?phone=2250778587708&text={ms}&type=phone_number&app_absent=0")



    # Encode the message string before passing it to the quote function
    # encoded_message = ms.encode('utf-8')
    # pywhatkit.sendwhats_image("+2250787022061", "bonjou", formatted_time, 45)
    # pywhatkit.sendwhats_image("+2250787022061", "https://web.whatsapp.com/send?phone=+22578587708&text={ms}", formatted_time, formatted)
    # return redirect(f"https://web.whatsapp.com/send?phone=+22578587708&text={ms}")
    # return redirect("/vente")
    

    # 


@app.route("/administa")
def administa():
    try :
        administa = Ajouter.query.all()
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

        return render_template("administa.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac)

    except :
        return render_template("administa.html",administa=administa,VetementHomme=VetementHomme,VetementFemme=VetementFemme,Montre=Montre,sac=sac)

@app.route("/indisponible")
def indisponible():

    return render_template("indiso.html")

@app.route("/")
def acceuil():
    catefemme = []
    montre = []
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
    if len(catefemme)>10 :
        catefemme = catefemme[:10]
    if len(montre) >10 :
        montre = montre[:10]


    print(commenta[0].mail)
    
    return render_template("acceuil.html",commenta=commenta,catefemme=catefemme,montre=montre)


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


if __name__ == '__main__' :
    app.run(debug=True,port=5005)
