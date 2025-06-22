from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Connect to PostgreSQL
engine = create_engine("postgresql://user:pass@localhost:5432/mydb", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Table: Restaurant Tables
class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    #qr_code_url = Column(String(255), nullable=False)
    orders = relationship("Order", back_populates="table")


# Table: Menu Items
class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(50))
    is_available = Column(Boolean, default=True)
    order_items = relationship("OrderItem", back_populates="item")


# Table: Orders
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    total_price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="Pending")

    table = relationship("Table", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


# Table: Order Items
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    item = relationship("MenuItem", back_populates="order_items")


# Create all tables
Base.metadata.create_all(engine)
