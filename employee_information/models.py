from datetime import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 


TYPEOFVISASTATUS =(
    
    ('في انتضار الدفع','في انتضار الدفع'),
    ('ينتضر القبول','ينتضر القبول'),
    ('ينتضر الدعوة','ينتضر الدعوة'),
    ('ينتضر الاستفبال في المطار','ينتضر الاستفبال في المطار'),
    ('وصل','وصل'),

    
)

# Create your models here.
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    firstname = models.TextField(verbose_name="اللفب") 
    lastname = models.TextField(verbose_name="الاسم") 
    gender = models.TextField(blank=True,null= True,verbose_name="الجنس") 
    dob = models.DateField(blank=True,null= True,verbose_name="تاريخ الميلاد") 
    contact = models.TextField(verbose_name="رقم الهاتف") 
    department_id = models.ForeignKey(Department,default="", on_delete=models.CASCADE,verbose_name="الفرع") 
    position_id = models.ForeignKey(Position,default="", on_delete=models.CASCADE,verbose_name="حالة الزبون") 
    date_hired = models.DateField(verbose_name="تاريخ بداية الفيزا") 
    salary = models.FloatField(default=0,verbose_name="الراتب اليومي auto") 
    status = models.IntegerField(default=1,verbose_name="يرجى عدم العبث يخص قاعدة البيانات") 
    date_added = models.DateTimeField(verbose_name="تاريخ الاضافة") 
    date_updated = models.DateTimeField(auto_now=True,verbose_name="") 
    pimage = models.ImageField(verbose_name="صورة جواز السفر")
    timage = models.ImageField(verbose_name="صورة وصل الدفع")
    Npassport = models.CharField(default="000000000",max_length=9,verbose_name="رقم جواز السفر")
    LesJoureDeTravaille  = models.IntegerField(default=6,validators=[MinValueValidator(3), MaxValueValidator(6)],verbose_name="عدد ايام العمل")    
    totalmadakhil = models.IntegerField(default=0,verbose_name="المدخول الكلي من العامل auto")
    typeofvisa = models.CharField(default='',choices=TYPEOFVISASTATUS,max_length=100,verbose_name="حالة الفيزا")
    LePaimentDeClient = models.IntegerField(default=000000,validators=[MinValueValidator(1), MaxValueValidator(250000)],verbose_name="دفع الزبون")
    
    
    
    def save(self, *args, **kwargs):
        if self.LesJoureDeTravaille  ==  6 :
            self.salary=3500 
            self.totalmadakhil = self.LesJoureDeTravaille * 200 
        elif self.LesJoureDeTravaille  ==  5:
            self.salary = 3300
            self.totalmadakhil = self.LesJoureDeTravaille * 200 + 200
        elif self.LesJoureDeTravaille  ==  4:
            self.salary = 3100
            self.totalmadakhil = self.LesJoureDeTravaille * 200 + 400

        elif self.LesJoureDeTravaille  ==  3:
            self.salary = 2900
            self.totalmadakhil = self.LesJoureDeTravaille * 200 + 400

        elif self.LesJoureDeTravaille  ==  2:
            self.salary = 2700
            self.totalmadakhil = self.LesJoureDeTravaille * 200 + 400

        else:
            self.salary = 0000
            self.totalmadakhil += 0000

        super(Employees, self).save(*args, **kwargs)
    
    
    def age(self):
        import datetime
        
        return int((datetime.date.today() - self.date_hired).days  )
    
    def NonPaye(self):

        
        return int(250000 - self.LePaimentDeClient  )
    
    
    def salairpourseman(self):
        
        return (self.LesJoureDeTravaille * self.salary) * 2
    
    
    
    


        

    

    
    def __str__(self):
        return self.firstname + ' '+self.lastname 