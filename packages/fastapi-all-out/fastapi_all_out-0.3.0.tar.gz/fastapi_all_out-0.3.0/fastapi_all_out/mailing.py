from datetime import timedelta
from enum import Enum
from typing import Any, TypedDict, TYPE_CHECKING

from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import EmailStr, ValidationError

from fastapi_all_out.lazy import get_settings_obj, get_mail_settings
from fastapi_all_out.settings import MailingConfig
from fastapi_all_out.utils import timedelta_to_string

if TYPE_CHECKING:
    from fastapi_all_out.auth.base import BaseUser, TempCodeProto


HOST = get_settings_obj().HOST
mail_settings: "MailSettingsType" = get_mail_settings()
endpoints = mail_settings['endpoints']


class MailSettingsType(TypedDict):
    sender: str
    endpoints: dict[str, str]
    temp_code_duration: dict[Enum | str, timedelta]


class MailSender:

    fast_mail: FastMail

    def __init__(self, conf: MailingConfig):
        self.fast_mail = FastMail(conf)

    async def send(
            self,
            to: EmailStr | str,
            data: dict[str, Any],
            template: str,
            subject: str
    ):
        email_msg = MessageSchema(
            subject=subject,
            recipients=[to],
            template_body=data,
            subtype=MessageType.html
        )
        await self.fast_mail.send_message(email_msg, template_name=template)

    async def send_tempcode_email(
            self,
            user: "BaseUser",
            temp_code: "TempCodeProto",
            host: str,
            endpoint: str,
            template: str,
            subject: str,
            **kwargs
    ) -> None:
        data = {
            'user': user, 'temp_code': temp_code, 'code': temp_code.code,
            'duration_text': timedelta_to_string(temp_code.duration),
            'host': host, 'endpoint': endpoint,
            **kwargs
        }
        await self.send(to=user.email, data=data, template=template, subject=subject)

    async def activation_email(self, user: "BaseUser", temp_code: "TempCodeProto") -> None:
        await self.send_tempcode_email(
            user=user,
            temp_code=temp_code,
            host=HOST,
            endpoint=endpoints['activation'],
            template='activation.html',
            subject='Account activation',
        )

    async def email_change_email(self, user: "BaseUser", temp_code: "TempCodeProto", new_email: str) -> None:
        await self.send_tempcode_email(
            user=user,
            temp_code=temp_code,
            host=HOST,
            endpoint=endpoints['email_change'],
            template='email_change.html',
            subject='Email change',
            new_email=new_email,
        )

    async def password_reset_email(self, user: "BaseUser", temp_code: "TempCodeProto") -> None:
        await self.send_tempcode_email(
            user=user,
            temp_code=temp_code,
            host=HOST,
            endpoint=endpoints['password_reset'],
            template='password_reset.html',
            subject='Password reset',
        )


try:
    mail_sender = MailSender(MailingConfig())
except ValidationError:
    mail_sender = None
