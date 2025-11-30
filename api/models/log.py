from django.db import models
import uuid

class FirewallLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    src_ip = models.CharField(max_length=100)
    dst_ip = models.CharField(max_length=100)
    
    port = models.IntegerField()
    protocol = models.CharField(max_length=20)

    action_taken = models.CharField(max_length=10)  # allow/block
    
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.src_ip} → {self.dst_ip} ({self.action_taken})"