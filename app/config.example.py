class Config:
    DB_URI = ""
    SECRET_KEY = ""

    MAIL_SERVER: str # Outlook: smtp.office365.com; Gmail: smtp.gmail.com
    MAIL_PORT: int # Outlook: 587; Gmail: 465
    MAIL_USERNAME: str #Your mail
    MAIL_PASSWORD: str #Your password
    MAIL_USE_TLS = False
    MAIL_USE_TLS = True
