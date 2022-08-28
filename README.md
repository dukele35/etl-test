# Inspectorio Project

### 1. Overview
- The purpose of this project is to build simple REST API service connected with a PostgreSQL database named `L` in which an user could perform `GET` & `POST` requests to retrieve or insert new data into `L`.
- The REST API service, which is developed upon Django REST, PostgreSQL & PgAdmin, is containerised by using `docker` and `docker-compose`.

### 2. How to run
- Download this folder to your local machine.
- Then run the following
```
docker-compose build && docker-compose up -d
```

### 3. What to expect
#### 3.1. REST API
- http://localhost/ shows the default Django REST's API Root page which includes http://localhost/item/, http://localhost/org/ & http://localhost/factory/
- http://localhost/api/ reveals the Swagger API doc instructing us how to perform `GET`, `POST`, `PUT`, `PATCH` & `DELETE` requests on different data models, i.e. `item`, `org` & `factory`.
#### 3.2. Data Models