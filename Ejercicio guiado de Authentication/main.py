from database import Session, Base, engine
from JWT_Manager import JWT_Manager
from flask import Flask
from usersrepository import UserRepository
from fruitsrepository import FruitRepository
from invoicesrepository import InvoiceRepository, InvoiceDetails
from routes import authentication_routes, fruits_routes, purchase_routes, invoices_routes
from models import User
from sqlalchemy import select

def create_initial_admin(users_repo):
    existing_admin = users_repo.session.execute(select(User).where(User.role == "admin"))
    result = existing_admin.scalars().first()
    if result:
        return

    users_repo.add_user("admin", "1234", "admin")

app = Flask("user-service")

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    with open("keys/private_key.pem", "rb") as file:
        private_key = file.read()

    with open("keys/public_key.pem", "rb") as file:
        public_key = file.read()

    jwt_manager = JWT_Manager(private_key, public_key)
    Base.metadata.create_all(engine)

    session = Session()

    users_repo = UserRepository(session)
    fruits_repo = FruitRepository(session)
    invoices_repo = InvoiceRepository(session)

    create_initial_admin(users_repo)

    authentication_routes(app, users_repo, jwt_manager)
    fruits_routes(app, fruits_repo, jwt_manager)
    purchase_routes(app, invoices_repo, jwt_manager)
    invoices_routes(app, invoices_repo, jwt_manager)

    app.run(host="localhost", port=5000, debug=True)
