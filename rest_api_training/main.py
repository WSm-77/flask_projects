from app import create_app, create_api
from database.database_setup import db, init_db

app = create_app()
api = create_api(app)

init_db(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)
