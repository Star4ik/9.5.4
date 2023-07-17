from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from NewsPaper.NewsPaper import settings
from NewsPaper.news.models import PostCategory


def send_notifications(preview, pk, title, subscribers):
    html_context = render_to_string(
        'post_create_email.html', {
            'text': preview,
            'link': f'{settings.SITE_URL}/{pk}'
        })
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_context, 'text/html')


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instanse, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instanse.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instanse.preview(), instanse.pk, instanse.title, subscribers)
