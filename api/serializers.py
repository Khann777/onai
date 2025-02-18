from pydantic import BaseModel, HttpUrl

class WebhookRequestSerializer(BaseModel):
    message: str
    callback_url: HttpUrl
