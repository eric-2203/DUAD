from models import Invoice, InvoiceDetails, Fruit, User
from sqlalchemy import select
from sqlalchemy.orm import selectinload

class InvoiceRepository:
    def __init__(self, session):
        self.session = session

    def get_all_invoices(self):
        result = self.session.execute(
            select(Invoice).options(
                selectinload(Invoice.invoice_details)
                .selectinload(InvoiceDetails.fruit)
            )
        )
        return result.scalars().all()

    def get_invoice_by_id(self, invoice_id):
        result = self.session.get(Invoice, invoice_id)
        return result

    def get_invoice_by_user(self, user_id):
        result = self.session.execute(
            select(Invoice)
            .options(
                selectinload(Invoice.invoice_details)
                .selectinload(InvoiceDetails.fruit)
            )
            .where(Invoice.user_id == user_id)
        )
        return result.scalars().all()

    def get_invoice_details(self, invoice_id):
        existing_invoice = self.get_invoice_by_id(invoice_id)
        if existing_invoice is None:
            raise ValueError("This invoice does not exist")

        result = self.session.execute(select(InvoiceDetails).where(InvoiceDetails.invoice_id == invoice_id))
        return result.scalars().all()

    def create_invoice(self, user_id, items):
        existing_user = self.session.get(User, user_id)
        if existing_user is None:
            raise ValueError("User does not exist in the database")

        subtotals = []
        invoice_items = []
        for item in items:
            fruit_id = item["fruit_id"]
            quantity = item["quantity"]
            fruit = self.session.get(Fruit, fruit_id)

            if fruit is None:
                raise ValueError("This fruit does not exist in the database")

            if not isinstance(quantity, int):
                raise ValueError("Quantity must be an integer")
            
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero")

            if fruit.stock_quantity < quantity:
                raise ValueError(f"There is not enough stock of {fruit.name} available to complete this purchase")

            subtotal = quantity * fruit.price

            invoice_items.append({"fruit_id": fruit_id, "quantity": quantity, "unit_price": fruit.price})
            subtotals.append(subtotal)
            

        total = sum(subtotals)

        invoice = Invoice(user_id=user_id, total=total)
        self.session.add(invoice)
        self.session.flush()

        for item in invoice_items:
            invoice_details = InvoiceDetails(invoice_id=invoice.id, fruit_id=item["fruit_id"], sold_quantity=item["quantity"], unit_price=item["unit_price"]
    )

            self.session.add(invoice_details)

        for item in invoice_items:
            fruit = self.session.get(Fruit, item["fruit_id"])
            fruit.stock_quantity -= item["quantity"]

        self.session.commit()

        return invoice