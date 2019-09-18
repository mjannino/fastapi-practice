from typing import Optional
from pydantic import EmailStr, UrlStr, BaseModel

class ExampleEntityBase(BaseModel):
    name: str
    email: EmailStr
    bio: Optional[str] = ""
    website: Optional[UrlStr] = None

class ExampleEntity(ExampleEntityBase):
    additional_field: str
