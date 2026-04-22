# FastAPI-Project

# Project Overview
This project is a professional, modular FastAPI implementation featuring 18 CRUD operations, integrated database management, and multi-layered security protocols (JWT, OAuth2, and API Keys). It is designed to demonstrate best practices in REST API development and modular code organization.

# Key Features
Modular Architecture: Organized into specific directories for api, models, schemas, and security.
Database Integration: Fully integrated with SQLAlchemy ORM and SQLite.
Comprehensive CRUD: Total of 18 endpoints (6 for each resource: Users, Products, and Orders).
Multi-Auth Security: Each module implements a different security standard.
Auto-Generated Docs: Interactive API documentation available via Swagger UI and ReDoc.

# Tech Stack
Language: Python 3.10+
Framework: FastAPI
ORM: SQLAlchemy
Database: SQLite
Validation: Pydantic v2
Security: JWT, OAuth2, API-Key Header

# Project Structure
├── api/
│   ├── users.py      # Users CRUD (JWT Secured)
│   ├── products.py   # Products CRUD (OAuth2 Secured)
│   └── orders.py     # Orders CRUD (API Key Secured)
├── database.py       # DB Connection & Session Management
├── models.py         # SQLAlchemy Database Models
├── schemas.py        # Pydantic Request/Response Models
├── security.py       # Authentication Logic
├── main.py           # Application Entry Point
└── requirements.txt  # Project Dependencies

# Security Protocols
This project demonstrates the implementation of three distinct security methods:
## 1. Users Module Security
Secured using JWT (JSON Web Tokens). This allows for stateless authentication where the server verifies the token signature for each request.
## 2. Products Module Security
Secured using OAuth2 (Bearer Token). This simulates a standard client-server authorization flow.
## 3. Orders Module Security
Secured using API Keys. The system validates a specific X-API-KEY header before granting access to order resources.

# API Endpoints
Each module contains 6 operations to handle data efficiently:

### Users Resource
* POST /users/ - Create a new user record.
* GET /users/ - List all registered users.
* GET /users/{id} - Retrieve a specific user by ID.
* PUT /users/{id} - Perform a full update on a user record.
* PATCH /users/{id} - Perform a partial update (e.g., updating just the email).
* DELETE /users/{id} - Remove a user from the system.

### Products Resource
Implements 6 CRUD operations for managing product inventory and pricing.

### Orders Resource
Implements 6 CRUD operations for processing orders and tracking quantities.

# Setup and Installation
### 1. Environment Setup
python -m venv venv
source venv/Scripts/activate  # Windows

### 2. Dependencies
pip install -r requirements.txt

### 3. Execution
uvicorn main:app --reload

## UI Overview 
<img width="1275" height="472" alt="Image" src="https://github.com/user-attachments/assets/c87d35d7-2f0c-49eb-9606-2195ca6907f3" />

<img width="1183" height="319" alt="Image" src="https://github.com/user-attachments/assets/cfd14345-ca2b-4256-9d3f-2ba8ea4ec66d" />

<img width="1199" height="307" alt="Image" src="https://github.com/user-attachments/assets/55fe6053-e388-41ac-a77e-55044f60ea27" />


## Author
### Palak Rathor
