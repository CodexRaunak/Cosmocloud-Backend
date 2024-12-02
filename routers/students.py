from fastapi import APIRouter, HTTPException, status, Path, Response, Body
from models.student import Student
from database import students_collection
from typing import Optional, Dict, Any
from bson import ObjectId

router = APIRouter()

def serialize_student(student: dict) -> dict:
    """Converts MongoDB document into a JSON-serializable format."""
    student["id"] = str(student["_id"])  # Convert ObjectId to string
    student.pop("_id", None)  # Remove the original `_id` field (optional)
    return student


@router.get("/") 
async def read_root():
    return {"message": "Welcome to the Student Management System!"}

@router.post("/students", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    student_data = student.model_dump()
    result = await students_collection.insert_one(student_data)
    if result.inserted_id:
        return {"id": str(result.inserted_id)}  # Return the inserted ID as a string
    else:
        raise HTTPException(status_code=400, detail="Student creation failed")

    

@router.get("/students", response_model=dict)
async def list_students(country: Optional[str] = None, age: Optional[int] = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = await students_collection.find(query,{"name":1,"age":1,"_id": 0}).to_list(100)  # Fetch data with filter
    # serialized_students = [serialize_student(student) for student in students]  # Serialize data

    return {"data": students}


@router.get("/students/{id}", response_model=dict)
async def get_student(id: str = Path(..., description="The ID of the student previously created")):
    if not ObjectId.is_valid(id):  
        raise HTTPException(status_code=400, detail="Invalid ID") 
    
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return {
        "name": student.get("name"),
        "age": student.get("age"),
        "address": student.get("address"),
    }

@router.patch("/students/{id}", response_model=dict)
async def update_student(student_data: Dict[str, Any] = Body(...), id: str = Path(..., description="The ID of the student previously created")):
    # Validate the ID format
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    # Convert the Pydantic model to a dictionary to get the updated data
    updated_data = {k: v for k, v in student_data.items() if v is not None}
 # Only include fields that are set (not None)

    # Ensure that the dictionary is not empty
    if not updated_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    # Convert the student id to an ObjectId
    student_id = ObjectId(id)

    # Perform the update operation in the database
    result = await students_collection.update_one(
        {"_id": student_id},  # Filter by the student ID
        {"$set": student_data}  # Update the fields with the provided data
    )

    # If no student is found with the provided ID
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/students/{id}", response_model=dict)
async def delete_student(id: str = Path(..., description="The ID of the student to be deleted")):
    # Validate the ID format
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    # Convert the student id to an ObjectId
    student_id = ObjectId(id)

    # Perform the deletion operation in the database
    result = await students_collection.delete_one({"_id": student_id})

    # If no student is found with the provided ID
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Return an empty response with 200 OK status code
    return {}