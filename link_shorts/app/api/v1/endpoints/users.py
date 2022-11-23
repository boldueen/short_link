from fastapi import APIRouter

from services.email_worker import get_result, send_welcome_to_email, UserMail

router = APIRouter()

@router.get('/', status_code=200)
async def user_test():
    return {
        "user":"new_user",
        "value":await get_result(5)
    }


@router.post('/send', status_code=200)
async def send_mail(email_info: UserMail):
    if(await send_welcome_to_email(email_info.email, email_info.name)):
        return{
            "message": "success"
        }
    else:
        return {"message": "error"}