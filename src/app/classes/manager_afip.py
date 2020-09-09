import requests


class ManagerAfip:
    def __init__(self):
        # self.url = "https://afip.tangofactura.com/Rest/GetContribuyenteFull"
        self.url = "https://afip.tangofactura.com/Index/GetFullContribuyente"
        self.exception = None
        self.client_cuit = None
        self.client_name = None
        self.client_address = None
        self.client_localidad = None
        self.client_codPostal = None
        self.client_provincia = None
        self.client_email = None

    def get_persona_juridica(self, cuit):
        # test_cuit = 30505779858
        payload = '{\r\n\t"cuit": %s \r\n\t\r\n}' % str(cuit)
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "GET", self.url, headers=headers, data=payload, verify=False
        )
        if response.json()["errorGetData"]:
            return False
        self.client_cuit = response.json()["Contribuyente"]["idPersona"]
        self.client_name = response.json()["Contribuyente"]["nombre"]
        self.client_address = response.json()["Contribuyente"]["domicilioFiscal"][
            "direccion"
        ]
        self.client_localidad = response.json()["Contribuyente"]["domicilioFiscal"][
            "localidad"
        ]
        self.client_codPostal = response.json()["Contribuyente"]["domicilioFiscal"][
            "codPostal"
        ]
        self.client_provincia = response.json()["Contribuyente"]["domicilioFiscal"][
            "nombreProvincia"
        ]
        return True
