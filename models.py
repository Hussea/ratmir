#alembic revision --autogenerate -m "your message"
# تنفيذ امر التعديل من التيرمنال 
#alembic upgrade head
# تحديث قاعده البيانات 
from typing import Optional
import datetime

from sqlalchemy import Date, ForeignKeyConstraint, Index, Integer, String, Time, text
from sqlalchemy.dialects.mysql import TEXT, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    num_T: Mapped[str] = mapped_column(String(100), nullable=False)
    data_prth: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    Salary: Mapped[int] = mapped_column(Integer, nullable=False)
    Job: Mapped[str] = mapped_column(String(100), nullable=False)
    nots: Mapped[str] = mapped_column(String(500), nullable=False)
    image_path: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[int] = mapped_column(TINYINT(1), nullable=False, server_default=text("'1'"))

    project_guards: Mapped[list['ProjectGuards']] = relationship('ProjectGuards', back_populates='employee')


class ListPointsCheckd(Base):
    __tablename__ = 'list_points_checkd'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_check_point: Mapped[int] = mapped_column(Integer, nullable=False)
    dataD: Mapped[datetime.date] = mapped_column(Date, nullable=False, server_default=text('(curdate())'))
    timeD: Mapped[datetime.time] = mapped_column(Time, nullable=False, server_default=text('(curtime())'))


class PointsChick(Base):
    __tablename__ = 'points_chick'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_project: Mapped[int] = mapped_column(Integer, nullable=False)
    name_point: Mapped[str] = mapped_column(String(100), nullable=False)
    Coordinates: Mapped[str] = mapped_column(String(100), nullable=False)
    id_entry_emp: Mapped[str] = mapped_column(String(100), nullable=False)


class Projuct(Base):
    __tablename__ = 'projuct'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    Coordinates: Mapped[str] = mapped_column(String(100), nullable=False)
    q_person: Mapped[int] = mapped_column(Integer, nullable=False)
    ses_work: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time_work: Mapped[str] = mapped_column(String(100), nullable=False)
    sum_of_proj: Mapped[int] = mapped_column(Integer, nullable=False)
    pers_of_proj: Mapped[str] = mapped_column(String(100), nullable=False)
    n_phone: Mapped[str] = mapped_column(String(100), nullable=False)
    sel_emp: Mapped[int] = mapped_column(Integer, nullable=False)
    nots: Mapped[str] = mapped_column(String(500), nullable=False)
    is_active: Mapped[int] = mapped_column(TINYINT(1), nullable=False, server_default=text("'1'"))

    project_guards: Mapped[list['ProjectGuards']] = relationship('ProjectGuards', back_populates='project')


class SalaryHistory(Base):
    __tablename__ = 'salary_history'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    emp_id: Mapped[int] = mapped_column(Integer, nullable=False)
    project_id: Mapped[int] = mapped_column(Integer, nullable=False)
    pay_method: Mapped[str] = mapped_column(String(100), nullable=False)
    pay_for: Mapped[str] = mapped_column(String(100), nullable=False)
    sum: Mapped[int] = mapped_column(Integer, nullable=False)
    nots: Mapped[str] = mapped_column(TEXT, nullable=False)
    done_or_not: Mapped[int] = mapped_column(TINYINT(1), nullable=False, server_default=text("'0'"))
    data_entry_clerk_id: Mapped[Optional[str]] = mapped_column(String(150))
    process_supervisor_id: Mapped[Optional[int]] = mapped_column(Integer)
    responsible_emp_id: Mapped[Optional[str]] = mapped_column(String(150))


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    role: Mapped[str] = mapped_column(String(100), nullable=False)


class WorkShifts(Base):
    __tablename__ = 'work_shifts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    employee_id_input: Mapped[int] = mapped_column(Integer, nullable=False)
    project_id_input: Mapped[int] = mapped_column(Integer, nullable=False)
    start_day: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    start_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    end_day: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    file_path: Mapped[str] = mapped_column(String(100), nullable=False)


class ProjectGuards(Base):
    __tablename__ = 'project_guards'
    __table_args__ = (
        ForeignKeyConstraint(['employee_id'], ['employee.id'], name='fk_pg_emp'),
        ForeignKeyConstraint(['project_id'], ['projuct.id'], name='fk_pg_proj'),
        Index('fk_pg_emp', 'employee_id'),
        Index('fk_pg_proj', 'project_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_name: Mapped[str] = mapped_column(String(100), nullable=False)
    employee_name: Mapped[str] = mapped_column(String(100), nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    emp: Mapped[str] = mapped_column(String(100), nullable=False)
    nots: Mapped[str] = mapped_column(String(500), nullable=False)
    is_active: Mapped[int] = mapped_column(TINYINT(1), nullable=False, server_default=text("'1'"))
    project_id: Mapped[Optional[int]] = mapped_column(Integer)
    employee_id: Mapped[Optional[int]] = mapped_column(Integer)
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    employee: Mapped[Optional['Employee']] = relationship('Employee', back_populates='project_guards')
    project: Mapped[Optional['Projuct']] = relationship('Projuct', back_populates='project_guards')
