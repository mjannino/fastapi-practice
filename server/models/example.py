from typing import Optional
from pydantic import EmailStr, UrlStr, BaseModel

class ExampleEntityBase(BaseModel):
    name: str
    email: EmailStr
    bio: Optional[str] = ""
    website: Optional[UrlStr] = None

class ExampleEntityV1(ExampleEntityBase):
    additional_field: str


class ExampleEntityV2(ExampleEntityBase):
    breaking_change_field: str
