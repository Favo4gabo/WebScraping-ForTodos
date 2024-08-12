# from bs4 import BeautifulSoup
# import requests
# import pandas

# def generar_excel():
    
#     # Leer el archivo excel con pandas y seleccionar la hoja del archivo
#     archivo = pandas.read_excel('URLs.xlsx', sheet_name='Sheet1')

#     # Extraer todos los datos de una columna específica
#     datos_columna = archivo['URL']

#     # Lista donde voy a guardar las urls
#     urls = datos_columna.tolist()  # Convertir la columna en una lista de URLs
#     # print(urls)
    
#     #En caso de que quiera probar con las urls manual
#     # urls = ['https://articulo.mercadolibre.com.ve/MLV-794259392-plotter-hp-designjet-750-c-plus-36-pulgadas-modelo-c4709a-_JM',
#     #         'https://articulo.mercadolibre.com.ve/MLV-725586032-escaner-epson-perfection-640u-color-plano-adaptador-usb-_JM',
#     #         'https://articulo.mercadolibre.com.ve/MLV-731492352-modems-internet-banda-ancha-star-bridge-motorola-_JM']
    
#     data = []

#     for url in urls:
#         try:
            
#             # Respuesta de la solicitud HTTP a las urls
#             response = requests.get(url)
#             # Revisar el status de la solicitud en caso de un error
#             response.raise_for_status()
#             # Pasar el contenido de la pagina a texto
#             content = response.text
            
#             # Parsear el html de la pagina para hacer Webscraping
#             soup = BeautifulSoup(content, 'lxml')
            
#             # Definimos los contenedores en los que vamos a buscar para filtrar mejor
#             box_1 = soup.find('div', class_='ui-pdp-container__row ui-pdp-container__row--description', id='description')
#             box_2 = soup.find('div', class_='ui-pdp-container__row ui-pdp-component-list pr-16 pl-16')

#             descripcion = box_1.find('p', class_='ui-pdp-description__content').get_text() if box_1 else "No se encontró la descripción"
#             condicion = box_2.find('span', class_='ui-pdp-subtitle').get_text() if box_2 else "No se encontró la condición"
#             nombre = box_2.find('h1', class_='ui-pdp-title').get_text() if box_2 else "No se encontró el nombre"
            
#             # Agregamos los datos extraidos a la data
#             data.append({
#                 'Nombre del producto': nombre,
#                 'Condición': condicion,
#                 'Descripción': descripcion,
#                 'URL': url
#             })

#         except requests.exceptions.RequestException as e:
#             print(f"Error al acceder a la URL {url}: {e}")
            
#     # creamos un dataframe con el contenido de data
#     df = pandas.DataFrame(data)
#     # Convertimos el dataframe a un archivo excel
#     df.to_excel('prueba.xlsx', index=False)
#     return 'Archivo Excel generado con éxito.'

# # Llamada a la función para generar el archivo Excel
# print(generar_excel())

#----------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import pandas

def generar_excel():
    archivo = pandas.read_excel('URLs.xlsx', sheet_name='Sheet1')
    datos_columna = archivo['URL']
    urls = datos_columna.tolist()
    data = []

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()   
            content = response.text     
            soup = BeautifulSoup(content, 'html.parser')            
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
    df = pandas.DataFrame(data)
    df.to_excel('prueba.xlsx', index=False)
    return 'Archivo Excel generado con éxito.'
# Llamada a la función para generar el archivo Excel
print(generar_excel())

#-------------------------------------------------------------------------------

