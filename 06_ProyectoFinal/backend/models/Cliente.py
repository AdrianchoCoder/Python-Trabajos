import json
import os

class Cliente:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    _archivo_json = os.path.join(BASE_DIR, '../data/clientes.json')

    def __init__(self, id=None, nombre='', email='', telefono='', documento=''):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.documento = documento

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "documento": self.documento
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=int(data.get("id")) if data.get("id") else None,
            nombre=data.get("nombre", ""),
            email=data.get("email", ""),
            telefono=data.get("telefono", ""),
            documento=data.get("documento", "")
        )

    def guardar(self):
        clientes = self.cargar_todos()

        if not self.id:
            self.id = max((c['id'] for c in clientes), default=0) + 1
        else:
            self.id = int(self.id)

        # Reemplaza si ya existe, o agrega si es nuevo
        clientes = [c for c in clientes if c['id'] != self.id]
        clientes.append(self.to_dict())

        self._guardar_todos(clientes)
        return True

    @classmethod
    def cargar_todos(cls):
        if not os.path.exists(cls._archivo_json):
            cls._guardar_todos([])

        with open(cls._archivo_json, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            return json.loads(contenido) if contenido else []

    @classmethod
    def _guardar_todos(cls, clientes):
        with open(cls._archivo_json, 'w', encoding='utf-8') as f:
            json.dump(clientes, f, indent=4)

    @classmethod
    def obtener_clientes(cls):
        return [cls.from_dict(data) for data in cls.cargar_todos()]

    @classmethod
    def obtener_cliente_por_id(cls, id):
        return next((c for c in cls.obtener_clientes() if c.id == id), None)

    @classmethod
    def eliminar_cliente_por_id(cls, id):
        clientes = [c for c in cls.cargar_todos() if c['id'] != id]
        cls._guardar_todos(clientes)
        return True
