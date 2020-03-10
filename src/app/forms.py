from app.models import User
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    FloatField,
    TextField,
)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember_me = BooleanField("Recuerdame")
    submit = SubmitField("Iniciar Sesion")


class RegistrationForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    password2 = PasswordField(
        "Repita Contraseña", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Registrarse")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Utilice otro nombre de usuario.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Utilice otro email.")


class EmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Recuperar Contraseña")


class PasswordForm(FlaskForm):
    password = PasswordField("Contraseña", validators=[DataRequired()])
    password2 = PasswordField(
        "Repita Contraseña", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Cambiar Contraseña")


class ChangePasswordForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    old_password = PasswordField("Antigua Contraseña", validators=[DataRequired()])
    password = PasswordField("Contraseña Nueva", validators=[DataRequired()])
    password2 = PasswordField(
        "Repita Contraseña", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Cambiar Contraseña")


class AuditIndexForm(FlaskForm):
    RegistrarCliente = SubmitField("Registrar Cliente")
    GestionarClientes = SubmitField("Gestionar Clientes")


class VerifyClientForm(FlaskForm):
    cuit = StringField("CUIT Cliente", validators=[DataRequired()])
    submit = SubmitField("Verificar")
    cancel = SubmitField("Cancelar")


class RegisterClientForm(FlaskForm):
    cuit = StringField(
        "CUIT Cliente", validators=[DataRequired()], render_kw={"disabled": ""}
    )
    client_name = StringField("Nombre Cliente", validators=[DataRequired()])
    client_email = StringField(
        "Email de Contacto", validators=[DataRequired(), Email()]
    )
    client_address = StringField("Domicilio Fiscal", validators=[DataRequired()])
    client_localidad = StringField("Localidad", validators=[DataRequired()])
    client_codPostal = TextField("Codigo Postal", validators=[DataRequired()])
    client_provincia = StringField("Provincia", validators=[DataRequired()])
    country = StringField("País", validators=[DataRequired()])
    initial_balance = FloatField(
        "Saldo Inicial de la Cuenta Deudores por Venta", validators=[DataRequired()]
    )
    submit = SubmitField("Registrar Cliente")
    cancel = SubmitField("Cancelar")
