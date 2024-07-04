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

from flask import Flask, request, render_template_string
import openpyxl
import pandas
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Ruta para la página principal que muestra el formulario
@app.route('/')
def index():
    # Renderiza el formulario HTML
    return render_template_string(open('index.html').read())

# Ruta para procesar los datos enviados desde el formulario
@app.route('/procesar', methods=['POST'])
def procesar():
    # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
    urls = request.form['urls'].split('\n')
    data = []

    # Iterar sobre cada URL para extraer la información del producto
    for url in urls:
        response = requests.get(url.strip())  # Realizar la solicitud HTTP a la URL
        soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML
        
        # Extraer el nombre y el precio del producto usando selectores CSS
        # Ajusta los selectores según la estructura de la página de Mercado Libre
        nombre = soup.select_one('h1').text if soup.select_one('h1') else 'N/A'
        precio_entero = soup.select_one('span.andes-money-amount__fraction').text if soup.select_one('span.andes-money-amount__fraction') else 'N/A'
        precio_decimal = soup.select_one('span.andes-money-amount__cents').text if soup.select_one('span.andes-money-amount__cents') else '00'
        
        # Combinar la parte entera y decimal del precio
        precio = f"{precio_entero},{precio_decimal}" if precio_entero != 'N/A' else 'N/A'
        
        condicion = soup.select_one("span.ui-pdp-subtitle").text if soup.select_one("span.ui-pdp-subtitle") else 'N/A'
        
        # Solo agregar el producto si la condición es "Usado"
        if condicion.lower() == "usado":
            categoria = soup.select_one('a.andes-breadcrumb__item').text if soup.select_one('a.andes-breadcrumb__item') else 'N/A'
            descripcion = soup.select_one('div.ui-pdp-collapsable__container').text if soup.select_one('div.ui-pdp-collapsable__container') else 'N/A'

            # Agregar los datos extraídos a la lista
            data.append({'Nombre del producto': nombre, 'Precio': precio, "Condicion": condicion, 'Categoria': categoria, 'Descripcion': descripcion})

    # Crear un DataFrame de pandas con los datos extraídos
    df = pandas.DataFrame(data)
    # Guardar el DataFrame en un archivo Excel
    df.to_excel('productos.xlsx', index=False)
    
    print(data)

    # Devolver un mensaje de éxito
    return 'Archivo Excel generado con éxito.'

# Ruta para extraer hipervínculos de un archivo Excel y guardarlos en otro archivo Excel
@app.route('/extract_links', methods=['POST'])
def extract_links():
    # Obtener las URLs ingresadas en el formulario y dividirlas en una lista
    file = request.files['file']
    
    # Abre el libro de Excel
    workbook = openpyxl.load_workbook(file)
    sheet = workbook['Links']  # Cambia el nombre de la hoja según sea necesario

    data = []

    # Recorre las filas y extrae los hipervínculos
    for row in sheet.iter_rows():
        cell = row[2]  # Cambia el índice de columna según sea necesario
        if cell.hyperlink:
            nombre = cell.value
            urls = cell.hyperlink.target

            # Agregar los datos extraídos a la lista
            data.append({'Nombre del producto': nombre, 'URL': urls})

    # Crear un DataFrame de pandas con los datos extraídos
    df = pandas.DataFrame(data)
    # Guardar el DataFrame en un archivo Excel
    df.to_excel('URLs.xlsx', index=False)
    
    print(data)

    return "Nombres y URLs extraídos y guardados en 'URLs.xlsx'"

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
    

    
        
        
    
