import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

from pydantic import BaseModel, EmailStr


from core.logging import logger

from core.config import settings

class UserMail(BaseModel):
    email: EmailStr
    name: str
    

async def send_welcome_to_email(recipient_mail: EmailStr, recipient_name:str) -> bool:
    email = settings.MAIL_EMAIL
    password = settings.MAIL_PASS
    server = smtplib.SMTP_SSL('smtp.yandex.ru')
    server.set_debuglevel(0)
    server.secure = True
    try:
        server.login(email, password)
    except Exception as e:
        logger.error(f'unable to login. msg: {e}')
        return False


        
    part = MIMEBase('application', "octet-stream")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "DAILY"
    msg['From'] = email
    msg['To'] = recipient_mail
    msg.attach(part)

    html_template = MIMEText((f"<div>SUI*IIIIII HELO MISTER {recipient_name}</div>"), 'html')
    msg.attach(html_template)
    
    try:
        server.sendmail(email, recipient_mail, msg.as_string())
    except Exception as e:
        logger.error(f'unable to send message to {recipient_mail}. msg: {e}')
        return
    server.quit()
    return True


async def get_result(id:int):
    return id*id


