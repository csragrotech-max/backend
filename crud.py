from sqlalchemy.orm import Session
import models
import schemas


def get_users(db: Session):

    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=pwd_context.hash(user.password),
        name=user.name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.name = user.name
        if user.password is not None:
            db_user.password = pwd_context.hash(user.password)

        db.commit()
        db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):

    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_user:
        db.delete(db_user)
        db.commit()

    return {"message": "User deleted"}

