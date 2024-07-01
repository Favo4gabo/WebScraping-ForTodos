# from flask import Flask, request, render_template_string
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
#         nombre = soup.select_one('h1').text.strip()
#         precio = soup.select_one('span.andes-money-amount__fraction').text.strip()
        
#         # Agregar los datos extraídos a la lista
#         data.append({'Nombre del producto': nombre, 'Precio': precio})
#         print(data)

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('productos.xlsx', index=False)

#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito.'

# # Ejecutar la aplicación Flask
# if __name__ == '__main__':
#     app.run(debug=True)




# -------------------------------------------

# import pandas
# import json

# # Read excel document
# excel_data_df = pandas.read_excel('data.xlsx', sheet_name='Links')

# # Convert excel to string 
# # (define orientation of document in this case from up to down)
# thisisjson = excel_data_df.to_json(orient='records')

# # Print out the result
# print('Excel Sheet to JSON:\n', thisisjson)

# # Make the string into a list to be able to input in to a JSON-file
# thisisjson_dict = json.loads(thisisjson)

# # Extrae la propiedad "Link a ML" de cada diccionario, si existe
# links_a_ml = [item.get("Link a ML") for item in thisisjson_dict if "Link a ML" in item]

# # Crear un nuevo diccionario para almacenar los links
# output_data = {"Links a ML": links_a_ml}

# # Guardar en un nuevo archivo JSON
# with open('output.json', 'w') as outfile:
#     json.dump(output_data, outfile, indent=4)

# print("Datos guardados en 'output.json'")


# ------------------------------------------------------------------------------


import openpyxl
import pandas
import requests
from bs4 import BeautifulSoup




    
# Abre el libro de Excel
workbook = openpyxl.load_workbook('data.xlsx')
sheet = workbook['Links']  # Cambia el nombre de la hoja según sea necesario

# Recorre las filas y extrae los hipervínculos
for row in sheet.iter_rows():
    cell = row[2]  # Cambia el índice de columna según sea necesario
    if cell.hyperlink:
        print(f"Texto: {cell.value}, URL: {cell.hyperlink.target}")

    nombre = cell.value
    urls = cell.hyperlink.target
    data = []
    
    for url in urls:
        response = requests.get(url.strip())  # Realizar la solicitud HTTP a la URL
        soup = BeautifulSoup(response.content, 'html.parser')  # Parsear el contenido HTML
        
        # Extraer el nombre y el precio del producto usando selectores CSS
        # Ajusta los selectores según la estructura de la página de Mercado Libre
        precio = soup.select_one('span.andes-money-amount__fraction').text.strip()


    # Agregar los datos extraídos a la lista
    data.append({'Nombre del producto': nombre, 'URL': urls, 'Precio': precio})
    # print(data)

    # Crear un DataFrame de pandas con los datos extraídos
    df = pandas.DataFrame(data)
    # Guardar el DataFrame en un archivo Excel
    df.to_excel('productos.xlsx', index=False)
        
# ------------------------------------------------------------------------------
    

    
        
        
    
