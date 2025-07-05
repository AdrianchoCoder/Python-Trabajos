import json
import os

class Glamping:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    _archivo_json = os.path.join(BASE_DIR, '../data/glampings.json')

    def __init__(self, id=None, nombre='', capacidad=0, precio_por_noche=0.0, descripcion=''):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.precio_por_noche = precio_por_noche
        self.descripcion = descripcion

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "capacidad": self.capacidad,
            "precio_por_noche": self.precio_por_noche,
            "descripcion": self.descripcion
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=int(data.get("id")) if data.get("id") else None,
            nombre=data.get("nombre", ""),
            capacidad=int(data.get("capacidad", 0)),
            precio_por_noche=float(data.get("precio_por_noche", 0)),
            descripcion=data.get("descripcion", "")
        )

    def guardar(self):
        glampings = self.cargar_todos()

        if not self.id:
            self.id = max((g['id'] for g in glampings), default=0) + 1
        else:
            self.id = int(self.id)

        glampings = [g for g in glampings if g['id'] != self.id]
        glampings.append(self.to_dict())

        self._guardar_todos(glampings)
        return True

    @classmethod
    def cargar_todos(cls):
        if not os.path.exists(cls._archivo_json):
            cls._guardar_todos([])

        with open(cls._archivo_json, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            return json.loads(contenido) if contenido else []

    @classmethod
    def _guardar_todos(cls, glampings):
        with open(cls._archivo_json, 'w', encoding='utf-8') as f:
            json.dump(glampings, f, indent=4)

    @classmethod
    def obtener_glampings(cls):
        return [cls.from_dict(data) for data in cls.cargar_todos()]

    @classmethod
    def obtener_glamping_por_id(cls, id):
        return next((g for g in cls.obtener_glampings() if g.id == id), None)

    @classmethod
    def eliminar_glamping_por_id(cls, id):
        glampings = [g for g in cls.cargar_todos() if g['id'] != id]
        cls._guardar_todos(glampings)
        return True
