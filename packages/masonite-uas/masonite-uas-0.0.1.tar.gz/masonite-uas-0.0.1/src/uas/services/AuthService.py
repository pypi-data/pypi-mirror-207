import random 
import sys
from datetime import datetime, timedelta

from masonite_servicing import *
from masonite.facades import Config

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


class AuthService: 
    def __init__(self):     
        pass

    ################################
    # VISIT REGISTRATION (GENERAL) #
    ###############################
    def is_ip_registered(self, ip):
        return result("ok", "IS_IP_REGISTERED", False)

    def create_ip_visit_object(self, ip):
        ip_address = IpAddress() 
        ip_address.address = ip_address 
        ip_address.visit_count = 1 
        ip_address.last_visit_at = datetime.today() 
        return result("ok", "IP_VISIT_OBJECT", ip_address)

    def register_ip_visit(self, ip): 
        if fetch(self.is_ip_registered, ip): 
            return result("not-ok", "IP_ALREADY_REGISTERED", None)

        ip_visit_object = fetch(self.create_ip_visit_object, ip)
        ip_visit_object.save() 
    
    ####################
    # TOKEN GENERATION # 
    ####################
    def generate_random_token(self): 
        return result("OK", "RANDOM_TOKEN", ''.join("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")) 

    def determine_token_type(self, _type):
        TokenType = None 

        # determine token type #         
        if _type == "user": 
            TokenType = UserToken 
        elif __type == "email":
            TokenType = EmailToken 

        return result("ok", "TOKEN_TYPE", TokenType)

    def determine_token_target(self, _type):
        if _type == "user": 
            return "user_id" 
        elif _type == "email": 
            return "email"

    def get_expiration_time(self): 
        # get expiration time
        expiration_time = Config.get("uas.expiration_time")
        return result("ok", "EXPIRATION_TIME", datetime.today() + timedelta(minutes=expiration_time)) 

    def generate_token(self, _type, target):
        # create token instance
        token = self.determine_token_type(_type)()
        token.token = fetch(self.generate_random_token)
        token.expires_at = self.get_expiration_time()   
        setattr(token, _type, target)

        return result("ok", "AUTH_TOKEN", token)

auth_service = AuthService()