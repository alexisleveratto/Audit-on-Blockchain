from app.models import User
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    FileField,
    FloatField,
    TextField,
    RadioField,
    IntegerField,
    SelectField,
    DateField,
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


class IndexForm(FlaskForm):
    RegistrarCliente = SubmitField("Registrar Cliente")
    GestionarClientes = SubmitField("Gestionar Clientes")
    ClientMainPage = SubmitField("Tu Cuenta")


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
    # initial_balance = FloatField(
    #     "Saldo Inicial de la Cuenta Deudores por Venta", validators=[DataRequired()]
    # )
    submit = SubmitField("Registrar Cliente")
    cancel = SubmitField("Cancelar")


class ClientPageForm(FlaskForm):
    ledger = SubmitField("Libro Mayor")
    modify = SubmitField("Modificar")
    delete = SubmitField("Eliminar")
    cancel = SubmitField("Cancelar")


class ModifyClientForm(FlaskForm):
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
    # initial_balance = FloatField(
    #     "Saldo Inicial de la Cuenta Deudores por Venta",
    #     validators=[DataRequired()],
    #     render_kw={"disabled": ""},
    # )
    submit = SubmitField("Modificar Cliente")
    cancel = SubmitField("Cancelar")


class AddTransaccionForm(FlaskForm):
    # codigo_cuenta = SelectField("Codigo de Cuenta", coerce=int, choices=[], validators=[DataRequired()])
    nombre_cuenta = SelectField(
        "Nombre de Cuenta", coerce=int, choices=[], validators=[DataRequired()]
    )
    d_h = RadioField("Tipo de Cuenta", choices=[("D", "Debe"), ("H", "Haber")])
    numero_minuta = IntegerField("Numero Minuta", validators=[DataRequired()])
    concepto = StringField("Concepto", validators=[DataRequired()])
    detalle = StringField("Detalle", validators=[DataRequired()])
    fecha_movimiento = DateField(
        "Fecha Movimiento",
        format="%d/%m/%Y",
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    monto = FloatField("Monto", validators=[DataRequired()])
    documentation = StringField(
        "Factura", validators=[DataRequired()], render_kw={"disabled": ""},
    )
    submit = SubmitField("Grabar Transaccion")
    cancel = SubmitField("Cancelar")


class AddCountryForm(FlaskForm):
    country_name = StringField("Nombre Pais", validators=[DataRequired()])
    submit = SubmitField("Agregar")
    cancel = SubmitField("Cancelar")


class AddCityForm(FlaskForm):
    zip_code = StringField("Codigo Postal", validators=[DataRequired()])
    city_name = StringField("Nombre Ciudad", validators=[DataRequired()])
    country_name = SelectField(
        "Nombre Pais", coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField("Agregar")
    cancel = SubmitField("Cancelar")


class AddOfficeForm(FlaskForm):
    address = StringField("Direccion Oficina", validators=[DataRequired()])
    city_name = SelectField(
        "Ciudad", coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField("Agregar")
    cancel = SubmitField("Cancelar")


class AddAccountForm(FlaskForm):
    account_name = StringField("Nombre Cuenta", validators=[DataRequired()])
    submit = SubmitField("Agregar")
    cancel = SubmitField("Cancelar")


class AddAuditForm(FlaskForm):
    username = StringField("Nombre de Usuario", validators=[DataRequired()])
    email = StringField("Email de Usuario", validators=[DataRequired()])
    submit = SubmitField("Agregar")
    cancel = SubmitField("Cancelar")


class XslTransactionsForm(FlaskForm):
    file_path = FileField(
        "Hoja de Cálcuĺo",
        validators=[
            FileRequired(),
            FileAllowed(
                [
                    "xlsx",
                    "xlsm",
                    "xlsb",
                    "xltx",
                    "xltm",
                    "xls",
                    "xlt",
                    "xml",
                    "xlam",
                    "xlw",
                    "csv",
                ],
                "Hoja de calculo",
            ),
        ],
    )
    zip_file_path = FileField(
        "Facturas",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png", "zip", "pdf"], "No es una extension válida"),
        ],
    )
    submit = SubmitField("Subir")

class NewLedgerForm(FlaskForm):
    initial_date = DateField(
        "Fecha Movimiento",
        format="%d/%m/%Y",
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    initial_balance = FloatField("Saldo Inicial", validators=[DataRequired()])
    account_name = SelectField(
        "Nombre de Cuenta", coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField("Agregar Mayor")

class NewContractForm(FlaskForm):
    fees = FloatField("Honorarios", validator=[DataRequired()])
    initial_date = DateField(
        "Fecha Inicio",
        format="%d/%m/%Y",
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    final_date = initial_date = DateField(
        "Fecha Fin",
        format="%d/%m/%Y",
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    client_name = SelectField(
        "Nombre Cliente", coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField("Agregar")


