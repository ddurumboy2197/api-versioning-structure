from fastapi import FastAPI
from pydantic import BaseModel

# API versiyalari uchun katalog
app = FastAPI(
    title="API",
    description="API versiyalari uchun katalog",
    version="1.0.0",
    contact={
        "name": "Developer",
        "email": "developer@example.com",
        "url": "https://example.com"
    }
)

# v1 versiyasi uchun API
v1_app = FastAPI(
    title="API v1",
    description="API v1 versiyasi uchun katalog",
    version="1.0.0",
    parent=app
)

# v2 versiyasi uchun API
v2_app = FastAPI(
    title="API v2",
    description="API v2 versiyasi uchun katalog",
    version="2.0.0",
    parent=app
)

# v1 versiyasi uchun model
class UserV1(BaseModel):
    id: int
    name: str

# v2 versiyasi uchun model
class UserV2(BaseModel):
    id: int
    name: str
    email: str

# v1 versiyasi uchun API endpoint
@app.get("/users/v1/{user_id}")
async def get_user_v1(user_id: int):
    return {"id": user_id, "name": "John Doe"}

# v2 versiyasi uchun API endpoint
@app.get("/users/v2/{user_id}")
async def get_user_v2(user_id: int):
    return {"id": user_id, "name": "John Doe", "email": "john@example.com"}

# v1 versiyasi uchun API endpoint
v1_app.get("/users/v1/{user_id}", response_model=UserV1)

# v2 versiyasi uchun API endpoint
v2_app.get("/users/v2/{user_id}", response_model=UserV2)
```

Bu kodda FastAPI kutubxonasidan foydalanib, API versiyalari uchun katalog yaratiladi. V1 va V2 versiyalari uchun API endpointlari yaratiladi, shuningdek, model va response_model uchun pydantic BaseModeldan foydalaniladi.
