from typing import List
from app.models import Diet
from app import db

class DietRepository:
    def save(self, diet: Diet) -> Diet:
        db.session.add(diet)  # Añade el objeto Diet a la sesión de la base de datos.
        db.session.commit()  # Confirma los cambios en la base de datos.
        return diet  # Retorna la instancia guardada de Diet.
    
    def delete(self, diet: Diet) -> None:
        db.session.delete(diet)  # Elimina el objeto Diet de la sesión de la base de datos.
        db.session.commit()  # Confirma los cambios en la base de datos.

    def find(self, id: int) -> Diet:
        return db.session.query(Diet).filter(Diet.id == id).one_or_none()
        # Realiza una consulta en la base de datos para buscar una Diet por su ID.
        # Retorna la instancia encontrada o None si no se encuentra ningún resultado.
    
    def all(self) -> List[Diet]:
        return db.session.query(Diet).all()
        # Realiza una consulta para obtener todas las Dietas almacenadas en la base de datos.
        # Retorna una lista con todas las instancias de Diet.
    
    def find_by_name(self, name: str) -> Diet:
        return db.session.query(Diet).filter(Diet.name == name).one_or_none()
        # Realiza una consulta en la base de datos para buscar una Diet por su nombre.
        # Retorna la instancia encontrada o None si no se encuentra ningún resultado.
