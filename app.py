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

# from bs4 import BeautifulSoup
# import requests
# import pandas

# def generar_excel():
#     archivo = pandas.read_excel('URLs.xlsx', sheet_name='Sheet1')
#     datos_columna = archivo['URL']
#     urls = datos_columna.tolist()
#     data = []

#     for url in urls:
#         try:
#             response = requests.get(url)
#             response.raise_for_status()   
#             content = response.text     
#             soup = BeautifulSoup(content, 'html.parser')            
#             box_1 = soup.find('div', class_='ui-pdp-container__row ui-pdp-container__row--description', id='description')
#             box_2 = soup.find('div', class_='ui-pdp-container__row ui-pdp-component-list pr-16 pl-16')            
#             descripcion = box_1.find('p', class_='ui-pdp-description__content').get_text() if box_1 else "No se encontró la descripción"
#             condicion = box_2.find('span', class_='ui-pdp-subtitle').get_text() if box_2 else "No se encontró la condición"
#             nombre = box_2.find('h1', class_='ui-pdp-title').get_text() if box_2 else "No se encontró el nombre"                
#             data.append({
#                 'Nombre del producto': nombre,
#                 'Condición': condicion,
#                 'Descripción': descripcion,
#                 'URL': url
#             })
#         except requests.exceptions.RequestException as e:
#             print(f"Error al acceder a la URL {url}: {e}")
#     df = pandas.DataFrame(data)
#     df.to_excel('prueba.xlsx', index=False)
#     return 'Archivo Excel generado con éxito.'
# # Llamada a la función para generar el archivo Excel
# print(generar_excel())

#-------------------------------------------------------------------------------


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pandas as pd

# def generar_excel():
#     # Leer el archivo Excel y obtener la columna de URLs
#     archivo = pd.read_excel('URLs2a100.xlsx', sheet_name='Hoja1')
#     datos_columna = archivo['URL']
#     urls = datos_columna.tolist()
    
#     # Lista para almacenar los datos extraídos
#     data = []
    
#     # Inicializar el controlador de Chrome
#     driver = webdriver.Chrome()
    
#     # Iterar sobre cada URL en la lista
#     for url in urls:
#         try:
#             # Navegar a la URL
#             driver.get(url)
            
#             # Encontrar los elementos de la página usando selectores CSS
#             box_1 = driver.find_element(By.CSS_SELECTOR, 'div.ui-pdp-container__row.ui-pdp-container__row--description#description')
#             box_2 = driver.find_element(By.CSS_SELECTOR, 'div.ui-pdp-container__row.ui-pdp-component-list.pr-16.pl-16')
            
#             # Extraer la descripción del producto
#             descripcion = box_1.find_element(By.CSS_SELECTOR, 'p.ui-pdp-description__content').text if box_1 else "No se encontró la descripción"
            
#             # Extraer el nombre del producto
#             nombre = box_2.find_element(By.CSS_SELECTOR, 'h1.ui-pdp-title').text if box_2 else "No se encontró el nombre"
            
#             # Extraer la condición del producto
#             condicion = box_2.find_element(By.CSS_SELECTOR, 'span.ui-pdp-subtitle').text if box_2 else "No se encontró la condición"
            
#             precio_entero = box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__fraction').text if box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__fraction') else 'N/A'
#             precio_decimal = box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__cents').text if box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__cents') else '00'            
#             # Combinar la parte entera y decimal del precio
#             precio = f"{precio_entero},{precio_decimal}" if precio_entero != 'N/A' else 'N/A'
            
#             # Encuentra las imágenes usando Selenium
#             imagenes = driver.find_elements(By.CSS_SELECTOR, 'img.ui-pdp-image.ui-pdp-gallery__figure__image')

#             # Extrae las URLs de las imágenes
#             imagen_1 = imagenes[0].get_attribute('data-zoom') if len(imagenes) > 0 else imagenes[0].get_attribute('src') if len(imagenes) > 0 else 'N/A'
#             imagen_2 = imagenes[1].get_attribute('data-zoom') if len(imagenes) > 1 else imagenes[1].get_attribute('src') if len(imagenes) > 1 else 'N/A'
            
#             # Añadir los datos extraídos a la lista
#             data.append({
#                 'Nombre del producto': nombre,
#                 'Precio': precio,
#                 'Condición': condicion,
#                 'Descripción': descripcion,
#                 'URL': url,
#                 'Imagen 1': imagen_1,
#                 'Imagen 2': imagen_2,
#             })
#         except Exception as e:
#             # Imprimir un mensaje de error si ocurre una excepción
#             print(f"Error al acceder a la URL {url}: {e}")
    
#     # Cerrar el controlador de Chrome
#     driver.quit()
    
#     # Crear un DataFrame de pandas con los datos extraídos
#     df = pd.DataFrame(data)
    
#     # Guardar el DataFrame en un archivo Excel
#     df.to_excel('Prueba2a100.xlsx', index=False)
    
#     return 'Archivo Excel generado con éxito.'

# # Llamar a la función para generar el archivo Excel
# generar_excel()



#------------------------------------------------------------------------------


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def generar_excel():
    # Leer el archivo Excel y obtener la columna 'URL'
    archivo = pd.read_excel('URLs601a700.xlsx', sheet_name='Hoja1')
    datos_columna = archivo['URL']
    urls = datos_columna.tolist()  # Convertir la columna de URLs en una lista
    data = []  # Lista para almacenar los datos extraídos

    # Inicializar el WebDriver de Chrome
    driver = webdriver.Chrome()
    for url in urls:
        try:
            driver.get(url)  # Navegar a la URL
            # Encontrar los elementos que contienen la descripción y otros detalles del producto
            box_1 = driver.find_element(By.CSS_SELECTOR, 'div.ui-pdp-container__row.ui-pdp-container__row--description#description')
            box_2 = driver.find_element(By.CSS_SELECTOR, 'div.ui-pdp-container__row.ui-pdp-component-list.pr-16.pl-16')
            
            # Extraer la descripción del producto
            descripcion = box_1.find_element(By.CSS_SELECTOR, 'p.ui-pdp-description__content').text if box_1 else "No se encontró la descripción"
            # Extraer el nombre del producto
            nombre = box_2.find_element(By.CSS_SELECTOR, 'h1.ui-pdp-title').text if box_2 else "No se encontró el nombre"
            # Extraer la condición del producto (nuevo/usado)
            condicion = box_2.find_element(By.CSS_SELECTOR, 'span.ui-pdp-subtitle').text if box_2 else "No se encontró la condición"
            
            # Extraer el precio del producto
            precio_entero = box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__fraction').text if box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__fraction') else 'N/A'
            precio_decimal = box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__cents').text if box_2.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__cents') else '00'
            # Combinar la parte entera y decimal del precio
            precio = f"{precio_entero},{precio_decimal}"
            
            # Extraer las URLs de las imágenes del producto
            imagenes = driver.find_elements(By.CSS_SELECTOR, 'img.ui-pdp-image.ui-pdp-gallery__figure__image')
            imagen_1 = imagenes[0].get_attribute('data-zoom') if len(imagenes) > 0 else 'N/A'
            imagen_2 = imagenes[1].get_attribute('data-zoom') if len(imagenes) > 1 else 'N/A'
            
            # Agregar los datos extraídos a la lista 'data'
            data.append({
                'Nombre del producto': nombre,
                'Precio': precio,
                'Condición': condicion,
                'Descripción': descripcion,
                'URL': url,
                'Imagen 1': imagen_1,
                'Imagen 2': imagen_2,
            })
        except Exception as e:
            # Imprimir un mensaje de error si ocurre una excepción
            print(f"Error al acceder a la URL {url}: {e}")
    
    driver.quit()  # Cerrar el WebDriver
    
    # Crear un DataFrame de pandas con los datos extraídos y guardarlo en un archivo Excel
    df = pd.DataFrame(data)
    df.to_excel('Prueba601a700.xlsx', index=False)    
    return 'Archivo Excel generado con éxito.'

generar_excel()