# Importar la clase para generar un mixin de soft delete
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class
# Importar la clase para definir tablas que se ignoran en el soft delete
from sqlalchemy_easy_softdelete.hook import IgnoredTable
# Importar el tipo de dato datetime para manejar fechas
from datetime import datetime

# Definición de un Mixin para soft delete utilizando una clase generada
class SoftDeleteMixin(generate_soft_delete_mixin_class(ignored_tables=[IgnoredTable(table_schema="public", name="roles"),])):  
    """
    Mixin para soft delete
    Este mixin permite implementar una funcionalidad de eliminación suave 
    en los modelos de SQLAlchemy, lo que significa que en lugar de eliminar 
    físicamente una fila de la base de datos, se marca como eliminada 
    estableciendo un valor en la columna 'deleted_at'.
    
    Más información en la documentación: https://pypi.org/project/sqlalchemy-easy-softdelete/
    """
    
    deleted_at: datetime  # Atributo para almacenar la fecha y hora de la eliminación suave
