# api/middleware/firewall.py
from django.http import JsonResponse
from api.repositories.rule_repo import RuleRepository
from api.services.logger_service import FirewallLogger

class FirewallMiddleware:
    """
    Middleware firewall untuk memblokir / mengizinkan akses berdasarkan rule.
    Default: block.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Ambil IP client asli
        client_ip = (
            request.META.get("HTTP_X_FORWARDED_FOR").split(",")[0]
            if request.META.get("HTTP_X_FORWARDED_FOR")
            else request.META.get("REMOTE_ADDR")
        )

        # IP server (destination)
        dst_ip = request.META.get("SERVER_ADDR") or request.get_host().split(":")[0]

        port = request.META.get("SERVER_PORT")
        protocol = request.META.get("wsgi.url_scheme")  # http/https

        rules = RuleRepository.get_all()
        matched_rule = None

        # Cari rule yang cocok
        for rule in rules:
            if rule.ip_address and rule.ip_address != client_ip:
                continue
            if rule.port and str(rule.port) != str(port):
                continue
            if rule.protocol and rule.protocol.lower() != protocol.lower():
                continue

            matched_rule = rule
            break

        # Jika ada rule yang match
        if matched_rule:
            if matched_rule.action == "block":
                FirewallLogger.log(
                    src_ip=client_ip,
                    dst_ip=dst_ip,
                    port=port,
                    protocol=protocol,
                    action="block"
                )
                return JsonResponse({"error": "Access blocked"}, status=403)

            # ALLOW
            FirewallLogger.log(
                src_ip=client_ip,
                dst_ip=dst_ip,
                port=port,
                protocol=protocol,
                action="allow"
            )
            return self.get_response(request)

        # Default block untuk IP yang tidak ada rule
        FirewallLogger.log(
            src_ip=client_ip,
            dst_ip=dst_ip,
            port=port,
            protocol=protocol,
            action="block"
        )
        return JsonResponse({"error": "Access denied (default block)"}, status=403)
