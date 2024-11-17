from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from database import Base, engine
from sqlalchemy.orm import relationship
# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    project_id = Column(Integer, nullable=True)  # Optional field for project association
'''# Employee model
# Employee model
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    
u    # Relationship with projects
    projects = relationship("Project", back_populates="employee")


# Project model
class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    employee_id = Column(Integer, ForeignKey('employees.id'))

    # Relationship with employee
    employee = relationship("Employee", back_populates="projects")
    
    # Relationship with team members
    team_members = relationship("TeamMember", back_populates="project")


# TeamMember model
class TeamMember(Base):
    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))

    # Relationship with project
    project = relationship("Project", back_populates="team_members")'''



'''class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String)

    projects = relationship("Project", back_populates="employee")
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    start_date = Column(String)
    end_date = Column(String)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    team_members = relationship("TeamMember", back_populates="project")


class TeamMember(Base):
    __tablename__ = "team_members"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="team_members")
# Create tables
Base.metadata.create_all(bind=engine)'''
