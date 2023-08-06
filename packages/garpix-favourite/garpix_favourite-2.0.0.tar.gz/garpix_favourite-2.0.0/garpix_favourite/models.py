from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from garpix_user.models import UserSession


class Favorite(models.Model):
    """
        Модель "Избранное" для пользователя.
    """

    user_session = models.ForeignKey(
        UserSession, on_delete=models.CASCADE, verbose_name=_('User'),
        related_name='favorites', editable=False
    )
    object_id = models.PositiveIntegerField(
        verbose_name=_('Object ID')
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, verbose_name=_('Content type'),
        editable=False,
    )
    content_object = GenericForeignKey(
        'content_type', 'object_id'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at')
    )

    def __str__(self):
        return 'User %i | Favorite: %s %s' % (
            self.user_session.id, self.object_id, self.content_object.__class__.__name__
        )

    class Meta:
        ordering = ('id',)
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')
        unique_together = (('user_session', 'content_type', 'object_id'),)
