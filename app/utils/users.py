import sqlalchemy as sa

from app.models.users import Users as db_user
from app.schema.users import UserCreate, UserUpdate

class Users:
    def __init__(self, session) -> None:
        self.session = session

    def create_user(self, user: UserCreate):
        user = db_user(
            name=user.name
        )

        self.session.add(user)
        self.session.commit()

        return user

    def delete_user(self, user_id: int):
        #check if user exist
        user_exist = self.session.execute(
            sa.select(
                db_user.id,
                db_user.name
            ).where(
                db_user.id==user_id
            )
        ).fetchone()

        if not user_exist:
            return None

        user_id = user_exist.id
        username = user_exist.name

        user_deleted = self.session.query(db_user).filter(
            db_user.id==user_id
        ).delete(
            synchronize_session='fetch'
        )

        self.session.commit()

        return username
    
    def update_user(self, user_id: int, user: UserUpdate):
        #check if user exist
        user_exist = self.session.execute(
            sa.select(
                db_user.id,
                db_user.name
            ).where(
                db_user.id==user_id
            )
        ).fetchone()

        if not user_exist:
            return None

        username = user_exist.name

        user_updated = self.session.query(db_user).filter(
            db_user.id==user_id
        ).update(
            {
                db_user.name: user.name
            },
            synchronize_session='fetch'
        )

        self.session.commit()

        return username
    
    def detail_user(self, user_id: int):
        user = self.session.execute(
            sa.select(
                db_user
            ).where(
                db_user.id==user_id
            )
        ).scalar()

        return user

    def list_user(self):
        users = self.session.execute(
            sa.select(
                db_user.id,
                db_user.name
            )
        ).fetchall()

        return users
