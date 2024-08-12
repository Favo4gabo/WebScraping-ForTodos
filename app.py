# from bs4 import BeautifulSoup
# import requests
# import pandas
# # import openpyxl

# # # Leer el archivo excel con pandas y seleccionar la hoja del archivo
# # archivo = pandas.read_excel('URLs.xlsx', sheet_name='Sheet1')

# # # Extraer todos los datos de una columna específica
# # datos_columna = archivo['URL']

# # # Lista donde voy a guardar las urls
# # urls = datos_columna.tolist()  # Convertir la columna en una lista de URLs
# # print(urls)

# def generar_excel():

#     urls = ['https://articulo.mercadolibre.com.ve/MLV-794259392-plotter-hp-designjet-750-c-plus-36-pulgadas-modelo-c4709a-_JM',
#             'https://articulo.mercadolibre.com.ve/MLV-725586032-escaner-epson-perfection-640u-color-plano-adaptador-usb-_JM',
#             'https://articulo.mercadolibre.com.ve/MLV-731492352-modems-internet-banda-ancha-star-bridge-motorola-_JM']

#     data = []

#     for url in urls:
#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # Verificar si la solicitud fue exitosa
#             content = response.text

#             soup = BeautifulSoup(content, 'lxml')

#             box_1 = soup.find('div', class_='ui-pdp-container__row ui-pdp-container__row--description', id='description')
#             box_2 = soup.find('div', class_ = 'ui-pdp-container__row ui-pdp-component-list pr-16 pl-16')

#             if box_1:
#                 descripcion = box_1.find('p', class_='ui-pdp-description__content').get_text()
#                 print(descripcion)
#             else:
#                 print(f"No se encontró la descripción en la URL: {url}")
                
#             if box_2:
#                 condicion = box_2.find('span', class_ = 'ui-pdp-subtitle').get_text()
#             else:
#                 print(f"No se encontró la condicion en la URL: {url}")
                
#             if box_2:
#                 nombre = box_2.find('h1', class_ = 'ui-pdp-title').get_text()
#             else:
#                 print(f"No se encontró el nombre en la URL: {url}")

#         except requests.exceptions.RequestException as e:
#             print(f"Error al acceder a la URL {url}: {e}")
            
#     # Agregar los datos extraídos a la lista
#     data.append({'Nombre del producto': nombre, 'Condicion':condicion, 'Descripcion': descripcion, 'URLs': urls})
#     print(data)        

#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pandas.DataFrame(data)
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('prueba.xlsx', index=False)
    
#     # Devolver un mensaje de éxito
#     return 'Archivo Excel generado con éxito (Automatico).'


from bs4 import BeautifulSoup
import requests
import pandas as pd

def generar_excel():
    urls = [
        'https://articulo.mercadolibre.com.ve/MLV-794259392-plotter-hp-designjet-750-c-plus-36-pulgadas-modelo-c4709a-_JM',
        'https://articulo.mercadolibre.com.ve/MLV-725586032-escaner-epson-perfection-640u-color-plano-adaptador-usb-_JM',
        'https://articulo.mercadolibre.com.ve/MLV-731492352-modems-internet-banda-ancha-star-bridge-motorola-_JM'
    ]
    data = []

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            content = response.text

            soup = BeautifulSoup(content, 'lxml')

            box_1 = soup.find('div', class_='ui-pdp-container__row ui-pdp-container__row--description', id='description')
            box_2 = soup.find('div', class_='ui-pdp-container__row ui-pdp-component-list pr-16 pl-16')

            descripcion = box_1.find('p', class_='ui-pdp-description__content').get_text() if box_1 else "No se encontró la descripción"
            condicion = box_2.find('span', class_='ui-pdp-subtitle').get_text() if box_2 else "No se encontró la condición"
            nombre = box_2.find('h1', class_='ui-pdp-title').get_text() if box_2 else "No se encontró el nombre"

            data.append({
                'Nombre del producto': nombre,
                'Condición': condicion,
                'Descripción': descripcion,
                'URL': url
            })

        except requests.exceptions.RequestException as e:
            print(f"Error al acceder a la URL {url}: {e}")

    df = pd.DataFrame(data)
    df.to_excel('prueba.xlsx', index=False)
    return 'Archivo Excel generado con éxito.'

# Llamada a la función para generar el archivo Excel
print(generar_excel())