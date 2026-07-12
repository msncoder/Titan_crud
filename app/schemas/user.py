from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# JWT Token ke liye standard models
class Token(BaseModel):
    access_token: str
    refresh_token: str  # Naya field add kiya
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
