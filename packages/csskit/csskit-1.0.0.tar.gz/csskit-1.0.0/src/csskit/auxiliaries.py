
class ClassProperty:

    def __init__(self, cls_get, use_cache=False):
        self.cls_get = cls_get
        self.use_cache = use_cache
        self.name = None
        self.shadow_name = None

    def __set_name__(self, owner, name):
        self.name = name
        self.shadow_name = "__" + self.name

    def __get__(self, instance, cls=None):

        if instance is not None:
            cls = instance.__class__

        if cls is None:
            return self

        if not self.use_cache or self.shadow_name not in cls.__dict__:
            result = self.cls_get.__func__(cls)

            if self.use_cache:
                # cls.__dict__[self.shadow_name] = result
                setattr(cls, self.shadow_name, result)
        else:
            result = cls.__dict__[self.shadow_name]

        return result


def classproperty_inner(fn, use_cache=False): # noqa
    return ClassProperty(cls_get=classmethod(fn), use_cache=False)


def classproperty2(use_cache=False): # noqa
    def wrap(fn):
        return classproperty_inner(fn, use_cache=use_cache)
    return wrap


def classproperty(fn): # noqa
    return ClassProperty(cls_get=classmethod(fn), use_cache=True)


class LookupMixin:

    @classproperty
    def identifiers(cls):
        return []

    @classmethod
    def from_identifier(cls, item, default_value=None):

        if not hasattr(cls, '_lookup_cache'):
            cache = {}
            setattr(cls, '_lookup_cache', cache)

            q = [cls.__subclasses__()]

            while q:

                for t in q[0]:

                    if "identifiers" in t.__dict__:

                        for identifier in t.identifiers: # noqa
                            cache[identifier] = t

                    S = t.__subclasses__() # noqa

                    if S:
                        q.append(S)

                q.pop(0)

        else:
            cache = getattr(cls, '_lookup_cache')

        return cache.get(item, default_value)
