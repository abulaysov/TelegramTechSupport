import dataclasses


@dataclasses.dataclass
class TelegramMessage:
    text: str
    chat_id: int
    message_id: int
    is_bot: bool = False
