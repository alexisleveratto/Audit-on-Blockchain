from app import app, db, posta
from app.forms import (
    AddTransaccionForm,
    AuditIndexForm,
    ChangePasswordForm,
    ClientPageForm,
    EmailForm,
    LoginForm,
    ModifyClientForm,
    PasswordForm,
    RegisterClientForm,
    RegistrationForm,
    VerifyClientForm,
)
from app.models import User
from app.utilsfunctions import allowed_file, get_random_string
from .classes import AfipManager, BlockchainManager, TransaccionManager
from .classes.cliente import Cliente
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message
import os
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    title = "Menu Principal"
    form = AuditIndexForm()
    if form.validate_on_submit():
        if form.RegistrarCliente.data:
            return redirect(url_for("verify_client"))
        if form.GestionarClientes.data:
            return redirect(url_for("client_table"))
    return render_template("index.html", title=title, form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Usuario o Contraseña Invalidos")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Iniciar Sesion", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registrado")
        return redirect(url_for("login"))
    return render_template("register.html", title="Registro", form=form)


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = EmailForm()
    if form.validate_on_submit():
        mail = form.email.data
        check_mail = User.query.filter_by(email=mail).first()
        if check_mail:
            hashCode = get_random_string()
            check_mail.hashCode = hashCode
            db.session.commit()
            msg = Message(
                "Confirm Password Change",
                sender="alexis.leveratto@github.com",
                recipients=[mail],
            )
            msg.body = (
                "Hello,\nWe've received a request to reset your password. If you want to reset your password, click the link below and enter your new password\n http://127.0.0.1:5000/"
                + check_mail.hashCode
            )
            posta.send(msg)
            flash("Revise su email")
            return redirect(url_for("forgot"))
    return render_template(
        "forgot_password.html", title="Recuperar Contraseña", form=form
    )


@app.route("/<string:hashCode>", methods=["GET", "POST"])
def hashcode(hashCode):
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    check_by_hashCode = User.query.filter_by(hashCode=hashCode).first()
    if check_by_hashCode:
        form = PasswordForm()
        if form.validate_on_submit():
            check_by_hashCode.set_password(form.password.data)
            check_by_hashCode.hashCode = None
            db.session.commit()
            flash("Contraseña Recuperada con Éxito")
            return redirect(url_for("login"))
        return render_template(
            "change_password.html", title="Cambiar Contraseña", form=form
        )
    return redirect(url_for("index"))


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.old_password.data):
            user.set_password(form.password.data)
            db.session.commit()
            logout_user()
            return redirect(url_for("index"))
        else:
            flash("Repita correctamente su contraseña anterior")
    return render_template(
        "user_change_password.html", title="Cambiar Contraseña", form=form
    )


@app.route("/verify-client", methods=["GET", "POST"])
def verify_client():
    if not current_user.is_authenticated:
        return redirect(url_for("index"))
    form = VerifyClientForm()
    if form.validate_on_submit():
        if form.submit.data:
            if AfipManager.get_persona_juridica(form.cuit.data):
                return redirect(url_for("new_client"))
            else:
                flash("No se encuentra ninguna persona con el CUIT brindado")
    if form.cancel.data:
        return redirect(url_for("index"))
    return render_template("verify_client.html", form=form)


@app.route("/new-client", methods=["GET", "POST"])
def new_client():
    form = RegisterClientForm()
    form.cuit.data = AfipManager.client_cuit
    if not form.client_name.data:
        form.client_name.data = AfipManager.client_name
    if not form.client_email.data:
        form.client_email.data = AfipManager.client_email
    if not form.client_address.data:
        form.client_address.data = AfipManager.client_address
    if not form.client_localidad.data:
        form.client_localidad.data = AfipManager.client_localidad
    if not form.client_codPostal.data:
        form.client_codPostal.data = AfipManager.client_codPostal
    if not form.client_provincia.data:
        form.client_provincia.data = AfipManager.client_provincia
    if form.validate_on_submit():
        # user = User(username=form.cuit.data, email=form.client_email.data)
        # user.set_password(str(form.cuit.data))
        # db.session.add(user)
        # db.session.commit()
        client = Cliente(
            client_cuit=form.cuit.data,
            client_name=form.client_name.data,
            client_email=form.client_email.data,
            client_address=form.client_address.data,
            client_localidad=form.client_localidad.data,
            client_codPostal=form.client_codPostal.data,
            client_provincia=form.client_provincia.data,
            country=form.country.data,
            initial_balance=form.initial_balance.data,
        )
        client.add_cliente()
        return redirect(url_for("index"))
    if form.cancel.data:
        return redirect(url_for("index"))
    flash("Verifique y complete la información de su cliente")
    return render_template("client_register.html", form=form)


@app.route("/clients", methods=["GET", "POST"])
@login_required
def client_table():
    clientes = BlockchainManager.getAll(ns_name="/Compania")
    return render_template("client_table.html", clientes=clientes)


@app.route("/clients/<client_id>", methods=["GET", "POST"])
@login_required
def client_page(client_id):
    client = BlockchainManager.getSingle(ns_name="/Compania", id=str("/" + client_id))
    form = ClientPageForm()
    if form.validate_on_submit():
        if form.modify.data:
            return redirect(url_for("modify_client", client_id=client_id))
    if form.cancel.data:
        return redirect(url_for("index"))
    return render_template("client_page.html", client=client, form=form)


@app.route("/clients/<string:client_id>/modify", methods=["GET", "POST"])
@login_required
def modify_client(client_id):
    form = ModifyClientForm()
    client = BlockchainManager.getSingle(ns_name="/Compania", id=str("/" + client_id))
    client_address = client["companiaAddres"].split(", ")
    form.cuit.data = client_id
    if not form.client_name.data:
        form.client_name.data = client["companiaName"]
    if not form.client_email.data:
        form.client_email.data = client_address[0]
    if not form.client_address.data:
        form.client_address.data = client_address[1]
    if not form.client_localidad.data:
        form.client_localidad.data = client_address[2]
    if not form.client_codPostal.data:
        form.client_codPostal.data = client_address[3]
    if not form.client_provincia.data:
        form.client_provincia.data = client_address[4]
    if not form.country.data:
        form.country.data = client["companiaConutry"]
    if not form.initial_balance.data:
        form.initial_balance.data = client["companiaBalance"]
    if form.validate_on_submit():
        client = Cliente(
            client_cuit=form.cuit.data,
            client_name=form.client_name.data,
            client_email=form.client_email.data,
            client_address=form.client_address.data,
            client_localidad=form.client_localidad.data,
            client_codPostal=form.client_codPostal.data,
            client_provincia=form.client_provincia.data,
            country=form.country.data,
            initial_balance=form.initial_balance.data,
        )
        client.update_cliente(
            companiaName=form.client_name.data,
            companiaConutry=form.country.data,
            client_email=form.client_email.data,
            client_address=form.client_address.data,
            client_localidad=form.client_localidad.data,
            client_codPostal=form.client_codPostal.data,
            client_provincia=form.client_provincia.data,
        )
        form_client_page = ClientPageForm()
        return render_template("client_page.html", client=client, form=form_client_page)
    if form.cancel.data:
        return redirect(url_for("index"))
    return render_template("client_modify.html", form=form)


@app.route("/clients/<string:client_id>/delete", methods=["GET", "POST"])
@login_required
def delete_client(client_id):
    # DO SOME DB SHIT HERE
    BlockchainManager.delete(ns_name="/Compania", id=str("/" + client_id))
    return redirect(url_for("client_table"))


@app.route("/clients/<string:client_id>/record-transaction", methods=["GET", "POST"])
@login_required
def record_transaction(client_id):
    form = AddTransaccionForm()

    if form.validate_on_submit():
        client = BlockchainManager.getSingle(
            ns_name="/Compania", id=str("/" + client_id)
        )
        added_transaction = TransaccionManager.add_transaccion(
            client,
            form.codigo_cuenta.data,
            form.nombre_cuenta.data,
            form.d_h.data,
            form.numero_minuta.data,
            form.concepto.data,
            form.detalle.data,
            form.fecha_movimiento.data,
            form.monto.data,
        )
        flash("Transaccion Agregada con el ID " + added_transaction["transactionId"])
        return render_template("record_transaction.html", form=form)
    if form.cancel.data:
        return redirect(url_for("index"))

    return render_template("record_transaction.html", form=form)


@app.route("/clients/<string:client_id>/transactions", methods=["GET", "POST"])
@login_required
def transaction_table(client_id):
    transactions = TransaccionManager.get_transaction_for_client(client_id)
    return render_template("transactions_table.html", transactions=transactions, client_id=client_id)


# @app.route("/clients/<string:client_id>/audit-results", methods=["GET", "POST"])
@app.route("/clients/<string:client_id>/audit-results", methods=["POST"])
@login_required
def upload_audit_results(client_id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No hay ningún archivo seleccionado')
            return redirect(request.url)
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)

        if not os.path.isdir(os.path.join(app.config['UPLOAD_FOLDER'], client_id)):
            client_id_folder = secure_filename(client_id)
            os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], client_id_folder) + '/')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.join(app.config['UPLOAD_FOLDER'], client_id), filename))
            flash("Documento Guardado con Exito")
    return redirect(url_for('transaction_table', client_id=client_id))