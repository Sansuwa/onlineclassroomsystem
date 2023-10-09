from django.db import models

# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    



class Category(TimeStampModel):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
        
    def __str__(self):
        return self.name
    
class Label(TimeStampModel):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
class Priority(models.TextChoices):
    LOWEST = "lowest" ,"LOWEST"
    LOW = "low" ,"LOW"
    MEDIUM = "medium","MEDIUM"
    HIGH = "high","HIGH"
    HIGHEST = "highest","HIGHEST"   
    
# class TaskPriority(TimeStampModel):
#     name  = models.CharField()
   
    
class Task(TimeStampModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    image= models.ImageField(upload_to="todolist",blank=True,null=True)
    task_date = models.DateField(blank=True,null=True)
    priority = models.CharField(
        max_length=100,
        choices=Priority.choices,
        default=Priority.LOWEST
    )
        
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    labels=models.ManyToManyField(Label,blank=True)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


        