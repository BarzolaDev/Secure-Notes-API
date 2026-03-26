# 🔐 Secure-Notes-API (FastAPI + MongoDB)

Este proyecto lo utilice para repasar el flujo de OAuth2, esta todo lo demás detallado. 

### 🚀 Características Principales

* **Seguridad Robusta:** Implementación de hashing con **Bcrypt** (comprendiendo la transición hacia estándares como Argon2) y flujo completo de **OAuth2 con JWT**.
* **Aislamiento de Datos (Multitenencia):** Lógica de filtrado a nivel de base de datos para asegurar que cada usuario acceda exclusivamente a sus propios registros.
* **Persistencia NoSQL:** Modelado de documentos dinámicos en **MongoDB**, optimizando la velocidad de lectura y escritura de tareas.
* **Gestión de Sesiones:** Generación de tokens con tiempo de expiración configurado para proteger rutas críticas.

### 🛠️ Stack

* **Framework:** FastAPI (asincrónico con async/await)
* **Database:** MongoDB
* **Seguridad:** Python-Jose JWT, Bcrypt
* **Validación:** Pydantic (Modelos de entrada/salida)

### 📡 Endpoints Clave

| `POST` | `/auth/register` | Register 
| `POST` | `/auth/login` |  Validamos LOGIN 
| `GET` | `/tasks` | Tareas únicas del usuario gracias a jwt
| `POST` | `/tasks` | Creamos las tareas
