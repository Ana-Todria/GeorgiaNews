from flask import  render_template, redirect, request
from flask_login import login_user, logout_user, login_required
from forms import ProductForm, LoginForm, RegisterForm, ThingForm, NewForm, TourForm, InfoForm, DocForm, BakForm
from models import Product, User, Thing, New, Tour, Info, Doc, Bak


from ext import app, db


@app.route("/")
def index():
    return render_template("project.html")

@app.route("/search")
def search():
    name = request.args.get("n")
    products=Product.query.filter(Product.name== name).all()
    return render_template("girshesanishnaoba.html", products=products)

@app.route("/search2")
def search2():
    name = request.args.get("m")
    tours=Tour.query.filter(Tour.name== name).all()
    return render_template("მარშუტები.html", tours=tours)



@app.route("/girshesanishnaoba")
def girsh():
    products=Product.query.all()
    return render_template("girshesanishnaoba.html", products=products )


@app.route("/base")
def base():
    return render_template("base.html")




@app.route("/axali")
def axali():
    things = Thing.query.all()
    return render_template("axali ambebi.html", things=things)


@app.route("/axali2")
def axali2():
    news = New.query.all()
    return render_template("axali ambebi2.html", news=news)


@app.route("/meti")
def meti():
    docs=Doc.query.all()
    return render_template("meti inf.html", docs=docs)


@app.route("/საქართველო")
def საქართველო():
    return render_template("საქართველო.html")



@app.route("/project1")
def project1():
    return render_template("project 1.html")


@app.route("/კონტაქტი")
def kontacti():
    return render_template("კონტაქტი.html")


@app.route("/მარშუტები")
def marshutebi():
    tours = Tour.query.all()
    return render_template("მარშუტები.html", tours=tours)


@app.route("/სვეტმეტი")
def svetmeti():
    infos = Info.query.all()
    return render_template("სვეტმეტი.html", infos=infos)


@app.route("/ბაკურიანი")
def ბაკურიანი():
    baks=Bak.query.all()
    return render_template("ბაკურიანი.html", baks=baks)


@app.route("/create_product", methods=["GET", "POST"])
def create_product():
    form = ProductForm()

    if form.validate_on_submit():


        new_product = Product(name=form.name.data,
                              text=form.text.data,
                              img=form.img.data,
                              link=form.link.data,
                            )
        db.session.add(new_product)
        db.session.commit()
        return redirect("/girshesanishnaoba")





    return render_template("create_product.html", form=form)

@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])

def edit_product(product_id):

    product =Product.query.get(product_id)
    form = ProductForm(name=product.name, text=product.text, img=product.img)
    if form.validate_on_submit():
        product.name = form.name.data
        product.text = form.text.data
        product.img = form.img.data

        db.session.commit()
        return redirect("/girshesanishnaoba")
    return render_template("create_product.html", form=form)

@app.route("/delete_product/<int:product_id>", methods=["GET", "POST"])
def delete_product(product_id):
    product= Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/girshesanishnaoba")

@app.route("/edit_thing/<int:thing_id>", methods=["GET", "POST"])

def edit_thing(thing_id):

    thing =Thing.query.get(thing_id)
    form = ThingForm( text=thing.text, img=thing.img)
    if form.validate_on_submit():

        thing.text = form.text.data
        thing.img = form.img.data
        db.session.commit()
        return redirect("/axali")
    return render_template("create_thing.html", form=form)

@app.route("/delete_thing/<int:thing_id>", methods=["GET", "POST"])
def delete_thing(thing_id):
    thing= Thing.query.get(thing_id)
    db.session.delete(thing)
    db.session.commit()
    return redirect("/axali")

@app.route("/create_thing", methods=["GET", "POST"])
def create_thing():
    form = ThingForm()
    if form.validate_on_submit():
        new_thing = Thing(
                              text =form.text.data,
                              img=form.img.data,
                               link=form.link.data
        )
        db.session.add(new_thing)
        db.session.commit()
        return redirect("/axali")




    return render_template("create_thing.html", form=form)

@app.route("/edit_new/<int:new_id>", methods=["GET", "POST"])

def edit_new(new_id):

    new =New.query.get(new_id)
    form = NewForm( text=new.text, img=new.img)
    if form.validate_on_submit():

        new.text = form.text.data
        new.img = form.img.data
        db.session.commit()
        return redirect("/axali ambebi2")
    return render_template("create_new.html", form=form)

@app.route("/delete_new/<int:new_id>", methods=["GET", "POST"])
def delete_new(new_id):
    new=New.query.get(new_id)
    db.session.delete(new)
    db.session.commit()
    return redirect("/axali ambebi2")

@app.route("/create_new", methods=["GET", "POST"])
def create_new():
    form = NewForm()
    if form.validate_on_submit():
        new_new = New(
                              text =form.text.data,
                              img=form.img.data
        )
        db.session.add(new_new)
        db.session.commit()
        return redirect("/axali ambebi")


    else:
        print(form.errors)


    return render_template("create_new.html", form=form)

@app.route("/edit_tour/<int:tour_id>", methods=["GET", "POST"])

def edit_tour(tour_id):

    tour =Tour.query.get(tour_id)
    form = TourForm( name=tour.name, img=tour.img)
    if form.validate_on_submit():

        tour.name = form.name.data
        tour.img = form.img.data
        db.session.commit()
        return redirect("/მარშუტები")
    return render_template("create_tour.html", form=form)

@app.route("/delete_tour/<int:tour_id>", methods=["GET", "POST"])
def delete_tour(tour_id):
    tour=Tour.query.get(tour_id)
    db.session.delete(tour)
    db.session.commit()
    return redirect("/მარშუტები")

@app.route("/create_tour", methods=["GET", "POST"])
def create_tour():
    form = TourForm()
    if form.validate_on_submit():
        new_tour = Tour(
                              name=form.name.data,
                              img=form.img.data
        )
        db.session.add(new_tour)
        db.session.commit()
        return redirect("/მარშუტები")


    else:
        print(form.errors)


    return render_template("create_tour.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
         new_user=User(username=form.username.data,
                       password=form.password.data,
                       role="Guest"
                       )

         db.session.add(new_user)
         db.session.commit()
         return redirect("/")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter(User.username == form.username.data).first()
        if user != None and user.check_password( form.password.data):
            login_user(user)
        db.session.commit()
        return redirect("/")


    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/edit_info/<int:info_id>", methods=["GET", "POST"])

def edit_info(info_id):

    info =Info.query.get(info_id)
    form = InfoForm( name=info.name, text=info.text)
    if form.validate_on_submit():

        info.name = form.name.data
        info.text = form.text.data
        db.session.commit()
        return redirect("/სვეტმეტი")
    return render_template("create_info.html", form=form)

@app.route("/edit_doc/<int:doc_id>", methods=["GET", "POST"])
def edit_doc(doc_id):

    doc =Doc.query.get(doc_id)
    form = DocForm( name=doc.name, text=doc.text)
    if form.validate_on_submit():

        doc.name = form.name.data
        doc.text = form.text.data
        db.session.commit()
        return redirect("/meti")
    return render_template("create_doc.html", form=form)

@app.route("/edit_bak/<int:bak_id>", methods=["GET", "POST"])
def edit_bak(bak_id):

    bak =Bak.query.get(bak_id)
    form = BakForm( name=bak.name, text=bak.text)
    if form.validate_on_submit():

        bak.name = form.name.data
        bak.text= form.text.data
        db.session.commit()
        return redirect("/ბაკურიანი")
    return render_template("create_bak.html", form=form)
