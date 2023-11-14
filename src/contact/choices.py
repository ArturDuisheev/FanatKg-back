from django.db.models import TextChoices


class SocialMedia(TextChoices):
    INSTAGRAM = 'Instagram', 'Instagram'
    TIK_TOK = 'TikTok', 'TikTok'
    WHATSAPP = 'WhatsApp', 'WhatsApp'
    TELEGRAM = 'Telegram', 'Telegram'
