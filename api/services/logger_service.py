from api.models.log import FirewallLog

class FirewallLogger:

    @staticmethod
    def log(src_ip, dst_ip, port, protocol, action):
        FirewallLog.objects.create(
            src_ip=src_ip,
            dst_ip=dst_ip,
            port=port,
            protocol=protocol,
            action_taken=action
        )
