from .manager_blockchain import ManagerBlockchain

BlockchainManager = ManagerBlockchain()

class Transaccion():
    cliente
    monto
    
    payload = "{
        "$class\": \"org.example.biznet.TransactionBalanceGeneral\",
        "Company_BalanceGeneral\": {
                \"$class\": \"org.example.biznet.Compania\",
                \"companiaId\": \"string\",
                \"companiaName\": \"string\",
                \"companiaConutry\": \"string\",
                \"companiaAddres\": \"string\",
                \"companiaBalance\": 0\n  
            },
        \"codigo_cuenta\": \"string\",
        \"nombre_cuenta\": \"string\",
        \"D_H\": \"D\",
        \"numero_minuta\": 0,
        \"concepto\": \"string\",
        \"detalle\": \"string\",
        \"fecha_movimiento\": \"string\",
        \"monto\": 4,
        \"timestamp\": \"2020-03-12T12:17:26.829Z\"
        }"
    payload = "{\n  \"$class\": \"org.example.biznet.TransactionBalanceGeneral\",\n  \"Company_BalanceGeneral\": {\n    \"$class\": \"org.example.biznet.Compania\",\n    \"companiaId\": \"%s\",\n    \"companiaName\": \"%s\",\n    \"companiaConutry\": \"%s\",\n    \"companiaAddres\": \"%s\",\n    \"companiaBalance\": %f\n  },\n  \"codigo_cuenta\": \"%s\",\n  \"nombre_cuenta\": \"%s\",\n  \"D_H\": \"%s\",\n  \"numero_minuta\": %f,\n  \"concepto\": \"%s\",\n  \"detalle\": \"%s\",\n  \"fecha_movimiento\": \"%s\",\n  \"monto\": %f\n}"
    def add_transccion(self):
        payload = self.set_own_payload()
        return BlockchainManager.add("/Compania", payload)