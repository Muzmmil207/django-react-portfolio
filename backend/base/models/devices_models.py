from django.db import models
from django.utils.translation import gettext_lazy as _


class DeviceTrack(models.Model):
    """Model for connected devices tracking"""

    class DeviceType(models.TextChoices):
        """Device type choices"""

        WINDOWS = "windows", _("Windows")
        MAC = "mac", _("Mac")
        LINUX = "linux", _("Linux")
        ANDROID = "android", _("Android")
        IOS = "ios", _("Ios")
        OTHER = "other", _("Other")

    user_agent = models.CharField(
        verbose_name="User Agent",
        help_text="e.g. Chrome 98, Windows, TECNO KE5, Android",
        max_length=255,
        blank=True,
        null=True,
    )
    user_device = models.CharField(max_length=12, choices=DeviceType.choices)
    ip_address = models.GenericIPAddressField(
        verbose_name="IP Address",
        help_text="IP address of the device",
        null=True,
        blank=True,
    )
    location = models.CharField(
        verbose_name="Location",
        help_text="Location of the device",
        max_length=255,
        blank=True,
        null=True,
    )
    visited_data = models.DateTimeField(
        help_text="The time when the user visit",
        auto_now=True,
    )

    class Meta:
        """Meta options for the model"""

        verbose_name = "Device Activity"
        verbose_name_plural = "Device Activity"
        ordering = ("-visited_data",)
        db_table = "device_track"

    def __str__(self):
        """String representation of the model."""
        return f"{self.user_agent}, Location: {self.location},\
                Last Activity - {self.visited_data}"
