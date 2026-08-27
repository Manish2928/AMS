# AMS — Attendance Management System

A full-stack **Attendance Management System** built with **Python, Flask, MySQL, and SQLAlchemy**, designed to digitize and streamline attendance management for students, faculty, and administrators.

The system provides role-based access, authentication, database-driven attendance operations, and a structured web application architecture.

---

## 📌 Project Overview

The **Attendance Management System (AMS)** is a web-based application developed to replace manual attendance processes with a centralized digital platform.

The system is designed around three primary user roles:

* **Administrator** — manages system-level operations and users.
* **Faculty** — manages attendance and student-related academic activities.
* **Student** — accesses attendance-related information and services.

The application follows a modular Flask architecture, separating authentication, database logic, models, routes, utilities, templates, and role-specific functionality.

---

## 🎯 Objectives

The main objectives of the project are to:

* Digitize the attendance management process.
* Reduce manual attendance-related work.
* Provide role-based access to system functionality.
* Centralize student and attendance data.
* Provide a structured and maintainable backend architecture.
* Improve accessibility and efficiency for students, faculty, and administrators.

---

## ✨ Key Features

### 🔐 Authentication & Security

* Secure user authentication
* Login and session management
* Role-based access control
* Password hashing using bcrypt
* CSRF protection
* Environment-based configuration for sensitive values

### 👨‍💼 Administrator

* Administrative access to the system
* User and system management
* Access to administrative functionality
* Centralized management of application data

### 👨‍🏫 Faculty

* Faculty authentication
* Student-related management
* Attendance management
* Access to attendance information
* Faculty-specific application functionality

### 👨‍🎓 Student

* Student authentication
* Access to personal attendance information
* Student-specific functionality and dashboards

### 📱 QR Code Integration

The application includes QR-code functionality using Python libraries such as `qrcode` and `Pillow`, supporting QR-based attendance-related workflows.

### 🗄️ Database Management

The system uses a relational MySQL database with SQLAlchemy for application-level database interaction.

Database-related functionality includes:

* SQLAlchemy ORM
* MySQL connectivity
* Database migrations with Flask-Migrate
* Centralized database models and queries

---

# 🏗️ System Architecture

The application follows a modular architecture to keep different responsibilities separated.

```text
                    ┌─────────────────────┐
                    │       Client        │
                    │   Web Browser/UI    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask Routes     │
                    │ Authentication/API  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌───────────┐    ┌───────────┐    ┌───────────┐
        │  Student  │    │  Faculty  │    │   Admin   │
        │   Module  │    │   Module  │    │   Module  │
        └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │    DB Queries &     │
                    │       Models       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       MySQL         │
                    │      Database       │
                    └─────────────────────┘
```

---

# 📂 Project Structure

```text
AMS/
│
├── app/
│   ├── admin/
│   ├── auth/
│   ├── db_queries/
│   ├── faculty/
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── student/
│   ├── templates/
│   ├── utils/
│   │
│   ├── __init__.py
│   └── extensions.py
│
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

### Module Description

| Module          | Responsibility                                |
| --------------- | --------------------------------------------- |
| `admin/`        | Administrator-related functionality           |
| `auth/`         | Authentication and authorization              |
| `db_queries/`   | Database operations and query logic           |
| `faculty/`      | Faculty-related functionality                 |
| `models/`       | SQLAlchemy database models                    |
| `routes/`       | Application routes and request handling       |
| `student/`      | Student-related functionality                 |
| `templates/`    | HTML templates                                |
| `static/`       | CSS, JavaScript, images, and static resources |
| `utils/`        | Utility and helper functions                  |
| `extensions.py` | Flask extension initialization                |
| `config.py`     | Application configuration                     |
| `run.py`        | Application entry point                       |

---

# 🛠️ Technology Stack

## Backend

* **Python**
* **Flask**
* **SQLAlchemy**
* **Flask-Migrate**

## Database

* **MySQL**
* **PyMySQL**
* **MySQL Connector**

## Authentication & Security

* **Flask-Login**
* **Flask-WTF**
* **WTForms**
* **bcrypt**

## Supporting Libraries

* **python-dotenv**
* **Requests**
* **python-dateutil**
* **qrcode**
* **Pillow**

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Manish2928/AMS.git
cd AMS
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

Create a `.env` file in the project root and configure the required environment variables.

Example:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_connection_string
```

> **Important:** Never commit sensitive credentials, passwords, secret keys, or database connection details to the repository.

---

# 🗄️ Database Configuration

The application uses **MySQL** as its primary relational database.

Create the required database before starting the application.

Example:

```sql
CREATE DATABASE attendance_management;
```

Configure the database connection through the application's environment/configuration settings.

---

# ▶️ Running the Application

Start the application using:

```bash
python run.py
```

For local development, the application can typically be accessed at:

```text
http://127.0.0.1:5000
```

---

# 🔑 User Roles

The application is designed around role-based access.

| Role              | Primary Responsibility                                    |
| ----------------- | --------------------------------------------------------- |
| **Administrator** | Manage system-level operations                            |
| **Faculty**       | Manage attendance and student-related academic operations |
| **Student**       | View personal attendance and student services             |

Each role has access to functionality appropriate to its responsibilities.

---

# 🔒 Security Considerations

The application incorporates several security-related mechanisms:

* Password hashing with **bcrypt**
* User authentication using **Flask-Login**
* CSRF protection using **Flask-WTF**
* Environment variables for sensitive configuration
* Role-based access control
* Server-side validation and database-backed authentication

For production deployment, secure environment configuration, HTTPS, restricted database access, and production-grade Flask deployment should be used.

---

# 📊 Database Layer

The application uses **SQLAlchemy ORM** to interact with the MySQL database.

The database layer is separated into:

```text
models/
db_queries/
```

This separation keeps database structures and application-level query logic organized and easier to maintain.

Database migrations are supported through **Flask-Migrate**.

---

# 📱 QR Code Functionality

QR-code functionality is integrated using:

```text
qrcode
Pillow
```

This provides the application with the capability to generate and process QR-based information within attendance-related workflows.

---

# 🧪 Testing & Validation

The system was developed and validated around its primary attendance-management workflows, including:

* Authentication
* Role-based access
* Student functionality
* Faculty functionality
* Administrative functionality
* Database operations
* Attendance-related operations
* QR-code functionality

---

# 🚀 Deployment

The application can be deployed to a Python-compatible server environment with:

* Python
* Flask
* MySQL
* Required Python dependencies
* Environment-based configuration

For production environments, a production WSGI server such as **Gunicorn** can be used instead of Flask's development server.

---

# 📌 Project Status

**Completed**

This repository contains the completed implementation of the Attendance Management System.

---

# 👨‍💻 Author

**Manish Kashyap**

GitHub: [Manish2928](https://github.com/Manish2928)

---

# 📄 License

This project currently does not specify an open-source license.

Unless a license is added to the repository, the default copyright remains with the project author.

---

## ⭐ Acknowledgements

This project was developed as a software application for learning, implementation, and practical application of:

* Web development with Flask
* Database management with MySQL
* ORM-based application development with SQLAlchemy
* Authentication and authorization
* Secure application development
* Modular software architecture
