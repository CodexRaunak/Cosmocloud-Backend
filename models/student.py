from pydantic import BaseModel
from typing import Optional
# from bson import ObjectId


# class ObjectIdModel(BaseModel):
#     id: str

#     class Config:
#         # This will help Pydantic to handle ObjectId by converting it to a string
#         json_encoders = {
#             ObjectId: str
#         }


class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]