
from masonite.middleware import IpMiddleware

from .RegisterVisitMiddleware import RegisterVisitMiddleware
from .RegisterAuthVisitMiddleware import RegisterAuthVisitMiddleware
from .RegisterAccessLocationMiddleware import RegisterAccessLocationMiddleware
from .SyncSessionUserMiddleware import SyncSessionUserMiddleware

UAS_MIDDLEWARES = [
    IpMiddleware,
    RegisterVisitMiddleware, 
    RegisterAuthVisitMiddleware, 
    RegisterAccessLocationMiddleware, 
    SyncSessionUserMiddleware
]