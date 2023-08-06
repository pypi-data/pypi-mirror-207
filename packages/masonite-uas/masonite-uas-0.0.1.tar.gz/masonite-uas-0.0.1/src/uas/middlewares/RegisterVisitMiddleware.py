from masonite.middleware import Middleware

from uas.services.AuthService import auth_service

class RegisterVisitMiddleware(Middleware):
    def before(self, request, response):
        auth_service.register_ip_visit(request.ip())        
        return request

    def after(self, request, response):
        return request
