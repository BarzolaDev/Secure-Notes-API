# 🔐 Secure Notes API

Una infraestructura de backend diseñada bajo el paradigma **Security-First**, utilizando **FastAPI** y **MongoDB**. Este proyecto implementa un sistema robusto de gestión de información sensible con aislamiento total de datos por usuario.

---

## 🎯 High-Level Features

* **Autenticación Stateless (JWT):** Implementación completa del flujo **OAuth2** con Bearer Tokens. Gestión de sesiones sin estado, permitiendo una escalabilidad horizontal del backend.
* **Criptografía y Hashing:** Protección de credenciales mediante **Bcrypt** con factor de costo dinámico, garantizando que los datos sensibles nunca se almacenen en texto plano.
* **Aislamiento Multitenant:** Arquitectura lógica que asegura la privacidad de los datos. Cada consulta a la base de datos está vinculada intrínsecamente al `user_id` extraído del token, eliminando riesgos de filtración cruzada.
* **Performance Asincrónica:** Aprovechamiento total del *event loop* de Python con `motor` (driver asíncrono de MongoDB) para manejar múltiples peticiones concurrentes sin bloqueos de I/O.
* **Esquemas de Datos Rigurosos:** Validación y sanitización de payloads mediante **Pydantic**, asegurando que solo los datos estructurados correctamente ingresen a la capa de persistencia.

---

## 🛠️ Tech Stack

* **Core:** FastAPI (Asynchronous Python)
* **NoSQL Storage:** MongoDB (Atlas / Community)
* **Security:** Python-Jose (JWT), Passlib (Bcrypt), OAuth2PasswordBearer
* **Dev Ops:** Pydantic (Environments & Schemas)

---

## 📡 Core Endpoints

| Método | Endpoint | Acción | Seguridad |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/signup` | Registro de usuario | Público |
| `POST` | `/auth/login` | Intercambio de credenciales por Token | Público |
| `GET` | `/notes` | Recuperación de notas privadas | **Requerido (JWT)** |
| `POST` | `/notes` | Persistencia de nueva nota | **Requerido (JWT)** |
