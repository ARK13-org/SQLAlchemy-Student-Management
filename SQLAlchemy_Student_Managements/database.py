from sqlalchemy import ForeignKey, String, Table, Column, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker


DATABASE_URL = "sqlite:///mydatabase.db"


class Base(DeclarativeBase):
    pass


class BaseModel:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


# Association table for the many-to-many relationship
student_classroom = Table(
    "student_classroom",
    Base.metadata,
    Column(
        "student_id",
        ForeignKey("student.id"),
        primary_key=True,
    ),
    Column(
        "classroom_id",
        ForeignKey("class_room.id"),
        primary_key=True,
    ),
)


class Field(Base, BaseModel):
    __tablename__ = "field"

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    students: Mapped[list["Student"]] = relationship(
        back_populates="field"
    )

    classrooms: Mapped[list["ClassRoom"]] = relationship(
        back_populates="field"
    )

    def __repr__(self) -> str:
        return f"<Field(id={self.id}, name='{self.name}')>"


class Master(Base, BaseModel):
    __tablename__ = "master"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)

    classrooms: Mapped[list["ClassRoom"]] = relationship(
        back_populates="master"
    )

    def __repr__(self) -> str:
        return (
            f"<Master(id={self.id}, "
            f"name='{self.name}', "
            f"last_name='{self.last_name}')>"
        )


class Student(Base, BaseModel):
    __tablename__ = "student"

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)

    field_id: Mapped[int | None] = mapped_column(
        ForeignKey("field.id"),
        nullable=True,
    )

    field: Mapped["Field | None"] = relationship(
        back_populates="students"
    )

    classrooms: Mapped[list["ClassRoom"]] = relationship(
        secondary=student_classroom,
        back_populates="students",
    )

    def __repr__(self) -> str:
        return (
            f"<Student(id={self.id}, "
            f"name='{self.name}', "
            f"last_name='{self.last_name}')>"
        )


class ClassRoom(Base, BaseModel):
    __tablename__ = "class_room"

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    master_id: Mapped[int | None] = mapped_column(
        ForeignKey("master.id"),
        nullable=True,
    )

    field_id: Mapped[int | None] = mapped_column(
        ForeignKey("field.id"),
        nullable=True,
    )

    master: Mapped["Master | None"] = relationship(
        back_populates="classrooms"
    )

    field: Mapped["Field | None"] = relationship(
        back_populates="classrooms"
    )

    students: Mapped[list["Student"]] = relationship(
        secondary=student_classroom,
        back_populates="classrooms",
    )

    def __repr__(self) -> str:
        return f"<ClassRoom(id={self.id}, name='{self.name}')>"


class Database:
    def __init__(self, database_url: str = DATABASE_URL):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_tables(self) -> None:
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.SessionLocal()