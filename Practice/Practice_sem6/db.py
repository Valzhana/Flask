import databases
from settings import settings
import sqlalchemy as sa

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()

engine = sa.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

users = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(32)),
    sa.Column('email', sa.String(128)),
    sa.Column('password', sa.String(128))
)

metadata.create_all(engine)