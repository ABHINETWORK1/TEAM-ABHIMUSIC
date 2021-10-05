import threading

from TGNRobot.modules.sql import BASE, SESSION
from sqlalchemy import Boolean, Column, Integer, String, UnicodeText


class GloballyBannedUsers(BASE):
    __tablename__ = "gbans"
    user_id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False)
    reason = Column(UnicodeText)
    
    def __init__(self, user_id, name, reason=None):
        self.user_id = user_id
        self.name = name
        self.reason = reason

    def __repr__(self):
        return "<GBanned User {} ({})>".format(self.name, self.user_id)
        
    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "reason": self.reason}
        
        
class GbanSettings(BASE):    
    __tablename__ = "gban_settings"
    chat_id = Column(String(14), primary_key=True)
    setting = Column(Boolean, default=True, nullable=False)

    def __init__(self, chat_id, enabled):
        self.chat_id = str(chat_id)
        self.setting = enabled
    
    def __repr__(self):
        return "<Gban setting {} ({})>".format(self.chat_id, self.setting)
      
      
GloballyBannedUsers.__table__.create(checkfirst=True)
GbanSettings.__table__.create(checkfirst=True)
GbanSettings.__table__.create(checkfirst=True)
        
