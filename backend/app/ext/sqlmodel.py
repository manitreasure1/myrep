from typing import AsyncGenerator, Optional

from flask import Flask
from sqlmodel import SQLModel, create_engine, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


class FlaskSQLModel:
    def __init__(self, model_cls=SQLModel) -> None:
        self.model_cls = model_cls
        self.engine = None
        self.async_engine = None
        self.async_session_factory: Optional[sessionmaker] = None

    def init_app(self, app: Flask):
        """Initialize SQLModel engine(s) from Flask config."""
        database_url = app.config.get("SQLMODEL_DATABASE_URI")
        if not database_url:
            raise RuntimeError("SQLMODEL_DATABASE_URI is required in app.config")

        echo = app.config.get("SQLMODEL_ECHO", False)
        use_async = app.config.get("SQLMODEL_ASYNC", False)

        if use_async:
            self.async_engine = create_async_engine(database_url, echo=echo, future=True)
            self.async_session_factory = sessionmaker(
                bind=self.async_engine, # type: ignore
                class_=AsyncSession,
                expire_on_commit=False,
                autoflush=False,
                autocommit=False,
            ) # type: ignore
        else:
            # Sync engine
            self.engine = create_engine(database_url, echo=echo, future=True)

        # Register extension
        app.extensions["sqlmodel"] = self

        # Auto-create tables if requested
        if app.config.get("SQLMODEL_AUTO_CREATE", False):
            if use_async:
                raise RuntimeError(
                    "SQLMODEL_AUTO_CREATE is not supported with async engine. "
                    "Call init_async_db() manually."
                )
            self.model_cls.metadata.create_all(self.engine) # type: ignore

    # -----------------------
    # SYNC
    # -----------------------
    def session(self) -> Session:
        """Get a sync session bound to the engine."""
        if not self.engine:
            raise RuntimeError("Sync engine is not initialized. Did you call init_app(app)?")
        return Session(self.engine)
    
    def session_scope(self):
        """Context manager for session (preferred in raw Flask routes)."""
        if not self.engine:
            raise RuntimeError("Engine is not initialized")
        return Session(self.engine)

    def init_db(self, drop_all: bool = False):
        """Initialize sync database (drop & create tables)."""
        if not self.engine:
            raise RuntimeError("Sync engine is not initialized.")
        if drop_all:
            self.model_cls.metadata.drop_all(self.engine)
        self.model_cls.metadata.create_all(self.engine)

    # -----------------------
    # ASYNC
    # -----------------------
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Async session generator for use in async contexts."""
        if not self.async_session_factory:
            raise RuntimeError("Async engine is not initialized. Did you call init_app(app)?")
        async with self.async_session_factory() as session:
            yield session

    async def init_async_db(self, drop_all: bool = False):
        """Initialize async database (drop & create tables)."""
        if not self.async_engine:
            raise RuntimeError("Async engine is not initialized.")
        async with self.async_engine.begin() as conn:
            if drop_all:
                await conn.run_sync(self.model_cls.metadata.drop_all)
            await conn.run_sync(self.model_cls.metadata.create_all)

sqlmodel = FlaskSQLModel()
