from django.utils import timezone
from django.db.models import Max

class AutoNumberMixin:
    """
    為模型自動產生唯一流水號（每年從001開始）
    格式範例: 'Q-2025-001'
    必須設置:
        `number_prefix`: 流水號前綴
        `number_field_name`: 流水號
    """
    number_prefix = ''  # 子類需指定，例如 'Q'
    number_field_name = 'number'  # 預設欄位名稱

    def generate_number(self):
        current_year = timezone.now().year
        prefix = f"{self.number_prefix}-{current_year}"

        ModelClass = self.__class__
        number_field = self._meta.get_field(self.number_field_name).attname

        # 取得最大號碼
        max_number = (
            ModelClass.objects
            .filter(**{f"{self.number_field_name}__startswith": prefix})
            .aggregate(Max(self.number_field_name))
            [f"{self.number_field_name}__max"]
        )

        if max_number:
            try:
                last_num = int(max_number.split('-')[-1])
            except ValueError:
                last_num = 0
        else:
            last_num = 0

        return f"{prefix}-{last_num + 1:03d}"

    def save(self, *args, **kwargs):
        if not getattr(self, self.number_field_name):
            number = self.generate_number()
            setattr(self, self.number_field_name, number)

        super().save(*args, **kwargs)
