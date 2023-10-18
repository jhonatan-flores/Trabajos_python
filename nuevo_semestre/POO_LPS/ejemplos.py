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
producto=[ 
    {
        'id'         :1,
        'nombre'     :'arroz',
        'descripcion':'costeño costal x 100k',
        'stokc'      :5,
        'unidad'     :125,
        'moneda'     :'soles'
    }
]
# casos de uso
class Producto:
    # atributos de instancia
    def init(self,nombre,descripcion,stock,
    unidad,precio,moneda="soles"):
        self.nombre     =nombre
        self.descripcion=descripcion
        self.stock      =stock
        self.precio     =precio
        self.moneda     =moneda
    #creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""tienes {len(productos)} productos los productos son: {productos}"""
        return mensaje
    
    def registrar_producto(self):
        nuevo_id=len(producto)+1
        producto_nuevo={
            "id"         :nuevo_id,
            "nombre"     :self    .nombre,
            "descripcion":self    .descripcion,
            "stock"      :self    .stock,
            "unidad"     :self    .unidad,
            "precio"     :self    .precio,
            "moneda"     :self    .moneda
        
        }
        registro_producto=producto.append
        (producto_nuevo)
        return f"el sieguiente producto se registro exitosamente{producto_nuevo}"
        
    def mostrar_producto(self,id):
        producto_buscar=producto[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminar=producto.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"
        
    def actualizar_producto(self, id,clave,valor):
        el=valor
        producto_actualizar=list(filter(lambda el:el[clave]==id,productos))[0].update({valor:valor})
        return "se actualizo"
# programacion funcional en python 
# metodo funcuional filter retorna una lista con el elemnto que sea true de una lista 
# funciones lista anonimos o autoejecutados en python se les conoce como funciones 
# lambda-> funcion anonimo
# su uso estroctura 
        
prod=Producto("aceite","extra virgen",2,"botella x litro",12.50)
print(prod.registrar_producto())
print(prod.mostar_productos())
print(prod.actualizar_producto(125,"precio",130))
print(prod.mostrar_producto())