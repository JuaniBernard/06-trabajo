from repositorios import Repositorios


class ProductoService:
    def add_producto(self, producto):
        key = len(Repositorios.productosList)
        while key in Repositorios.productosList:
            key = key + 1
        Repositorios.productosList[key] = producto.__dict__
        return key

    def update_producto(self, key, producto):
        if key in Repositorios.productosList:
            Repositorios.productosList[key]['_descripcion'] = producto.\
                _descripcion
            Repositorios.productosList[key]['_precio'] = producto._precio
            Repositorios.productosList[key]['_tipo'] = producto._tipo
        else:
            raise ValueError("ID de producto incorrecta.")

    def delete_producto(self, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
        else:
            raise ValueError("ID de producto incorrecta.")

    def get_productosList(self):
        return Repositorios.productosList

    def insertion_sort_precio(self, lista, orden):
        lista1 = lista.copy()
        if orden == 'ascendente':
            for i in range(1, len(lista1)):
                valor = lista1[i]
                j = i-1
                while j >= 0 and valor['_precio'] < lista1[j]['_precio']:
                    lista1[j + 1] = lista1[j]
                    j -= 1
                lista1[j + 1] = valor
            return lista1
        if orden == 'descendente':
            for i in range(1, len(lista1)):
                valor = lista1[i]
                j = i-1
                while j >= 0 and valor['_precio'] > lista1[j]['_precio']:
                    lista1[j + 1] = lista1[j]
                    j -= 1
                lista1[j + 1] = valor
            return lista1
