# Visualización de terremotos mundiales

![1-Logo](https://user-images.githubusercontent.com/122131317/218566603-d6720244-e06a-446a-84d5-fcca6798e381.png)

### Resumen:
Utilizando la API RESTful de USGS obtendremos la información y localización geográfica de los terremotos con magnitud mayor a 4.0 sucedidos a lo largo del 2022. Incluiremos toda la información en un dataframe que luego usaremos para visualizar todas las incidencias en un mapa global.

El Servicio Geológico de EE.UU. (USGS) es una agencia civil de cartografía y ciencias del agua, la tierra y la biología del país. Recopila, supervisa, analiza y proporciona información sobre terremotos, evalúan los impactos y riesgos sísmicos y llevan a cabo investigaciones sobre las causas y efectos de los terremotos.

### Paso 1:
Primero haremos una llamada a la API con los parámetros que nos interesan y nos devolverá una respuesta en formato JSON. 
La documentación la podemos encontrar aquí: https://earthquake.usgs.gov/fdsnws/event/1/

### Paso 2:
Una vez tenemos obtenemos la respuesta, transformaremos los datos y los guardaremos en un DataFrame.

### Paso 3:
Partiendo del DataFrame anterior visualizaremos los datos en un mapa 3D con plotly.graph_objects que muestre la localización e intensidad de los terremotos.

### Paso 4:
Convertiremos el mapa en formato GIF y lo mostraremos aquí. ⬇️⬇️⬇️

![earthquakes_global](https://user-images.githubusercontent.com/122131317/222718317-59298328-5497-4400-b94e-dafd9b5d8ec7.gif)

<h2 style="text-align:center;">Espero que te haya gustado!! 😄</h2>

## Autor: 
<p>Marta Búa Fernández ➡️ Ir al perfil de<a href="https://www.linkedin.com/in/martabuaf" target = "_blank"> LinkedIn </a></p> 
