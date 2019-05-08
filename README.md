# Stuffs API

Stuffs API is a Django-based application designed to manage Specifications, Groups, and Components. This application allows for creating, updating, and cloning specifications

## Table of Contents

- [Installation & Usage](#installation)
- [Seeding Data](#seeding-data)
- [Feature Documentation](#feature-documentation)
   - [Specifications CRUD](#specifications-crud)
   - [Groups CRUD](#groups-crud)
   - [Components CRUD](#components-crud)
   - [Clone Specifications](#clone-specifications)
   - [Import Specifications](#import-specifications)
   - [Export Built Specifications Report](#export-built-specifications-report)

## Installation

### 1. **Clone the repository**:
```sh
   git clone https://github.com/yourusername/stuffs-api.git
   cd lennar-api
   chmod +x ./bin/**/*
```

### 2. **Use Docker to run the project**
```sh
   docker-compose up -d
```

OR
```sh
./bin/start-all
```
That's all you will be able to access the application at localhost:8000


## Seeding Data
To seed the database with initial data, run the custom Django management command:

This code is supposed to run inside the container
### 3. Connect to Running container
```sh
./bin/app/connect
```
And run
```sh
python manage.py seed_data
```

## CRUD Operations

#### Specifications CRUD

| Method | Endpoint                         | Description                        |
|--------|----------------------------------|------------------------------------|
| GET    | /api/stuffs/                     | API Root                           |
| GET    | /api/stuffs/specifications/      | List all specifications            |
| POST   | /api/stuffs/specifications/      | Create a new specification         |
| GET    | /api/stuffs/specifications/{id}/ | Retrieve a specific specification  |
| PUT    | /api/stuffs/specifications/{id}/ | Update a specific specification    |
| DELETE | /api/stuffs/specifications/{id}/ | Delete a specific specification    |


#### Groups CRUD
| Method | Endpoint                               | Description                            |
|--------|----------------------------------------|----------------------------------------|
| GET   | /api/stuffs/specifications/{id}/groups  | List all groups in specification       |
| POST   | /api/stuffs/specifications/{id}/groups | Create a new group in a specification  |
| GET    | /api/stuffs/groups/{id}/               | Retrieve a specific group              |
| PUT    | /api/stuffs/groups/{id}/               | Update a specific group                |
| DELETE | /api/stuffs/groups/{id}/               | Delete a specific group                |

#### Components CRUD
| Method | Endpoint                                    | Description                                    |
|--------|---------------------------------------------|------------------------------------------------|
| GET   | /api/stuffs/specifications/{id}/components/  | List all Components in specification           |
| POST   | /api/stuffs/specifications/{id}/components/ | Create a new Component in a specification      |
| GET    | /api/stuffs/components/{id}/                | Retrieve a specific Component                  |
| PUT    | /api/stuffs/components/{id}/                | Update a specific Component                    |
| DELETE | /api/stuffs/components/{id}/                | Delete a specific Component                    |

### Implementation

- **Serializers**:
  - `SpecificationSerializer`: Handles the validation and serialization of Specifications.
  - `GroupSerializer`: Handles the validation and serialization of Groups.
  - `ComponentSerializer`: Handles the validation and serialization of Components.

