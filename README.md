# Student Management System Backend

## Overview

This project is a backend implementation for a Student Management System, built using **FastAPI** (Python framework) and **MongoDB** as the database. It allows the management of student data, providing a set of APIs to add, update, fetch, and delete student records from a MongoDB database hosted on MongoDB Atlas.

## Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB (MongoDB Atlas M0 free cluster)
- **Deployment**: Render 

## Features

- **CRUD Operations** for student data.
- **MongoDB Atlas Integration**: The database is hosted on MongoDB Atlas for scalable and secure data storage.
- **FastAPI**: A modern Python framework for building APIs quickly and efficiently.

## APIs

The backend exposes a set of RESTful APIs to interact with the student data:

1. **GET /students**
   - Fetch all students.
   
2. **GET /students/{id}**
   - Fetch a student by ID.

3. **POST /students**
   - Add a new student.
   
4. **PATCH /students/{id}**
   - Update an existing student by ID.
   
5. **DELETE /students/{id}**
   - Delete a student by ID.

## Deployment

The application has been deployed on **Render** (or any other platform you choose, e.g., AWS, Azure). The base URL for accessing the API is:
https://cosmocloud-backend-d97r.onrender.com


### Running Locally

To run the application locally, you can follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/CodexRaunak/Cosmocloud-Backend
   cd Cosmocloud-Backend
   ```

2. Create virtual env

  ```bash
  python -m venv .venv
  source .venv/Scripts/activate  
  ```

3. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

4. Set up MongoDB Atlas:

- Create an account on MongoDB Atlas.
- Create a free-tier M0 cluster.
- Set up a database and collection.
- Obtain the connection string and replace it in the .env file0
 
  ```bash
  MONGO_DB_URL = "<your-mongo-db-url>"
  ``` 

5. Run the server

  ```bash
  uvicorn main:app --reload
  ``` 




  



