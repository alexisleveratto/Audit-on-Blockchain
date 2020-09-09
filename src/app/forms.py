from app.models import User
from flask_babel import lazy_gettext as _l
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
    username = StringField(_l("Usuario"), validators=[DataRequired()])
    password = PasswordField(_l("Contraseña"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Recuerdame"))
    submit = SubmitField(_l("Iniciar Sesion"))


class RegistrationForm(FlaskForm):
    username = StringField(_l("Usuario"), validators=[DataRequired()])
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    password = PasswordField(_l("Contraseña"), validators=[DataRequired()])
    password2 = PasswordField(
        _l("Repita Contraseña"), validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(_l("Registrarse"))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l("Utilice otro nombre de usuario."))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l("Utilice otro email."))


class EmailForm(FlaskForm):
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    submit = SubmitField(_l("Recuperar Contraseña"))


class PasswordForm(FlaskForm):
    password = PasswordField(_l("Contraseña"), validators=[DataRequired()])
    password2 = PasswordField(
        _l("Repita Contraseña"), validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(_l("Cambiar Contraseña"))


class ChangePasswordForm(FlaskForm):
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    old_password = PasswordField(_l("Antigua Contraseña"), validators=[DataRequired()])
    password = PasswordField(_l("Contraseña Nueva"), validators=[DataRequired()])
    password2 = PasswordField(
        _l("Repita Contraseña"), validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField(_l("Cambiar Contraseña"))


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Request Password Reset")


class IndexForm(FlaskForm):
    RegistrarCliente = SubmitField(_l("Registrar Cliente"))
    GestionarClientes = SubmitField(_l("Gestionar Clientes"))
    ClientMainPage = SubmitField(_l("Tu Cuenta"))


class VerifyClientForm(FlaskForm):
    cuit = StringField(_l("CUIT Cliente"), validators=[DataRequired()])
    submit = SubmitField(_l("Verificar"))
    cancel = SubmitField(_l("Cancelar"))


class RegisterClientForm(FlaskForm):
    cuit = StringField(
        _l("CUIT Cliente"), validators=[DataRequired()], render_kw={"disabled": ""}
    )
    client_name = StringField(_l("Nombre Cliente"), validators=[DataRequired()])
    client_email = StringField(
        _l("Email de Contacto"), validators=[DataRequired(), Email()]
    )
    client_address = StringField(_l("Domicilio Fiscal"), validators=[DataRequired()])
    client_localidad = StringField(_l("Localidad"), validators=[DataRequired()])
    client_codPostal = TextField(_l("Codigo Postal"), validators=[DataRequired()])
    client_provincia = StringField(_l("Provincia"), validators=[DataRequired()])
    country = StringField(_l("País"), validators=[DataRequired()])
    # initial_balance = FloatField(
    #     "Saldo Inicial de la Cuenta Deudores por Venta", validators=[DataRequired()]
    # )
    submit = SubmitField(_l("Registrar Cliente"))
    cancel = SubmitField(_l("Cancelar"))


class ClientPageForm(FlaskForm):
    ledger = SubmitField(_l("Libro Mayor"))
    modify = SubmitField(_l("Modificar"))
    delete = SubmitField(_l("Eliminar"))
    cancel = SubmitField(_l("Cancelar"))


class ModifyClientForm(FlaskForm):
    cuit = StringField(
        _l("CUIT Cliente"), validators=[DataRequired()], render_kw={"disabled": ""}
    )
    client_name = StringField(_l("Nombre Cliente"), validators=[DataRequired()])
    client_email = StringField(
        _l("Email de Contacto"), validators=[DataRequired(), Email()]
    )
    client_address = StringField(_l("Domicilio Fiscal"), validators=[DataRequired()])
    client_localidad = StringField(_l("Localidad"), validators=[DataRequired()])
    client_codPostal = TextField(_l("Codigo Postal"), validators=[DataRequired()])
    client_provincia = StringField(_l("Provincia"), validators=[DataRequired()])
    country = StringField(_l("País"), validators=[DataRequired()])
    # initial_balance = FloatField(
    #     "Saldo Inicial de la Cuenta Deudores por Venta",
    #     validators=[DataRequired()],
    #     render_kw={"disabled": ""},
    # )
    submit = SubmitField(_l("Modificar Cliente"))
    cancel = SubmitField(_l("Cancelar"))


class AddTransaccionForm(FlaskForm):
    # codigo_cuenta = SelectField("Codigo de Cuenta", coerce=int, choices=[], validators=[DataRequired()])
    nombre_cuenta = SelectField(
        _l("Nombre de Cuenta"), coerce=int, choices=[], validators=[DataRequired()]
    )
    d_h = RadioField(_l("Tipo de Cuenta"), choices=[("D", "Debe"), ("H", "Haber")])
    numero_minuta = IntegerField(_l("Numero Minuta"), validators=[DataRequired()])
    concepto = StringField(_l("Concepto"), validators=[DataRequired()])
    detalle = StringField(_l("Detalle"), validators=[DataRequired()])
    fecha_movimiento = DateField(
        _l("Fecha Movimiento"),
        format="%d/%m/%Y",
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    monto = FloatField(_l("Monto"), validators=[DataRequired()])
    documentation = StringField(
        _l("Factura"), validators=[DataRequired()], render_kw={"disabled": ""},
    )
    submit = SubmitField(_l("Grabar Transaccion"))
    cancel = SubmitField(_l("Cancelar"))


class AddCountryForm(FlaskForm):
    country_name = StringField(_l("Nombre Pais"), validators=[DataRequired()])
    submit = SubmitField(_l("Agregar"))
    cancel = SubmitField(_l("Cancelar"))


class AddCityForm(FlaskForm):
    zip_code = StringField(_l("Codigo Postal"), validators=[DataRequired()])
    city_name = StringField(_l("Nombre Ciudad"), validators=[DataRequired()])
    country_name = SelectField(
        _l("Nombre Pais"), coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField(_l("Agregar"))
    cancel = SubmitField(_l("Cancelar"))


class AddOfficeForm(FlaskForm):
    address = StringField(_l("Direccion Oficina"), validators=[DataRequired()])
    city_name = SelectField(
        _l("Ciudad"), coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField(_l("Agregar"))
    cancel = SubmitField(_l("Cancelar"))


class AddAccountForm(FlaskForm):
    account_name = StringField(_l("Nombre Cuenta"), validators=[DataRequired()])
    submit = SubmitField(_l("Agregar"))
    cancel = SubmitField(_l("Cancelar"))


class AddAuditForm(FlaskForm):
    username = StringField(_l("Nombre de Usuario"), validators=[DataRequired()])
    email = StringField(_l("Email de Usuario"), validators=[DataRequired()])
    submit = SubmitField(_l("Agregar"))
    cancel = SubmitField(_l("Cancelar"))


class XslTransactionsForm(FlaskForm):
    file_path = FileField(
        _l("Hoja de Cálcuĺo"),
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
                _l("Hoja de calculo"),
            ),
        ],
    )
    zip_file_path = FileField(
        _l("Facturas"),
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png", "zip", "pdf"], _l("No es una extension válida")),
        ],
    )
    submit = SubmitField(_l("Subir"))


class NewLedgerForm(FlaskForm):
    initial_date = DateField(
        _l("Fecha Movimiento"),
        format="%d/%m/%Y",
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    initial_balance = FloatField(_l("Saldo Inicial"), validators=[DataRequired()])
    account_name = SelectField(
        _l("Nombre de Cuenta"), coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField(_l("Agregar Mayor"))


class NewContractForm(FlaskForm):
    fees = FloatField(_l("Honorarios"), validator=[DataRequired()])
    initial_date = DateField(
        _l("Fecha Inicio"),
        format="%d/%m/%Y",
        validators=[DataRequired()],
        render_kw={"placeholder": "dd/mm/AAAA"},
    )
    final_date = initial_date = DateField(
        _l("Fecha Fin"), format="%d/%m/%Y", render_kw={"placeholder": "dd/mm/AAAA"},
    )
    client_name = SelectField(
        _l("Nombre Cliente"), coerce=int, choices=[], validators=[DataRequired()]
    )
    submit = SubmitField(_l("Agregar"))
