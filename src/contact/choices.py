from django.db.models import TextChoices

class SocialMedia(TextChoices):
    INSTAGRAM = 'Инстаграм', 'Инстаграм'
    TIK_TOK = 'ТикТок', 'ТикТок'
    WHATSAPP = 'Вотцап', 'Вотцап'
    TELEGRAM = 'Телеграм', 'Телеграм'