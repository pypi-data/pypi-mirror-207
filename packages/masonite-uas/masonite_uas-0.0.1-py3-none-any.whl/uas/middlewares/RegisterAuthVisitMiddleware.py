from masonite.middleware import Middleware


class RegisterAuthVisitMiddleware(Middleware):
    def before(self, request, response):
        return request

    def after(self, request, response):
        return request
