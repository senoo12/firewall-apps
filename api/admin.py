from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'port', 'protocol', 'action', 'description')

@admin.register(FirewallLog)
class FirewallLogAdmin(admin.ModelAdmin):
    list_display = ('src_ip', 'dst_ip', 'port', 'protocol', 'action_taken', 'timestamp')