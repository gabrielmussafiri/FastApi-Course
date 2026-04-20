from .. import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends , APIRouter
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)



# Create User
@router.post("/", status_code=status.HTTP_201_CREATED , response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    # Hash the password
    hashed_password= utils.hash_password(user.password)
    user.password = hashed_password
    
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    
# Get user by id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id:int,db:Session=Depends(get_db)):
    user =db.query(models.Users).filter(models.Users.id ==id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id:{id} does not exist')
    
    return user

# Get All users
@router.get('/')
def get_users(db:Session=Depends(get_db)):
    users = db.query(models.Users).all()
    return users
# Update Users by id
@router.put('/{id}')
def update_user(id:int, updated_user:schemas.UserUpdate, db:Session=Depends(get_db)):
    user_query = db.query(models.Users).filter(models.Users.id==id)
    user = user_query.first()
    
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} does not exist')
    user_query.update(updated_user.dict(),synchronize_session=False)
    db.commit()
    
    return user_query.first()

