from typing import Union, Callable, Optional, Any, Self
from datetime import timedelta, datetime
from string import ascii_uppercase, digits
from random import choices

from tortoise import fields, timezone

from fastapi_all_out.enums import TempCodeTriggers
from fastapi_all_out.lazy import get_user_model_path, get_mail_settings
from . import max_len_of
from . import BaseModel, BaseUser


class TempCode(BaseModel):
    id: int = fields.BigIntField(pk=True)
    user: Union["BaseUser", fields.ForeignKeyRelation["BaseUser"]] = fields.ForeignKeyField(
        get_user_model_path(), related_name='temp_code', on_delete=fields.CASCADE
    )
    code: str = fields.CharField(max_length=6)
    expired_at: datetime = fields.DatetimeField()
    trigger: TempCodeTriggers = fields.CharEnumField(TempCodeTriggers)
    extras: Optional[dict[str, Any] | list[Any]] = fields.JSONField(null=True)

    class Meta:
        abstract = True
        unique_together = ('user', 'trigger')

    @property
    def duration(self) -> timedelta:
        return get_tempcode_durations(self.trigger)

    @property
    def is_expired(self) -> bool:
        return timezone.now() > self.expired_at

    @classmethod
    async def new(
            cls,
            user: BaseUser,
            trigger: TempCodeTriggers,
            extras: Optional[dict[str, Any] | list[Any]] = None
    ) -> Self:
        return await cls.create(
            user=user,
            code=get_random_tempcode(max_len_of(cls)('code'))(),
            expired_at=timezone.now() + get_tempcode_durations(trigger),
            trigger=trigger,
            extras=extras
        )

    async def update(self, extras: Optional[dict[str, Any] | list[Any]] = None):
        self.code = get_random_tempcode(max_len_of(self.__class__)('code'))()
        self.expired_at = timezone.now() + self.duration
        if extras:
            self.extras = extras
        await self.save(force_update=True, update_fields=('code', 'expired_at', 'extras'))


def get_random_tempcode(code_len: int) -> Callable[[], str]:
    return lambda: ''.join(choices(ascii_uppercase + digits, k=code_len))


durations = get_mail_settings()['temp_code_duration']


def get_tempcode_durations(trigger: TempCodeTriggers) -> timedelta:
    return durations.get(trigger) or durations['_default']
