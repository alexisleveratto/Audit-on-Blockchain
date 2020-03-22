from .manager_blockchain import ManagerBlockchain

BlockchainManager = ManagerBlockchain()


class Cliente:
    def __init__(
        self,
        client_cuit,
        client_name,
        client_email,
        client_address,
        client_localidad,
        client_codPostal,
        client_provincia,
        country,
        initial_balance,
    ):
        self.companiaId = client_cuit
        self.companiaName = client_name
        self.companiaAddres = (
            client_email
            + ", "
            + client_address
            + ", "
            + client_localidad
            + ", "
            + client_codPostal
            + ", "
            + client_provincia
        )
        self.companiaConutry = country
        self.companiaBalance = initial_balance

    def set_own_payload(self):
        payload = (
            '{\n  "$class": "org.example.biznet.Compania",\n  "companiaId": "%s", "companiaName": "%s",\n  "companiaConutry": "%s",\n  "companiaAddres": "%s",\n  "companiaBalance": %f\n}'
            % (
                str(self.companiaId),
                str(self.companiaName),
                str(self.companiaConutry),
                str(self.companiaAddres),
                self.companiaBalance,
            )
        )
        return payload

    def set_update_payload(self):
        payload = (
            '{\n    "$class": "org.example.biznet.Compania",\n    "companiaName": "%s",\n    "companiaConutry": "%s",\n    "companiaAddres": "%s",\n    "companiaBalance": %f\n}'
            % (
                str(self.companiaName),
                str(self.companiaConutry),
                str(self.companiaAddres),
                self.companiaBalance,
            )
        )
        return payload

    def add_cliente(self):
        payload = self.set_own_payload()
        return BlockchainManager.add("/Compania", payload)

    def update_cliente(
        self,
        companiaName,
        companiaConutry,
        client_email,
        client_address,
        client_localidad,
        client_codPostal,
        client_provincia,
    ):
        self.companiaName = companiaName
        self.companiaConutry = companiaConutry
        self.companiaAddres = (
            client_email
            + ", "
            + client_address
            + ", "
            + client_localidad
            + ", "
            + client_codPostal
            + ", "
            + client_provincia
        )

        payload = self.set_update_payload()

        response = BlockchainManager.update(
            ns_name="/Compania", id=str("/" + self.companiaId), payload=payload,
        )
        return response

    def delete_cliente(self):
        BlockchainManager.delete("/Compania", self.companiaId)

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_cliente(self, client_id=None):
        if not client_id:
            client_id=self.companiaId
        response = BlockchainManager.getSingle("/Compania", id="/" + client_id)
        return response.json()

    def set_auditor(self, id_auditor):
        self.id_auditor = id_auditor

    def get_auditr(self):
        return self.id_auditor

    def set_ciudad(self, id_ciudad):
        self.id_ciudad = id_ciudad

    def get_ciudad(self):
        return self.id_ciudad
