from django.db import models

class File(models.Model):
    # blank=False : 해당 필드가 비어 있으면 안됨.
    # null=False : 디폴트값으로 True인 경우에 장고는 db에 NULL로 저장
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

