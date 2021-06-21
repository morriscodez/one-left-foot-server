from oneleftfootapi.models import skill_level
from django.db import models
from django.db.models.deletion import CASCADE

class DanceTypeJoin(models.Model):

    dance_user = models.ForeignKey("DanceUser", on_delete=models.CASCADE)
    dance_type = models.ForeignKey("DanceType", on_delete=models.CASCADE)
    skill_level = models.ForeignKey("SkillLevel", on_delete=models.CASCADE)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("dance_user", "dance_type")