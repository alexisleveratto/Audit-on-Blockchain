from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
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


class RegisterClientForm(FlaskForm):
    cuit = StringField("CUIT Cliente", validators=[DataRequired()])
    client_name = StringField("Nombre Cliente")
    client_email = StringField("Email de Contacto")
    client_address = StringField("Domicilio Fiscal")
    client_localidad = StringField("Localidad")
    client_codPostal = StringField("Codigo Postal")
    client_provincia = StringField("Provincia")
    country = StringField("País")
    initial_balance = FloatField(
        "Saldo Inicial de la Cuenta Deudores por Venta", validators=[DataRequired()]
    )

    submit = SubmitField("Registrar Cliente")
    cancel = SubmitField("Cancelar")
