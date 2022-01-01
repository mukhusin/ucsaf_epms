from django.db import models


# Create your models here.
# class Role(models.Model):
#     id=models.AutoField(primary_key=True)
#     role_name=models.CharField(max_length=255)
#     title=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()
    
# class Users(models.Model):
#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField(max_length=255)
#     title=models.CharField(max_length=255)
#     role=models.(Role,on_delete=models.SET_NULL)
#     email=models.CharField(max_length=255)
#     username=models.CharField(max_length=255)
#     password=models.CharField(max_length=255)
#     profile_pict=models.CharField(max_length=255)
#     is_active=models.BooleanField(default=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Common_Project(models.Model):
#     id=models.AutoField(primary_key=True)
#     common_project_name=models.CharField(primary_key=255)
#     common_project_descrption=models.TextField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()


# class Common_Phase(models.Model):
#     id=models.AutoField(primary_key=255)
#     common_project_id=models.ForeignKey(Common_Project,on_delete=models.CASCADE)
#     common_phase_name=models.CharField(max_length=255)
#     common_phase_description=models.TextField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project(models.Model):
#     id=models.CharField(max_length=255)
#     project_name=models.CharField(max_length=255)
#     common_project_id=models.ForeignKey(Common_Project,on_delete=models.CASCADE)
#     common_project_description=models.TextField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project_Leader(models.Model):
#     id=models.AutoField(primary_key=True)
#     project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
#     user_id=models.ForeignKey(Users,on_delete=models.CASCADE)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project_Phase(models.Model):
#     id=models.AutoField(primary_key=True)
#     common_phase_id=models.ForeignKey(Common_Phase,on_delete=models.CASCADE)
#     project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
#     status=models.BooleanField(default=False)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project_Lot(models.Model):
#     id=models.AutoField(primary_key=255)
#     project_id=models.ForeignKey(Project,on_delete=models.CASCADE)
#     lot_number=models.IntegerField()
#     region=models.CharField(max_length=100)
#     district=models.CharField(max_length=100)
#     ward=models.CharField(max_length=100)
#     village=models.CharField(max_length=100)
#     subsidy=models.DecimalField(max_digits=10,decimal_places=2)
#     status=models.CharField( max_length=50)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()
 
# class Mno_Lot(models.Model):
#     id=models.AutoField(primary_key=True)
#     mno_id=models.ForeignKey(Users, on_delete=models.CASCADE)
#     project_lot_id=models.ForeignKey(Project_Lot, on_delete=models.CASCADE)
#     number_of_site=models.IntegerField()
#     population=models.IntegerField()
#     minimum_signal_level=models.IntegerField()
#     isApproved=models.BooleanField(default=False)
#     status=models.CharField(max_length=100)
#     subsidy=models.DecimalField(max_digits=10, decimal_places=2)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project_Lot_Plan(models.Model):
#     id=models.AutoField(primary_key=True)
#     mno_lot_id=models.ForeignKey(Mno_Lot, on_delete=models.CASCADE)
#     activity_name=models.CharField(max_length=200)
#     start_date=models.DateField(auto_now=False, auto_now_add=False)
#     days_required=models.DateField(auto_now=False, auto_now_add=False)
#     predecessor=models.CharField(max_length=255)
#     successor=models.CharField(max_length=255)
#     risk=models.TextField()
#     isPublished=models.BooleanField(default=False)
#     end_date=models.DateField(auto_now=False, auto_now_add=False)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Lot_Progress(models.Model):
#     id=models.AutoField(primary_key=True)
#     lot_progress_name=models.CharField(max_length=255)
#     lot_progress_percentage=models.DecimalField(max_digits=10, decimal_places=2)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Mno_Lot_Progress(models.Model):
#     id=models.AutoField(primary_key=True)
#     lot_progress_id=models.ForeignKey(Lot_Progress, on_delete=models.CASCADE)
#     mno_id=models.ForeignKey(Users, on_delete=models.CASCADE)
#     isDone=models.BooleanField(default=False)
#     status=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project_Activity(models.Model):
#     id=models.AutoField(primary_key=True)
#     project_id=models.ForeignKey(Project, on_delete=models.CASCADE)
#     project_activity_name=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()

# class Project_Activity_Schedule(models.Model):
#     id=models.AutoField(primary_key=True)
#     project_activity_id=models.ForeignKey(Project_Activity, on_delete=models.CASCADE)
#     day_from_start=models.DateField(auto_now=False, auto_now_add=False)
#     plan_calender_date=models.DateTimeField(auto_now=False, auto_now_add=False)
#     status=models.CharField(max_length=255)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()
    
# class Lot_Site(models.Model):
#     id=models.AutoField(primary_key=True)
#     mno_lot_id=models.ForeignKey(Mno_Lot, on_delete=models.CASCADE)
#     lot_site_name=models.CharField(max_length=255)
#     site_id=models.CharField(max_length=255)
#     long_cordinate=models.CharField(max_length=50)
#     lat_cordinate=models.CharField(max_length=50)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     objects=models.Manager()