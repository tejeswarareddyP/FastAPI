import json
from pathlib import Path
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal, get_db, engine, Base
from email_utils import send_invitation_email

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_users/")
async def add_user(username: str, email: str, project_id: int = None, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Add new user
    new_user = User(username=username, email=email, project_id=project_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User added successfully", "user": new_user}


@app.get("/get_users/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": users}


@app.patch("/update_users/")
async def update_user(user_id: int, username: str = None, email: str = None, project_id: int = None, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if username:
        user.username = username
    if email:
        user.email = email
    if project_id is not None:
        user.project_id = project_id

    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": user}


@app.delete("/delete_users/")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
# Send Invitation Email
@app.post("/send_invites")
async def send_invites():
    await send_invitation_email()
    return {"message": "Invitation emails sent successfully"}





