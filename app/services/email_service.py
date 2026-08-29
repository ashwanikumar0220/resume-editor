import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key=os.getenv("RESEND_API_KEY")


async def send_email(to_email:str,subject:str,html:str):
    params:resend.Emails.SendParams ={
    "from":"onboarding@resend.dev",
    "to":"manas788899@gmail.com",
    "subject": subject,
    "html":html,
    }

    return await resend.Emails.send_async(params)

    