from django.db import models
class Gym(models.Model):
    workoutname = models.CharField(max_length = 50) 
    picture = models.FileField()
    email = models.EmailField(blank = False) 
    workoutdesc = models.TextField(blank=False)
    def __str__(self):
        return self.workoutname




    def uploadata_fields_blank(self):
        return(self.workoutname != False)

    def TestWorkout(self):
        return (len(self.workoutname) >= 3) and (len(self.workoutname) <= 50) 
       
    def email_fields_blank(self):
        return (self.email != False)
 
    def workoutdes_field_blank(self):
        return (self.workoutdesc != True ) and (len(self.workoutdesc) <= 50)







