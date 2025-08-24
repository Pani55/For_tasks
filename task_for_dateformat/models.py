from django.db import models
from datetime import datetime


# Create y models here.
class TestModel(models.Model):
    date_field = models.DateField()

    def get_month_week(self):
        # Получаем номер месяца
        month = self.date_field.strftime('%m')
        # Получаем номер недели в году
        week_number = self.date_field.isocalendar()[1]
        # Вычисляем номер недели в месяце
        first_day = datetime(self.date_field.year, self.date_field.month, 1)
        week_in_month = week_number - first_day.isocalendar()[1] + 1
        return f"{month}/{week_in_month}"
