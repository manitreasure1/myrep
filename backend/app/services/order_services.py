from typing import Sequence
from sqlmodel import Session, select
from database.models import OrderModel, OrderItemModel, ProductModel, OrderStatus


class OrderService:
    @staticmethod
    def create_order(session: Session, shop_id: int, customer_name: str, items: list[dict]) -> OrderModel:
        order = OrderModel(shop_id=shop_id, customer_name=customer_name, status=OrderStatus.PENDING)

        total = 0.0
        session.add(order)
        session.flush() 

        for item in items:
            product = session.get(ProductModel, item["product_id"])
            if not product:
                continue
            quantity = item.get("quantity", 1)
            unit_price = product.price
            subtotal = quantity * unit_price
            total += subtotal


            if order.id and  product.id:

                order_item = OrderItemModel(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=quantity,
                    unit_price=unit_price,
                    subtotal=subtotal
                )
                session.add(order_item)

        order.total_amount = total
        session.commit()
        session.refresh(order)
        return order

    @staticmethod
    def get_order(session: Session, order_id: int) -> OrderModel | None:
        return session.get(OrderModel, order_id)

    @staticmethod
    def list_orders(session: Session, shop_id: int | None = None) -> Sequence[OrderModel]:
        query = select(OrderModel)
        if shop_id:
            query = query.where(OrderModel.shop_id == shop_id)
        return session.exec(query).all()

    @staticmethod
    def update_status(session: Session, order_id: int, status: OrderStatus) -> bool:
        order = session.get(OrderModel, order_id)
        if not order:
            return False
        order.status = status
        session.add(order)
        session.commit()
        return True
