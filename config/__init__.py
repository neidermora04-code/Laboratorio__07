from django.template.context import BaseContext


def _base_context_copy(self):
    duplicate = BaseContext()
    duplicate.__class__ = self.__class__
    duplicate.__dict__ = self.__dict__.copy()
    duplicate.dicts = self.dicts[:]
    return duplicate


BaseContext.__copy__ = _base_context_copy
