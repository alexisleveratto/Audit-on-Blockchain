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

    def add_cliente(self):
        self.set_own_payload()
        BlockchainManager.add("/Compania", self.payload)

    def update_cliente(self,  companiaName, companiaConutry, client_email, client_address, client_localidad, client_codPostal, client_provincia):
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
        BlockchainManager.update(ns_name="/Compania", id="/" + self.companiaId, payload=self.payload)


