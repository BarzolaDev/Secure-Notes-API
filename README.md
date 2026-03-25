# To-Do List API (Authentication & Multi-user)

Hice este proyecto para aprender el manejo de bases de datos NoSQL con **MongoDB** y profundizar en el flujo de **OAuth2**.

## 🚀 Features
- **Sistema de Usuarios:** Registro y Login con hashing de contraseñas (BCrypt).
- **Seguridad:** Autenticación basada en JWT (OAuth2).
- **Aislamiento de Datos:** Cada usuario es dueño de sus registros; las listas son privadas y persistentes.
- **CRUD Completo:** Gestión total de tareas y listas por cada perfil.

## 🛠️ Tech Stack
- **Backend:** Python (FastAPI)
- **Database:** MongoDB
- **Security:** JWT, OAuth2, BCrypt

## 🔐 Flow & Logic
- Las contraseñas se hashean antes de guardarse en la DB.
- Los tokens JWT se generan al login y se validan en cada ruta protegida.
- Implementación de lógica para que un usuario solo pueda interactuar con sus propios documentos.
