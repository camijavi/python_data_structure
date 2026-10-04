# Your mission: Represent each order as a
# dictionary that includes a customer and a list
# of devices. Show how many devices each order contains.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def supportRequestLog():
    printTitle("Registro de Solicitudes de Soporte Técnico")

    supportOrders = [
        {
            "orderId": 101,
            "customerName": "Empresa Alfa S.A.",
            "devicesList": ["Servidor Dell R740", "Switch Cisco 2960", "Router MikroTik CCR"]
        },
        {
            "orderId": 102,
            "customerName": "Tecnologías Beta",
            "devicesList": ["Laptop Lenovo ThinkPad", "Impresora HP LaserJet"]
        },
        {
            "orderId": 103,
            "customerName": "Servicios Gamma",
            "devicesList": ["Firewall Fortinet 60F"]
        },
        {
            "orderId": 104,
            "customerName": "Corporación Delta",
            "devicesList": ["UPS APC 1500VA", "Switch PoE UniFi", "Punto de Acceso Ubiquiti", "NAS Synology"]
        }
    ]

    print("Resumen de órdenes de soporte:")
    for orderItem in supportOrders:
        orderId = orderItem["orderId"]
        customerName = orderItem["customerName"]
        devicesList = orderItem["devicesList"]
        deviceCount = len(devicesList)

        print(f"\nOrden #{orderId} - Cliente: {customerName}")
        print(f"  Cantidad de dispositivos: {deviceCount}")
        print(f"  Dispositivos: {', '.join(devicesList)}")

    totalDevices = sum(len(order["devicesList"]) for order in supportOrders)
    printSuccess(f"\nTotal general de dispositivos en soporte: {totalDevices}")


if __name__ == "__main__":
    supportRequestLog()