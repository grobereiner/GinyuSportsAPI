<div align="center">
  <img src="img/giniu.png" height="250"></img>
  <h1>GinyuSportsAPI</h1>
</div>

## Estructura del proyecto: Microservicios
Hemos escogido microservicios debido a que nuestros principales casos de uso:

- Búsqueda específica de partidos
- Scraping de partidos y actualización de base de datos

Son acciones complejas que no están relacionadas por lo que es factible separar cada uso en un servidor diferente de tal forma que no sea necesario detener la API cuando se necesita realizar mantenimiento en alguno de los servicios. Por ejemplo: 

- Un usuario puede estar realizando búsquedas mientras se está optimizando el algoritmo de scraping en el servicio de administrador.
- Los administradores pueden estar scrapeando nueva información mientras que se añaden nuevas funciones a las acciones de un usuarios.

### Directorios y diagrama:

```py
-cli_API
|--controlador.py
|--servicio.py

-server_ADMIN
|--controlador.py
|--dao.py
|--servicio.py
-server_API
|--controlador.py
|--servicio.py
-server_SEARCH
|--controlador.py
|--dao.py
|--servicio.py
```

![](img/diagram.png)