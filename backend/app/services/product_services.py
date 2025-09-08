from typing import Sequence
from sqlmodel import Session, select
from database.models import ProductModel


class ProductService:
    @staticmethod
    def create_product(session: Session, shop_id: int, name: str, price: float) -> ProductModel:
        product = ProductModel(shop_id=shop_id, name=name, price=price)
        session.add(product)
        session.commit()
        session.refresh(product)
        return product

    @staticmethod
    def get_product(session: Session, product_id: int) -> ProductModel | None:
        return session.get(ProductModel, product_id)

    @staticmethod
    def list_products(session: Session, shop_id: int | None = None) -> Sequence[ProductModel]:
        query = select(ProductModel)
        if shop_id:
            query = query.where(ProductModel.shop_id == shop_id)
        return session.exec(query).all()

    @staticmethod
    def delete_product(session: Session, product_id: int) -> bool:
        product = session.get(ProductModel, product_id)
        if not product:
            return False
        session.delete(product)
        session.commit()
        return True
