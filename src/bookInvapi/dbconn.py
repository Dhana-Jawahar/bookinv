from sqlalchemy import create_engine
from sqlalchemy.orm import  declarative_base

# import os


# DATABASE_URL = os.environ.get('DB_URL')
# "postgresql+psycopg2://"+dbuser+":"+dbpassword +"@localhost:5432/"+dbname
DATABASE_URL ="postgresql+psycopg2://postgres:postgres@localhost:5432/bookinvdb"
engine = create_engine(DATABASE_URL,
  pool_size=10,          # Number of connections to maintain
    max_overflow=20,       # Extra connections allowed beyond pool_size
    pool_timeout=30,       # Seconds to wait for a connection
    pool_recycle=1800,     # Recycle connections after 30 minutes
)

# models.Base.metadata.create_all(bind=engine)

# Create the table in the database
# metadata.create_all(engine)
# print("Database and table created successfully!")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
