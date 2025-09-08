import enum
from datetime import datetime
from sqlmodel import Field, SQLModel, Relationship


class ProductCategory(str, enum.Enum):
    COFFEE = "coffee"
    TEA = "tea"
    PASTRY = "pastry"
    SANDWICH = "sandwich"
    DRINK = "drink"
    OTHER = "other"

class ShopType(str, enum.Enum):
    CAFE = "cafe"
    KIOSK = "kiosk"
    FRANCHISE = "franchise"
    ROASTER = "roaster"
    OTHER = "other"


class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ShopModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    type: ShopType = Field(default=ShopType.CAFE, nullable=False)
    address: str | None = Field(default=None)
    city: str | None = Field(default=None)
    country: str | None = Field(default="Unknown")
    phone: str | None = Field(default=None)
    email: str | None = Field(default=None)
    website: str | None = Field(default=None)

    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.now, 
        sa_column_kwargs={"onupdate": datetime.now}
    )
    is_active: bool = Field(default=True)
    products: list["ProductModel"] = Relationship(back_populates="shop")
    orders: list["OrderModel"] = Relationship(back_populates="shop")




class ProductModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    shop_id: int = Field(foreign_key="shops.id", nullable=False)

    name: str = Field(index=True, nullable=False)
    description: str | None = Field(default=None)
    category: ProductCategory = Field(default=ProductCategory.COFFEE, nullable=False)

    price: float = Field(default=0.0, nullable=False)
    is_available: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"onupdate": datetime.now}
    )
    shop: "ShopModel" = Relationship(back_populates="products")
    order_items: list["OrderItemModel"] = Relationship(back_populates="product")




class OrderModel(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    shop_id: int = Field(foreign_key="shops.id", nullable=False)
    customer_name: str = Field(nullable=False)
    status: OrderStatus = Field(default=OrderStatus.PENDING, nullable=False)

    total_amount: float = Field(default=0.0, nullable=False)

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column_kwargs={"onupdate": datetime.utcnow}
    )
    shop: "ShopModel" = Relationship(back_populates="orders")
    items: list["OrderItemModel"] = Relationship(back_populates="order")


class OrderItemModel(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="orders.id", nullable=False)
    product_id: int = Field(foreign_key="products.id", nullable=False)

    quantity: int = Field(default=1, nullable=False)
    unit_price: float = Field(default=0.0, nullable=False)
    subtotal: float = Field(default=0.0, nullable=False)
    order: "OrderModel" = Relationship(back_populates="items")
    product: "ProductModel" = Relationship(back_populates="order_items")
