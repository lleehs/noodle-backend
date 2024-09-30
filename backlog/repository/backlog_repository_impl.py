from django.db import IntegrityError

from backlog.entity.backlog import Backlog
from backlog.repository.backlog_repository import BacklogRepository


class BacklogRepositoryImpl(BacklogRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def create(self, title):
        try:
            backlog = Backlog(title=title)
            backlog.save()

            return backlog

        except IntegrityError:
            return None

