import pytest

from app.classes.cliente import Cliente
from app.classes import BlockchainManager, TransaccionManager

##### En estas pruebas, testeamos el registro de los clientes como participantes de nuestra blockchain
def add_client(
    cuit, client_name, email, address, localidad, zip_code, provincia, country
):
    client = Cliente(
        client_cuit=cuit,
        client_name=client_name,
        client_email=email,
        client_address=address,
        client_localidad=localidad,
        client_codPostal=zip_code,
        client_provincia=provincia,
        country=country,
        initial_balance=0,
    )
    response = client.add_cliente()
    try:
        response["error"]
        return False
    except:
        return True


def delete_client(client_id):
    try:
        BlockchainManager.delete(ns_name="/Compania", id=str("/" + client_id))
        return True
    except:
        return False


# Prueba de Registro de Cliente: Validar datos obligatorios del cliente.
# a.Permitir registrar cliente con los datos completos: si el auditor ingresa todos los datos obligatorios,
# se debe permitir pasar a la siguiente etapa de registro.


def test_new_client_ok():
    test_cuit = "test_cuit"
    test_client_name = "test_client_name"
    test_email = "test_email"
    test_address = "test_address"
    test_localidad = "test_localidad"
    test_zip_code = "test_zip_code"
    test_provincia = "test_provincia"
    test_country = "test_country"
    assert add_client(
        test_cuit,
        test_client_name,
        test_email,
        test_address,
        test_localidad,
        test_zip_code,
        test_provincia,
        test_country,
    )
    assert delete_client(test_cuit)


# b.Rechazar registro de cliente con los datos incompletos: si el auditor cuando no completa todos los campos requeridos,
# no debe continuar con el proceso de registro.
def test_new_client_fail():
    test_cuit = ""  # Dejamos vacio el cuit
    test_client_name = "test_client_name"
    test_email = "test_email"
    test_address = "test_address"
    test_localidad = "test_localidad"
    test_zip_code = "test_zip_code"
    test_provincia = "test_provincia"
    test_country = "test_country"
    assert not (
        add_client(
            test_cuit,
            test_client_name,
            test_email,
            test_address,
            test_localidad,
            test_zip_code,
            test_provincia,
            test_country,
        )
    )
    assert delete_client(test_cuit)


# 3.	Prueba de Edición de Cliente: Validar datos obligatorios del cliente.
# a.	Permitir edición de cliente con los datos completos: si el auditor ingresa
# todos los datos, al editar un cliente, se debe permitir pasar a la siguiente etapa de edición.
def test_modify_client_ok():
    test_cuit = "test_cuit"
    test_client_name = "test_client_name"
    test_email = "test_email"
    test_address = "test_address"
    test_localidad = "test_localidad"
    test_zip_code = "test_zip_code"
    test_provincia = "test_provincia"
    test_country = "test_country"

    assert add_client(
        test_cuit,
        test_client_name,
        test_email,
        test_address,
        test_localidad,
        test_zip_code,
        test_provincia,
        test_country,
    )

    old_client = BlockchainManager.getSingle(
        ns_name="/Compania", id=str("/" + test_cuit)
    )
    old_client_address = old_client["companiaAddres"].split(", ")

    old_client_name = old_client["companiaName"]
    old_client_email = old_client_address[0]
    old_client_address = old_client_address[1]
    old_client_localidad = old_client_address[2]
    old_client_codPostal = old_client_address[3]
    old_client_provincia = old_client_address[4]
    old_country = old_client["companiaConutry"]

    client = Cliente(
        client_cuit=test_cuit,
        client_name=old_client_name,
        client_email=old_client_email,
        client_address=old_client_address,
        client_localidad=old_client_localidad,
        client_codPostal=old_client_codPostal,
        client_provincia=old_client_provincia,
        country=old_country,
        initial_balance=0,
    )

    client.update_cliente(
        companiaName="new companiaName",
        companiaConutry="new companiaConutry",
        client_email="new client_email",
        client_address="new client_address",
        client_localidad="new client_localidad",
        client_codPostal="new client_codPostal",
        client_provincia="new client_provincia",
    )

    updated_client = BlockchainManager.getSingle(
        ns_name="/Compania", id=str("/" + test_cuit)
    )
    if updated_client["companiaName"] == "new companiaName":
        assert True
    else:
        assert False
    assert delete_client(test_cuit)


# b.Rechazar edición de cliente con los datos incompletos: si el auditor no ingresa todos los datos,
#   al editar un cliente, no debe continuar con el proceso de edición.
def test_modify_client_fail():
    test_cuit = "test_cuit"
    test_client_name = "test_client_name"
    test_email = "test_email"
    test_address = "test_address"
    test_localidad = "test_localidad"
    test_zip_code = "test_zip_code"
    test_provincia = "test_provincia"
    test_country = "test_country"

    assert add_client(
        test_cuit,
        test_client_name,
        test_email,
        test_address,
        test_localidad,
        test_zip_code,
        test_provincia,
        test_country,
    )

    old_client = BlockchainManager.getSingle(
        ns_name="/Compania", id=str("/" + test_cuit)
    )
    old_client_address = old_client["companiaAddres"].split(", ")

    old_client_name = old_client["companiaName"]
    old_client_email = old_client_address[0]
    old_client_address = old_client_address[1]
    old_client_localidad = old_client_address[2]
    old_client_codPostal = old_client_address[3]
    old_client_provincia = old_client_address[4]
    old_country = old_client["companiaConutry"]

    client = Cliente(
        client_cuit=test_cuit,
        client_name=old_client_name,
        client_email=old_client_email,
        client_address=old_client_address,
        client_localidad=old_client_localidad,
        client_codPostal=old_client_codPostal,
        client_provincia=old_client_provincia,
        country=old_country,
        initial_balance=0,
    )

    try:
        client.update_cliente(
            companiaName=None,  # No se ingresa el nombre
            companiaConutry="new companiaConutry",
            client_email="new client_email",
            client_address="new client_address",
            client_localidad="new client_localidad",
            client_codPostal="new client_codPostal",
            client_provincia="new client_provincia",
        )
        assert False
    except:
        assert True

    assert delete_client(test_cuit)


# 4.Prueba de Registro de Transacción: Validar datos de registro de transacción.

# a.Permitir registro de transacción con los datos completos: si el cliente ingresa
#  todos los datos al registro de una transacción, se debe permitir pasar a la siguiente etapa de registro.


def test_record_transaction_ok():
    test_cuit = "test_cuit"
    test_client_name = "test_client_name"
    test_email = "test_email"
    test_address = "test_address"
    test_localidad = "test_localidad"
    test_zip_code = "test_zip_code"
    test_provincia = "test_provincia"
    test_country = "test_country"

    assert add_client(
        test_cuit,
        test_client_name,
        test_email,
        test_address,
        test_localidad,
        test_zip_code,
        test_provincia,
        test_country,
    )

    client = BlockchainManager.getSingle(ns_name="/Compania", id=str("/" + test_cuit))
    try:
        TransaccionManager.add_transaccion(
            cliente=client,
            codigo_cuenta="test_codigo_cuenta",
            nombre_cuenta="test_nombre_cuenta",
            d_h="D",
            numero_minuta=0,
            concepto="test_comcepto",
            detalle="test_detalle",
            fecha_movimiento="test_fecha_movimiento",
            monto=198,
        )
        assert True
    except:
        assert delete_client(test_cuit)
        assert False
    assert delete_client(test_cuit)


# b. Rechazar registro de transacción con los datos incompletos: si el cliente no ingresa todos los
#  datos al registro de una transacción, no debe continuar con el proceso de registro.
def test_record_transaction_fail():
    test_cuit = "test_cuit"
    test_client_name = "test_client_name"
    test_email = "test_email"
    test_address = "test_address"
    test_localidad = "test_localidad"
    test_zip_code = "test_zip_code"
    test_provincia = "test_provincia"
    test_country = "test_country"

    assert add_client(
        test_cuit,
        test_client_name,
        test_email,
        test_address,
        test_localidad,
        test_zip_code,
        test_provincia,
        test_country,
    )

    client = BlockchainManager.getSingle(ns_name="/Compania", id=str("/" + test_cuit))
    try:
        TransaccionManager.add_transaccion(
            cliente=client,
            codigo_cuenta="test_codigo_cuenta",
            nombre_cuenta="test_nombre_cuenta",
            d_h="D",
            numero_minuta=0,
            concepto="test_comcepto",
            detalle="test_detalle",
            fecha_movimiento="test_fecha_movimiento",
            monto=None,  # No ingresamos el monto
        )
        assert False
    except:
        assert delete_client(test_cuit)
        assert True
    assert delete_client(test_cuit)
