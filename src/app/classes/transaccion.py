from .manager_blockchain import ManagerBlockchain

BlockchainManager = ManagerBlockchain()


class ManagerTransaccion:
    def add_transaccion(
        self,
        cliente,
        codigo_cuenta,
        nombre_cuenta,
        d_h,
        numero_minuta,
        concepto,
        detalle,
        fecha_movimiento,
        monto,
    ):
        payload = (
            '{\n  "$class": "org.example.biznet.TransactionBalanceGeneral",\n  "Company_BalanceGeneral": {\n    "$class": "org.example.biznet.Compania",\n    "companiaId": "%s",\n    "companiaName": "%s",\n    "companiaConutry": "%s",\n    "companiaAddres": "%s",\n    "companiaBalance": %f\n  },\n  "codigo_cuenta": "%s",\n  "nombre_cuenta": "%s",\n  "D_H": "%s",\n  "numero_minuta": %f,\n  "concepto": "%s",\n  "detalle": "%s",\n  "fecha_movimiento": "%s",\n  "monto": %f\n}'
            % (
                cliente["companiaId"],
                cliente["companiaName"],
                cliente["companiaConutry"],
                cliente["companiaAddres"],
                cliente["companiaBalance"],
                codigo_cuenta,
                nombre_cuenta,
                d_h,
                numero_minuta,
                concepto,
                detalle,
                fecha_movimiento,
                monto,
            )
        )
        return BlockchainManager.add("/TransactionBalanceGeneral", payload)
