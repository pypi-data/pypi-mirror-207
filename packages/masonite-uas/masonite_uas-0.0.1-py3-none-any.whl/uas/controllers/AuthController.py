from masonite.controllers import Controller 
from uas.services.AuthService import auth_service

from uas.models.AccessLocation import AccessLocation 
from uas.models.Country import Country 
from uas.models.EmailToken import EmailToken 
from uas.models.IpAddress import IpAddress 
from uas.models.PendingLogin import PendingLogin 
from uas.models.Profile import Profile 
from uas.models.SessionUser import SessionUser 
from uas.models.User import User 
from uas.models.UserAgent import UserAgent 
from uas.models.UserSession import UserSession 
from uas.models.UserToken import UserToken 

class AuthController(Controller):

    def info(self): 
        return {
            "status" : "ok",
            "message" : "INFO", 
            "data" : { 
                "version" : "v0.0.0"
            }
        }

    def debug(self): 
        auth_service.generate_random_token()

        return {
            "status" : "ok", 
            "message" : "DEBUG", 
            "data" : {}
        }