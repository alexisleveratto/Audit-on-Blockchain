from .manager_blockchain import ManagerBlockchain


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

    def set_payload(self):
        self.payload = (
            '{\n  "$class": "org.example.biznet.Compania",\n  "companiaId": "%s",\n  "companiaName": "%s",\n  "companiaConutry": "%s",\n  "companiaAddres": "%s",\n  "companiaBalance": %f\n}'
            % (
                str(self.companiaId),
                str(self.companiaName),
                str(self.companiaConutry),
                str(self.companiaAddres),
                self.companiaBalance,
            )
        )
