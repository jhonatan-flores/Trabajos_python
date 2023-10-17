#crear un sistema para gestion o control de stock de productos.
# caso de uso
# historias de usuario
# producto ower
# baclog
# MVP
# prototipos de Mierda

# entidades entitis 
# la base de datos sobre lo que voy a trabajar
# averiguar formas normales(normalizacion de base de datos)

# casos de uso
class Producto:
    def __init__(self ,nombre, descripcion, stock,unidad, precio, moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
# creacion de productos
def mostrar_productos(self):
    mensaje=f'''
    tienes {len(productos)}
    los productos son: {productos}
    '''
    return mensaje


def registrar_producto(self):
    nuevo_id=len(productos)+1
    producto_nuevo={
        "id":nuevo_id,
        "nombre":self.nombre,
        "descricion":self.descripcion,
        "stock":self.stock,
        "unidad":self.unidad,
        "moneda":self.moneda
    }
    registro_producto=productos.append
    (producto_nuevo)
    return f'El siguiente producto se registro exitosamente:{producto_nuevo}'

def mostrar_producto(self,id):
    producto_buscar=productos[id-1]
    return producto_buscar

def eliminar_producto(self,id):
    producto_eliminar=productos.pop(id-1)
    return f'el siguente producto fue eliminado exitosamente{producto_eliminar}'

def actualizar_producto(self,id):
    pass
produc=Producto ("aceite","extra virgen",2,"litro x botella",12)

print(produc.registrar_productos())
print(produc.mostrar_productos())
print(produc.mostrar_producto(1))
print(produc.eliminar_producto(1))
print(produc.mostrar_productos())
