# Volunteer System

### A Python CLI application for managing nonprofit events, volunteers, and assignments using SQLAlchemy, SQLite, and Alembic migrations.

### By **Jackson**

## Project Description

The Volunteer System is a command-line interface (CLI) application designed to streamline event and volunteer management for nonprofit organizations. Built with Python, SQLAlchemy, SQLite, and Click, it allows users to create, list, assign, delete, and report on events and volunteers. The system supports tracking event details (name, date, location, required skills, and description) and volunteer information (name, email, phone, skills), with assignments linking volunteers to events. 

## Key features

- **Event Management**: Add, list, and delete events with details like location and required skills.
- **Volunteer Management**: Register, list, and delete volunteers with unique email validation.
- **Assignments**: Assign volunteers to events based on skill matches.
- **Reporting**: Generate detailed event reports with volunteer assignments.
- **Database Migrations**: Use Alembic to manage schema changes, such as adding a `description` column to events.

The CLI uses colored output (`yellow` for menu options, `blue` for headers, `green` for success, `red` for errors) and manual string formatting for a user-friendly experience. The SQLite database (`volunteer_system.db`) ensures persistent storage with `ForeignKey` constraints for data integrity.

## Project Structure

- **Database**: SQLite (`volunteer_system.db`)
- **Files**:
  - `model.py`: Defines SQLAlchemy models (`Event`, `Volunteer`, `Assignment`) with `ForeignKey` constraints.
  - `crud.py`: Handles database operations (create, read, delete).
  - `main.py`: Implements the CLI using Click.
  - `alembic/`: Alembic migration scripts for schema management.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:JACKMUNGAI001/volunteer_system.git
   cd volunteer_system

2. **Install Dependencies**:
   ```bash
pipenv install
pipenv shell

3. **Initialize Database**:
Run main.py or apply migrations to create volunteer_system.db.

4. **Initialize Alembic**:
   ```bash
alembic init alembic

In alembic.ini, set sqlalchemy.url = sqlite:///volunteer_system.db.
In alembic/env.py, add:
from model import Base
target_metadata = Base.metadata

5. **Apply Migrations**:
   ```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

6. **Run the CLI**:
   ```bash
python main.py

## Usage
Run python main.py to launch the interactive menu. Select an option (1-10):
1. Add Event: Create an event with name, date, location, required skills, and description.
2. List Events: Display all events in a table.
3.Add Volunteer: Add a volunteer with name, email, phone, and skills.
4. List Volunteers: Display all volunteers in a table.
5. Assign Volunteer: Assign a volunteer to an event with a date.
6. List Assignments: Show assignments for an event.
7. Event Report: Generate a report with event details and volunteers.
8. Exit: Close the application.
9. Delete Event: Remove an event and its assignments by ID.
10. Delete Volunteer: Remove a volunteer and their assignments by ID.

## Dependencies
- **sqlalchemy**: Database ORM.
- **click**: CLI interface with colored output.
- **alembic**: Database migrations.
- **pipenv**: Dependency management.


## Contact Details

- Email: <jacksonmungai001@gmail.com>

## License

MIT License

Copyright &copy; 2025 Jackson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.