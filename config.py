from os import environ  
  
class Config:
     API_ID = int(environ.get("API_ID", 10000844)) 
     API_HASH = environ.get("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b") 
     BOT_TOKEN = environ.get("BOT_TOKEN", "6998167875:AAEr3DxL2t5zA37GuhRDZ1r6xrBwSIcQS5E")  
     BOT_SESSION = environ.get("BOT_SESSION", "bot")  
     DATABASE_URI = environ.get("DATABASE", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") 
     DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0") 
     BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5019308664').split()] 
  
class temp(object): 
     lock = {} 
     CANCEL = {} 
     forwardings = 0 
     BANNED_USERS = [] 
     IS_FRWD_CHAT = [] 
 
