What This Project Is:
built a Flask REST API that connects HTTP requests to a SQLite database using SQLAlchemy.

What I learned:
Flask — how to spin up a lightweight Python web server and define URL routes with @app.route()
SQLAlchemy ORM — how to define database models as Python classes instead of writing raw SQL, and how columns map to data types
Full CRUD operations — implementing all four HTTP methods (GET, POST, PUT, DELETE) and mapping them to database actions
SQLite integration — setting up a local file-based database with zero configuration using sqlite:///
Session management — understanding db.session.add() and db.session.commit() as the "save" mechanism for database changes
JSON serialization — why a to_dict() method is needed to convert SQLAlchemy model objects into JSON-friendly dictionaries
RESTful routing conventions — how URL patterns like /destinations/<id> with different HTTP methods represent different actions on the same resource
Basic error handling — returning 404 responses when a resource isn't found vs. 201 on successful creation
