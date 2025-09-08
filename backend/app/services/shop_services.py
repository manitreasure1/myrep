from typing import Sequence
from sqlmodel import Session, select
from database.models import ShopModel


class ShopService:
    @staticmethod
    def create_shop(session: Session, name: str) -> ShopModel:
        shop = ShopModel(name=name)
        session.add(shop)
        session.commit()
        session.refresh(shop)
        return shop

    @staticmethod
    def get_shop(session: Session, shop_id: int) -> ShopModel | None:
        return session.get(ShopModel, shop_id)

    @staticmethod
    def list_shops(session: Session) -> Sequence[ShopModel]:
        return session.exec(select(ShopModel)).all()

    @staticmethod
    def delete_shop(session: Session, shop_id: int) -> bool:
        shop = session.get(ShopModel, shop_id)
        if not shop:
            return False
        session.delete(shop)
        session.commit()
        return True
