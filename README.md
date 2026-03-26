🔐 Secure-Notes-API (FastAPI + MongoDB)
API de gestión de notas y tareas con arquitectura de seguridad robusta. Este proyecto fue diseñado para dominar el flujo de autenticación asincrónica y la persistencia en bases de datos NoSQL, garantizando el aislamiento total de datos entre usuarios.

🚀 Características Principales
Seguridad de Grado Industrial: Implementación de hashing avanzado con Bcrypt (Aunque el standard es Argon2 el proceso es el mismo) y flujo completo de OAuth2 con JWT.
Aislamiento de Datos (Multitenencia): Lógica de filtrado a nivel de base de datos para asegurar que cada usuario acceda exclusivamente a sus propios registros.
Persistencia NoSQL: Modelado de documentos dinámicos en MongoDB, optimizando la velocidad de lectura y escritura de tareas.
Gestión de Sesiones: Generación de tokens con tiempo de expiración configurado para proteger rutas críticas.

🛠️ Stack
Framework: FastAPI 
Database: MongoDB 
Seguridad: Python-Jose JWT, Bcrypt 
Validación: Pydantic (Modelos de entrada/salida)

📡 Endpoints Clave
POST /auth/register → Registro de usuarios con validación de credenciales únicas.
POST /auth/login → Intercambio de credenciales por Token de Acceso (JWT).
GET /tasks → Recupera únicamente las tareas pertenecientes al usuario autenticado.
POST /tasks → Creación de registros vinculados automáticamente al ID del autor.
