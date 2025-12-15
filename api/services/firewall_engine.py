from scapy.all import sniff
from api.repositories.rule_repo import RuleRepository
from api.services.logger_service import LoggerService


class FirewallEngine:

    @staticmethod
    def apply_rules(packet):
        rules = RuleRepository.get_all()

        # Ambil informasi paket
        try:
            src_ip = packet[0][1].src
            dst_ip = packet[0][1].dst
            protocol = packet[0][2].name.lower()
            port = packet[0][2].dport
        except:
            # Jika paket tidak memiliki info lengkap
            protocol = "unknown"
            port = 0

        for rule in rules:

            match_ip = (not rule.ip_address) or (rule.ip_address == src_ip)
            match_port = (not rule.port) or (rule.port == port)
            match_proto = (not rule.protocol) or (rule.protocol.lower() == protocol)

            if match_ip and match_port and match_proto:
                # Rule terpenuhi
                LoggerService.log_packet(packet, rule.action)
                return rule.action

        # Tidak ada rule cocok → default allow
        LoggerService.log_packet(packet, "allow")
        return "allow"

    @staticmethod
    def start_sniffing(interface=None):
        """
        Memulai proses sniffing paket jaringan.
        
        interface = Nama interface jaringan (ex: "Wi-Fi", "Ethernet", "eth0")
        jika None → Scapy memilih default interface.
        """

        print("[FirewallEngine] Sniffing started...")
        sniff(prn=FirewallEngine.apply_rules, iface=interface, store=False)
