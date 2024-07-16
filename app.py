# from flask import Flask, request, render_template_string
# import openpyxl
# import pandas
# import requests
# from bs4 import BeautifulSoup

# # Crear una instancia de la aplicación Flask
# app = Flask(__name__)

# # Ruta para la página principal que muestra el formulario
# @app.route('/')
# def index():
#     # Renderiza el formulario HTML
#     return render_template_string(open('index.html').read())


# # Ruta para procesar los datos enviados desde el formulario (automatico)
# @app.route('/automatico', methods=['POST'])
# def automatico():
#     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
#     file = request.files['file']
#     # urls = request.form['urls'].split('\n')
    
#     # Guardar un archivo
#     # file.save(file.filename)
    
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook['Links']  # Cambia el nombre de la hoja según sea necesario

#     data = []

#     # Recorre las filas y extrae los hipervínculos
#     for row in sheet.iter_rows():
#         cell = row[2]  # Cambia el índice de columna según sea necesario
#         if cell.hyperlink:            
#             urls = cell.hyperlink.target
#             # nombre = cell.value
                                        
#             # # Agregar las urls extraídas a la lista            
#             data.append(urls)

#     print(data)
    
#     for url in data:
#         response = requests.get(url)  # Realizar la solicitud HTTP a la URL
#         soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML
        
#         # Extraer el nombre y el precio del producto usando selectores CSS
#         # Ajusta los selectores según la estructura de la página de Mercado Libre
#         nombre_tag = soup.select_one('h1')
#         if nombre_tag is not None:
#             nombre = nombre_tag.text.strip()
#         precio_tag = soup.select_one('span.andes-money-amount__fraction')
#         if precio_tag is not None:
#             precio = precio_tag.text.strip()
#         condicion_tag = soup.select_one('span.ui-pdp-subtitle')
#         if condicion_tag is not None:
#             condicion = condicion_tag.text.strip()
        
#         # Agregar los datos extraídos a la lista
#         data.append({'Nombre del producto': nombre, 'Precio': precio, 'Condicion':condicion})
#         print(data)

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('productos_2°Intento.xlsx', index=False)

#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito (Automatico).'


# # Ruta para procesar los datos enviados desde el formulario
# @app.route('/manual', methods=['POST'])
# def manual():
#     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
#     urls = request.form['urls'].split('\n')
#     data = []

#     # Iterar sobre cada URL para extraer la información del producto
#     for url in urls:
#         response = requests.get(url.strip())  # Realizar la solicitud HTTP a la URL
#         soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML
        
#         # Extraer el nombre y el precio del producto usando selectores CSS
#         # Ajusta los selectores según la estructura de la página de Mercado Libre
#         nombre = soup.select_one('h1').text if soup.select_one('h1') else 'N/A'
#         precio = soup.select_one('span.andes-money-amount__fraction').text if soup.select_one('span.andes-money-amount__fraction') else 'N/A'
#         condicion = soup.select_one("span.ui-pdp-subtitle").text if soup.select_one("span.ui-pdp-subtitle") else 'N/A'
        
#         # Agregar los datos extraídos a la lista
#         data.append({'Nombre del producto': nombre, 'Precio': precio, "Condicion": condicion})

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('productos.xlsx', index=False)

#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito (Manual).'
    
# if __name__ == '__main__':
#     app.run(debug=True)
    


# # ------------------------------------------------------------------------------
# # CODIGO POR PARTES
# # ------------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ESTE FUNCIONA
# -------------------------------------------------------------------------------

# from flask import Flask, request, render_template_string
# import openpyxl
# import pandas
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# # Ruta para la página principal que muestra el formulario
# @app.route('/')
# def index():
#     # Renderiza el formulario HTML
#     return render_template_string(open('index.html').read())

# # Ruta para procesar los datos enviados desde el formulario
# @app.route('/procesar', methods=['POST'])
# def procesar():
#     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
#     urls = request.form['urls'].split('\n')
#     data = []

#     # Iterar sobre cada URL para extraer la información del producto
#     for url in urls:
#         response = requests.get(url.strip())  # Realizar la solicitud HTTP a la URL
#         soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML
        
#         # Extraer el nombre y el precio del producto usando selectores CSS
#         # Ajusta los selectores según la estructura de la página de Mercado Libre
#         nombre = soup.select_one('h1').text if soup.select_one('h1') else 'N/A'
#         precio_entero = soup.select_one('span.andes-money-amount__fraction').text if soup.select_one('span.andes-money-amount__fraction') else 'N/A'
#         precio_decimal = soup.select_one('span.andes-money-amount__cents').text if soup.select_one('span.andes-money-amount__cents') else '00'
        
#         # Combinar la parte entera y decimal del precio
#         precio = f"{precio_entero},{precio_decimal}" if precio_entero != 'N/A' else 'N/A'
        
#         # condicion = soup.select_one("span.ui-pdp-subtitle").text if soup.select_one("span.ui-pdp-subtitle") else 'N/A'
        
#         # # # # Solo agregar el producto si la condición es "Usado"
#         # # if condicion == "Usado":
#         # categoria = soup.select_one('a.andes-breadcrumb__item').text if soup.select_one('a.andes-breadcrumb__item') else 'N/A'
#         descripcion_1 = soup.select_one('div.ui-pdp-description').text if soup.select_one('p.ui-pdp-description__content') else 'N/A'
#         descripcion_2 = soup.select_one('div.ui-pdp-collapsable__container').text if soup.select_one('div.ui-pdp-collapsable__container') else 'N/A'
#         descripcion_3 = soup.select_one('p.ui-pdp-description__content').text if soup.select_one('p.ui-pdp-description__content') else 'N/A'    
#         # Extraer URLs de las imágenes
#         imagenes = soup.select('img.ui-pdp-image.ui-pdp-gallery__figure__image')
#         imagen_1 = imagenes[0].get('data-zoom', imagenes[0].get('src')) if len(imagenes) > 0 else 'N/A'
#         imagen_2 = imagenes[1].get('data-zoom', imagenes[1].get('src')) if len(imagenes) > 1 else 'N/A'

#         # Agregar los datos extraídos a la lista
#         # data.append({'Nombre del producto': nombre, 'Precio': precio, "Condicion": condicion, 'Categoria': categoria, 'Descripcion': descripcion})
#         data.append({'Nombre': nombre, 'Descripcion':descripcion_1, 'Descripcion 2':descripcion_2, 'Imagen 1': imagen_1, 'Imagen 2': imagen_2, 'Precio': precio})

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('Productos.xlsx', index=False)
    
#     print(data)

#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito.'

# # Ruta para extraer hipervínculos de un archivo Excel y guardarlos en otro archivo Excel
# @app.route('/extract_links', methods=['POST'])
# def extract_links():
#     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
#     file = request.files['file']
    
#     # Abre el libro de Excel
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook['Links']  # Cambia el nombre de la hoja según sea necesario

#     data = []

#     # Recorre las filas y extrae los hipervínculos
#     for row in sheet.iter_rows():
#         cell = row[2]  # Cambia el índice de columna según sea necesario
#         if cell.hyperlink:
#             nombre = cell.value
#             urls = cell.hyperlink.target

#             # Agregar los datos extraídos a la lista
#             data.append({'Nombre del producto': nombre, 'URL': urls})

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('URLs.xlsx', index=False)
    
#     print(data)

#     return "Nombres y URLs extraídos y guardados en 'URLs.xlsx'"

# # Ejecutar la aplicación Flask
# if __name__ == '__main__':
#     app.run(debug=True)
    


# ------------------------------------------------------------------------------------------
# ESTE ES EL QUE SIRVE
# -------------------------------------------------------------------------------------------------


# from flask import Flask, request, render_template_string
# import openpyxl
# import pandas
# import requests
# from bs4 import BeautifulSoup
# import time

# app = Flask(__name__)

# # Ruta para la página principal que muestra el formulario
# @app.route('/')
# def index():
#     # Renderiza el formulario HTML
#     return render_template_string(open('index.html').read())

# # Ruta para procesar los datos enviados desde el formulario
# @app.route('/procesar', methods=['POST'])
# def procesar():
#     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
#     urls = request.form['urls'].split('\n')
#     data = []

#     # Iterar sobre cada URL para extraer la información del producto
#     for url in urls:
#         # try:
#             response = requests.get(url.strip())  # Realizar la solicitud HTTP a la URL
#             response.raise_for_status()  # Verificar si la solicitud fue exitosa
#             soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML                        
            
#             # # Extraer el nombre y el precio del producto usando selectores CSS
#             nombre = soup.select_one('h1').text if soup.select_one('h1') else 'N/A'
            
#             precio_entero = soup.select_one('span.andes-money-amount__fraction').text if soup.select_one('span.andes-money-amount__fraction') else 'N/A'
#             precio_decimal = soup.select_one('span.andes-money-amount__cents').text if soup.select_one('span.andes-money-amount__cents') else '00'            
#             # Combinar la parte entera y decimal del precio
#             precio = f"{precio_entero},{precio_decimal}" if precio_entero != 'N/A' else 'N/A'

#             # Extraer URLs de las imágenes
#             imagenes = soup.select('img.ui-pdp-image.ui-pdp-gallery__figure__image')
#             imagen_1 = imagenes[0].get('data-zoom', imagenes[0].get('src')) if len(imagenes) > 0 else 'N/A'
#             imagen_2 = imagenes[1].get('data-zoom', imagenes[1].get('src')) if len(imagenes) > 1 else 'N/A'
            
#             condicion_tag = soup.select_one('span.ui-pdp-subtitle')
#             if condicion_tag is not None:
#               condicion = condicion_tag.text.strip()
              
#             descripcion = soup.select_one("p.ui-pdp-description__content").text.strip() if soup.select_one('p.ui-pdp-description__content') else "Descripcion no encontrada"
#             descripcion2 = soup.select_one("div.ui-pdp-description").text.strip() if soup.select_one('div.ui-pdp-description') else "Descripcion no encontrada"

#             # Agregar los datos extraídos a la lista
#             data.append({'Nombre':nombre, 'Precio':precio, 'Condicion': condicion, 'Descripcion': descripcion, 'Descripcion 2': descripcion2, 'Imagen 1': imagen_1, 'Imagen 2': imagen_2 })            

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('Productos.xlsx', index=False)
    
#     print(data)

#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito.'

# # Ruta para extraer hipervínculos de un archivo Excel y guardarlos en otro archivo Excel
# # @app.route('/extract_links', methods=['POST'])
# # def extract_links():
# #     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
# #     file = request.files['file']
    
# #     # Abre el libro de Excel
# #     workbook = openpyxl.load_workbook(file)
# #     sheet = workbook['Links']  # Cambia el nombre de la hoja según sea necesario

# #     data = []

# #     # Recorre las filas y extrae los hipervínculos
# #     for row in sheet.iter_rows():
# #         cell = row[2]  # Cambia el índice de columna según sea necesario
# #         if cell.hyperlink:
# #             nombre = cell.value
# #             urls = cell.hyperlink.target

# #             # Agregar los datos extraídos a la lista
# #             data.append({'Nombre del producto': nombre, 'URL': urls})

# #     # Crear un DataFrame de pandas con los datos extraídos
# #     df = pandas.DataFrame(data)
# #     # Guardar el DataFrame en un archivo Excel
# #     df.to_excel('URLs.xlsx', index=False)
    
# #     print(data)

# #     return "Nombres y URLs extraídos y guardados en 'URLs.xlsx'"

# # Ejecutar la aplicación Flask
# if __name__ == '__main__':
#     app.run(debug=True)




# -------------------------------------------------------------------


# ESTE ES EL MISMO CODIGO QUE SIRVE PERO SIN EL OTRO ENDPOINT

# from flask import Flask, request, render_template_string
# import openpyxl
# import pandas
# import requests
# from bs4 import BeautifulSoup
# import time

# app = Flask(__name__)

# # Ruta para la página principal que muestra el formulario
# @app.route('/')
# def index():
#     # Renderiza el formulario HTML
#     return render_template_string(open('index.html').read())

# # Ruta para procesar los datos enviados desde el formulario
# @app.route('/procesar', methods=['POST'])
# def procesar():
#     # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
#     urls = request.form['urls'].split('\n')
#     data = []

#     # Iterar sobre cada URL para extraer la información del producto
#     for url in urls:
#         # try:
#             response = requests.get(url.strip())  # Realizar la solicitud HTTP a la URL
#             response.raise_for_status()  # Verificar si la solicitud fue exitosa
#             soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML                        
            
#             # # Extraer el nombre y el precio del producto usando selectores CSS
#             nombre = soup.select_one('h1').text if soup.select_one('h1') else 'N/A'
            
#             precio_entero = soup.select_one('span.andes-money-amount__fraction').text if soup.select_one('span.andes-money-amount__fraction') else 'N/A'
#             precio_decimal = soup.select_one('span.andes-money-amount__cents').text if soup.select_one('span.andes-money-amount__cents') else '00'            
#             # Combinar la parte entera y decimal del precio
#             precio = f"{precio_entero},{precio_decimal}" if precio_entero != 'N/A' else 'N/A'

#             # Extraer URLs de las imágenes
#             imagenes = soup.select('img.ui-pdp-image.ui-pdp-gallery__figure__image')
#             imagen_1 = imagenes[0].get('data-zoom', imagenes[0].get('src')) if len(imagenes) > 0 else 'N/A'
#             imagen_2 = imagenes[1].get('data-zoom', imagenes[1].get('src')) if len(imagenes) > 1 else 'N/A'
            
#             condicion_tag = soup.select_one('span.ui-pdp-subtitle')
#             if condicion_tag is not None:
#               condicion = condicion_tag.text.strip()
              
#             descripcion = soup.select_one("p.ui-pdp-description__content").text.strip() if soup.select_one('p.ui-pdp-description__content') else "Descripcion no encontrada"
#             descripcion2 = soup.select_one("div.ui-pdp-description").text.strip() if soup.select_one('div.ui-pdp-description') else "Descripcion no encontrada"

#             # Agregar los datos extraídos a la lista
#             data.append({'Nombre':nombre, 'Precio':precio, 'Condicion': condicion, 'Descripcion': descripcion, 'Descripcion 2': descripcion2, 'Imagen 1': imagen_1, 'Imagen 2': imagen_2 })            

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('Productos.xlsx', index=False)
    
#     print(data)

#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito.'

# # Ejecutar la aplicación Flask
# if __name__ == '__main__':
#     app.run(debug=True)

# ---------------------------------------------------------------------------------------------



# ME AYUDE CON EL TUTORIAL

# import requests
# from bs4 import BeautifulSoup

# urls = 'https://articulo.mercadolibre.com.ve/MLV-727896380-etiquetas-blancas-avery-5160-de-25-x-67-cm-3600-piezas-_JM'

# response = requests.get(urls)

# soup = BeautifulSoup(response.content, 'html.parser')

# productos = soup.find_all('div', class_='ui-pdp-container ui-pdp-container--pdp')

# for producto in productos:
#     nombre = soup.find('h1', class_='ui-pdp-title').text
#     precio_entero = soup.find('span', class_='andes-money-amount__fraction').text
#     precio_decimal = soup.find('span', class_='andes-money-amount__cents').text
#     condicion = soup.find('span', class_='ui-pdp-subtitle').text
#     descripcion = soup.find('p', class_='ui-pdp-description__content').text
    
#     print(f"Nombre: {nombre}; | Precio: {precio_entero},{precio_decimal}; | Codicion: {condicion}; | Descripcion: {descripcion} ")
    
    
    



import requests
from bs4 import BeautifulSoup
import pandas

# Lista de URLs
urls = [
    'https://articulo.mercadolibre.com.ve/MLV-727896380-etiquetas-blancas-avery-5160-de-25-x-67-cm-3600-piezas-_JM',
    'https://articulo.mercadolibre.com.ve/MLV-725586032-escaner-epson-perfection-640u-color-plano-adaptador-usb-_JM',
    'https://articulo.mercadolibre.com.ve/MLV-726105772-impresora-epson-lx-800-matriz-de-punto-monocromatica-_JM',
    'https://articulo.mercadolibre.com.ve/MLV-726605292-impresora-hp-deskjet-400-c2642a-monocromatica-_JM'
]

nombres = []
precios = []
condiciones = []
descripciones = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # productos = soup.find_all('div', class_='ui-pdp-container ui-pdp-container--pdp')
    
    # for producto in productos:
    # Extrae la información que necesitas
    nombre = soup.find('h1', class_='ui-pdp-title').text
    precio_entero = soup.find('span', class_='andes-money-amount__fraction').text
    precio_decimal = soup.find('span', class_='andes-money-amount__cents').text
    condicion = soup.find('span', class_='ui-pdp-subtitle').text
    descripcion_element = soup.find('p', class_='ui-pdp-description__content')
    if descripcion_element:
        descripcion = descripcion_element.text
    else:
        descripcion = 'Descripción no encontrada'
    
    nombres.append(nombre)
    precios.append(f"{precio_entero},{precio_decimal}")
    condiciones.append(condicion)
    descripciones.append(descripcion)
    
df = pandas.DataFrame({
    'Nombres': nombres,
    'Precios': precios,
    'Condicion': condiciones,
    'Descripcion': descripciones,
})

df.to_excel('prueba_1.xlsx', index=False)
print('Excel generado con éxito')