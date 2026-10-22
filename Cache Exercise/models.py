from typing import List
from sqlalchemy import String, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import date
from decimal import Decimal

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, default="user")

    invoices: Mapped[List["Invoice"]] = relationship(back_populates="user")

    def to_dict(self):
        return {"id": self.id,
                "username": self.username,
                "role": self.role}


class Fruit(Base):
    __tablename__ = "fruits"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    date_received: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    invoice_details: Mapped[List["InvoiceDetails"]] = relationship(back_populates="fruit")

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "price": self.price,
                "stock_quantity": self.stock_quantity}

class Invoice(Base):
    __tablename__ = "invoices"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date_created: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    user: Mapped["User"] = relationship(back_populates="invoices")

    invoice_details: Mapped[List["InvoiceDetails"]] = relationship(back_populates="invoice", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "date_created": self.date_created,
                "total": self.total}


class InvoiceDetails(Base):
    __tablename__ = "invoice_details"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), nullable=False)
    fruit_id: Mapped[int] = mapped_column(ForeignKey("fruits.id"), nullable=False)
    sold_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    fruit: Mapped["Fruit"] = relationship(back_populates="invoice_details")

    invoice: Mapped["Invoice"] = relationship(back_populates="invoice_details")

    def to_dict(self):
        return {"id": self.id,
                "invoice_id": self.invoice_id,
                "fruit_id": self.fruit_id,
                "fruit_name": self.fruit.name,
                "sold_quantity": self.sold_quantity,
                "unit_price": self.unit_price}
