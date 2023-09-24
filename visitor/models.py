from django.db import models

# Create your models here.
class visitor_model(models.Model):
    name = models.CharField(max_length = 180, unique= True, help_text= 'Please Enter Visitor Name')
    email = models.EmailField(max_length=180, help_text= 'Please Enter Visitor Email')
    mobile = models.CharField(max_length = 10,help_text='Please Enter Visitor 10 digit Phone Number')
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class staff_member_model(models.Model):
    name = models.CharField(max_length = 180,unique= True, help_text= 'Please Enter Staff Member Name')
    email = models.EmailField(max_length=180, help_text= 'Please Enter Staff Member Email')
    mobile = models.CharField(max_length = 10, help_text='Please Enter Staff Member 10 digit Phone Number')
    image = models.ImageField(upload_to ='uploads/', help_text= 'Please Enter Staff Member Image')

    def __str__(self):
        return self.name

class drink_model(models.Model):
    name = models.CharField(max_length = 180, unique=True, help_text= 'Please Enter Drink Name')
    serve_member_name = models.ForeignKey(staff_member_model, to_field='name', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class visitor_detail_model(models.Model):
    staff_member_name = models.ForeignKey(staff_member_model, to_field='name', on_delete=models.CASCADE)
    visitor_name = models.ForeignKey(visitor_model, to_field='name', on_delete=models.CASCADE)
    reason = models.CharField(max_length = 256, help_text= 'Please Enter Reason')
    state = models.CharField(max_length=20, default="Inprogress", help_text= 'Please Leave This Field as it is')
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.staff_member_name} - {self.visitor_name}"
    
class visitor_drink_model(models.Model):
    visitor_name = models.ForeignKey(visitor_model, to_field='name', on_delete=models.CASCADE)
    drink_name = models.ForeignKey(drink_model, to_field='name', on_delete=models.CASCADE)
    state = models.CharField(max_length=20, default="Inprogress", help_text= 'Please Leave This Field as it is')
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.visitor_name} - {self.drink_name}"
