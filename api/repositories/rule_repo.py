from api.models.rule import Rule


class RuleRepository:

    @staticmethod
    def get_all():
        """Ambil seluruh rule"""
        return Rule.objects.all().order_by("-created_at")

    @staticmethod
    def get_by_id(rule_id):
        """Ambil rule berdasarkan ID"""
        try:
            return Rule.objects.get(id=rule_id)
        except Rule.DoesNotExist:
            return None

    @staticmethod
    def create(data):
        """Buat rule baru"""
        return Rule.objects.create(**data)

    @staticmethod
    def update(rule, data):
        """Update rule"""
        for key, value in data.items():
            setattr(rule, key, value)
        rule.save()
        return rule

    @staticmethod
    def delete(rule_id):
        """Hapus rule"""
        return Rule.objects.filter(id=rule_id).delete()
