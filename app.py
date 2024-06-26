# from flask import Flask, request, render_template_string
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template_string(open('formulario.html').read())

# @app.route('/procesar', methods=['POST'])
# def procesar():
#     urls = request.form['urls'].split('\n')
#     nombres = []
#     precios = []

#     for url in urls:
#         if url.strip():
#             response = requests.get(url.strip())
#             soup = BeautifulSoup(response.content, 'html.parser')
#             nombre = soup.find('h1', {'class': 'ui-pdp-title'}).text.strip()
#             precio = soup.find('span', {'class': 'price-tag-fraction'}).text.strip()
#             nombres.append(nombre)
#             precios.append(precio)

#     df = pd.DataFrame({'Nombre': nombres, 'Precio': precios})
#     df.to_excel('productos.xlsx', index=False)

#     return 'Archivo Excel generado con éxito.'

# if __name__ == '__main__':
#     app.run(debug=True)



# ---------------------------------------------------------------------------------------------
# SEGUNDO INTENTO
# -----------------------------------------------------

# from flask import Flask, request, render_template_string
# import requests
# from bs4 import BeautifulSoup
# import pandas 

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template_string(open('index.html').read())

# @app.route('/procesar', methods=['POST'])
# def procesar():
#     urls = request.form['urls'].split('\n')
#     nombres = []
#     precios = []

#     for url in urls:
#         if url.strip():
#             response = requests.get(url.strip())
#             soup = BeautifulSoup(response.content, 'html.parser')
#             nombre_element = soup.find('h1', {'class': 'ui-pdp-title'}).text.strip()
#             precio_element = soup.find('span', {'class': 'price-tag-fraction'}).text.strip()
            
#             if nombre_element and precio_element:
#                 nombre = nombre_element.text.strip()
#                 precio = precio_element.text.strip()
#                 nombres.append(nombre)
#                 precios.append(precio)
#             else:
#                 nombres.append('No encontrado')
#                 precios.append('No encontrado')

#     df = pandas.DataFrame({'Nombre': nombres, 'Precio': precios})
#     df.to_excel('productos.xlsx', index=False)

#     return 'Archivo Excel generado con éxito.'

# if __name__ == '__main__':
#     app.run(debug=True)


# ----------------------------------------------------------------------------
# TERCER INTENTO
# --------------------------------------------------------------------------

# import requests
# from bs4 import BeautifulSoup
# import pandas
# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template_string(open('index.html').read())

# @app.route('/procesar', methods=['POST'])
# def procesar():
#     urls = request.form['urls'].split('\n')
#     # Listas para almacenar los datos
#     nombres = []
#     precios = []
    
#     # Función para extraer datos de una URL
#     # Iterar sobre las URLs y extraer datos
#     for url in urls:
#         if url.strip():
#             response = requests.get(url.strip())
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Extraer nombre del producto
#             nombre_element = soup.find('h1', {'class': 'ui-pdp-title'})
#             if nombre_element:
#                 nombre = nombre_element.text.strip()
#             else:
#                 nombre = 'No encontrado'
                
#             # Extraer precio del producto
#             precio_element = soup.find('span', {'class': 'price-tag-fraction'})
#             if precio_element:
#                 precio = precio_element.text.strip()
#             else:
#                 precio = 'No encontrado'
                
#             nombres.append(nombre)
#             precios.append(precio)
            
#     df = pandas.DataFrame({'Nombre': nombres, 'Precio': precios})
#     df.to_excel('productos.xlsx', index=False)
#     return 'Archivo Excel generado con éxito.'

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    
# -------------------------------------------------------------------------------
# CUARTO INTENTO
# -------------------------------------------------------------
from flask import Flask, request, render_template_string
import requests
from bs4 import BeautifulSoup
import pandas

# Crear una instancia de la aplicación Flask
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
        nombre = soup.select_one('h1').text.strip()
        precio = soup.select_one('span.andes-money-amount__fraction').text.strip()
        
        # Agregar los datos extraídos a la lista
        data.append({'Nombre': nombre, 'Precio': precio})
        print(data)

    # Crear un DataFrame de pandas con los datos extraídos
    df = pandas.DataFrame(data)
    # Guardar el DataFrame en un archivo Excel
    df.to_excel('productos.xlsx', index=False)

    # Devolver un mensaje de éxito
    return 'Archivo Excel generado con éxito.'

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
    
