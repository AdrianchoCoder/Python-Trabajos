import json
import os
from datetime import datetime

class Reserva:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    _archivo_json = os.path.join(BASE_DIR, '../data/reservas.json')

    def __init__(self, id=None, cliente=None, glamping=None, fecha_inicio='', fecha_fin='', total_pagado=0.0, estado='pendiente'):
        self.id = id
        self.cliente = cliente
        self.glamping = glamping
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.total_pagado = total_pagado
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "clienteId": self.cliente.id if self.cliente else None,
            "glampingId": self.glamping.id if self.glamping else None,
            "fechaInicio": self.fecha_inicio,
            "fechaFin": self.fecha_fin,
            "totalPagado": self.total_pagado,
            "estado": self.estado
        }

    @classmethod
    def from_dict(cls, data, cliente, glamping):
        return cls(
            id=int(data.get("id")) if data.get("id") else None,
            cliente=cliente,
            glamping=glamping,
            fecha_inicio=data.get("fechaInicio", ""),
            fecha_fin=data.get("fechaFin", ""),
            total_pagado=float(data.get("totalPagado", 0)),
            estado=data.get("estado", "pendiente")
        )

    def guardar(self):
        reservas = self.cargar_todos()

        if not self.id:
            self.id = max((r['id'] for r in reservas), default=0) + 1
        else:
            self.id = int(self.id)

        reservas = [r for r in reservas if r['id'] != self.id]
        reservas.append(self.to_dict())

        self._guardar_todos(reservas)
        return True

    @classmethod
    def cargar_todos(cls):
        if not os.path.exists(cls._archivo_json):
            cls._guardar_todos([])

        with open(cls._archivo_json, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            return json.loads(contenido) if contenido else []

    @classmethod
    def _guardar_todos(cls, reservas):
        with open(cls._archivo_json, 'w', encoding='utf-8') as f:
            json.dump(reservas, f, indent=4)

    @classmethod
    def obtener_reservas(cls, clientes, glampings):
        raw = cls.cargar_todos()
        reservas = []
        for r in raw:
            cliente = next((c for c in clientes if c.id == r['clienteId']), None)
            glamping = next((g for g in glampings if g.id == r['glampingId']), None)
            if cliente and glamping:
                reservas.append(cls.from_dict(r, cliente, glamping))
        return reservas

    @classmethod
    def eliminar_reserva_por_id(cls, id):
        reservas = [r for r in cls.cargar_todos() if r['id'] != id]
        cls._guardar_todos(reservas)
        return True
