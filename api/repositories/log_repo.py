from api.models.log import FirewallLog


class LogRepository:

    @staticmethod
    def get_all():
        """Ambil seluruh log"""
        return FirewallLog.objects.all().order_by("-timestamp")

    @staticmethod
    def create(data):
        """Buat log baru"""
        return FirewallLog.objects.create(**data)

    @staticmethod
    def delete_all():
        """Kosongkan semua log firewall"""
        FirewallLog.objects.all().delete()

    @staticmethod
    def get_recent(limit=100):
        """Ambil log terbaru (misalnya untuk dashboard)"""
        return FirewallLog.objects.all().order_by("-timestamp")[:limit]
