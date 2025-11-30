from django.db import models
import uuid

class Rule(models.Model):
    ACTION_CHOICES = (
        ("allow", "Allow"),
        ("block", "Block"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    ip_address = models.CharField(max_length=100, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    protocol = models.CharField(max_length=20, null=True, blank=True)

    action = models.CharField(
        max_length=10,
        choices=ACTION_CHOICES,
        default="allow"
    )

    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        info = []
        if self.ip_address:
            info.append(f"IP: {self.ip_address}")
        if self.port:
            info.append(f"Port: {self.port}")
        if self.protocol:
            info.append(f"Protocol: {self.protocol}")

        filter_desc = ", ".join(info) if info else "Any"
        return f"{self.action.upper()} - {filter_desc}"
