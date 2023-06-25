
Memoria

En este segundo ejercicio de Django se han seguido los siguientes puntos:

En la Gestión de usuarios:
- Se han creado dos grupos distintos: "Administradores" y "Empleados". Para ello, se han definido modelos personalizados Administrador y Empleado que heredan de la clase Group proporcionada por Django.
- Se ha limitado el uso de los grupos que no sean administradores mediante el uso de permisos desde el panel de administración.

Se han implementado tests unitarios para comprobar el correcto funcionamiento de la API. Se ha utilizado la clase APITestCase proporcionada por el módulo rest_framework de Django y se han realizado pruebas para diferentes funcionalidades, como la lista de grupos y personas.

Se ha implementado al menos un viewset. Utilizando Django REST Framework, se ha creado un viewset para el modelo Person. Esta implementación permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) en el modelo a través de las rutas del API.

Se ha utilizado MySQL como base de datos. Para ello, se ha configurado la conexión a la base de datos en el archivo settings.py, se han instalado las dependencias necesarias, módulo mysql-client, y se ha realizado la migración de la base de datos.

Se ha asegurado la portabilidad del servidor mediante la creación del archivo requirements.txt. Este archivo contiene todas las dependencias utilizadas, incluyendo mysqlclient en caso de utilizar MySQL.

Se ha aplicado el principio DRY (don't repeat yourself) utilizando mixins y herencia de clases en las vistas genéricas y viewsets. Se ha creado una clase base que contiene la lógica común de las vistas genéricas y se han definido las vistas específicas para cada modelo.

Se han utilizado al menos 4 vistas genéricas distintas para cada modelo, cumpliendo con el requisito establecido. Se han utilizado vistas como ListView, DetailView, CreateView, UpdateView y DeleteView.

Se ha implementado al menos una api_view propia que enlaza modelos. Se ha proporcionado un ejemplo básico de una función api_view que enlaza los modelos Person y Group.

Conclusiones

El desarrollo del servidor con Django ha permitido cumplir con los requisitos establecidos y abordar distintas funcionalidades esenciales. A través de la implementación de modelos, vistas genéricas, viewsets y pruebas unitarias, se ha logrado crear un servidor funcional y robusto.

Al aplicar el principio DRY, se ha evitado la duplicación de código y se ha fomentado la reutilización y mantenibilidad del código. Además, la utilización de grupos de usuarios ha permitido establecer restricciones de acceso y controlar las acciones disponibles para cada tipo de usuario.

La elección de MySQL como base de datos ha ampliado las opciones de almacenamiento y ha facilitado la migración desde una base de datos SQLite existente. La portabilidad del servidor se ha garantizado mediante la inclusión de todas las dependencias en el archivo requirements.txt.

