from allauth.account.utils import filter_users_by_username
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
date_format = "%Y-%m-%d"

# Create your models here.
class PixelModel(models.Model):
    pixel_line = models.IntegerField(default=0)
    pixel_col = models.IntegerField(default=0)
    lat = models.FloatField(default = 0.0)
    lon = models.FloatField(default=0.0)
    landcov = models.IntegerField(default=0)
    elevation_m= models.IntegerField(default=0)
    class Meta:
        db_table = 'PixelModel'

    @classmethod
    def create_from_json_structure(cls, **kwargs):
        vegetable = cls.objects.create(pixel_line= kwargs['pixel_line'], pixel_col = kwargs['pixel_col'] , lat= kwargs['lat'],lon=kwargs['lon'],landcov=kwargs['landcov'],elevation_m=kwargs['elevation_m'])




class GrowModel(models.Model):
    id_growmodel = models.AutoField(primary_key=True)
    vegfamilyname = models.CharField(max_length=100)
    Kini_days = models.IntegerField(default=0)
    Kdev_days = models.IntegerField(default=0)
    Kmid_days = models.IntegerField(default=0)
    Klate_days = models.IntegerField(default=0)
    Kini = models.FloatField(default=0)
    Kmid = models.FloatField(default=0)
    Kend = models.FloatField(default=0)
    seed_date = models.DateField()
    class Meta:
        db_table = 'GrowModel'

    def __str__(self):
        return self.vegfamilyname
    def get_family(self):
        return self.family

    def get_Kc(self, NumOfDays):
        # datetime.strptime(date, date_format)
        B = self.Kini_days
        C = B + self.Kdev_days
        D = C + self.Kmid_days
        E = D + self.Klate_days
        if (NumOfDays <= B):
            return self.Kini
        if (NumOfDays > B and NumOfDays <= C):
            return (self.Kmid - self.Kini) / (self.Kdev_days) * NumOfDays + self.Kini * (
                        1 + self.Kini_days / self.Kdev_days) - self.Kini_days / self.Kdev_days * self.Kmid
        if (NumOfDays > C and NumOfDays <= D):
            return self.Kmid
        if (NumOfDays > D and NumOfDays <= E):
            return (self.Kend - self.Kmid) / self.Klate_days * NumOfDays + (
                        self.Kmid - (self.Kend - self.Kmid) / self.Klate_days * (D))
        if (NumOfDays > E):
            return self.Kend

    def get_Status(self, date):
        # nb of days since seed date
        NumOfDays = (date - self.seed_date).days
        B = 0 + self.Kini_days
        C = B + self.Kdev_days
        D = C + self.Kmid_days
        E = D + self.Klate_days
        if (NumOfDays <= B):
            return "germination/growth/initial stage"
        if (NumOfDays > B and NumOfDays <= C):
            return "dev stage"
        if (NumOfDays > C and NumOfDays <= D):
            return "mid stage"
        if (NumOfDays > D and NumOfDays <= E):
            return "late stage"
        if (NumOfDays > E):
            return "end stage"


class VegetableModel(models.Model):
    id_growmodel = models.ForeignKey(GrowModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    crop_category = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    scient_name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    culture_advice = models.CharField(max_length=100)
    culture_seeding = models.CharField(max_length=100)
    culture_type = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=100)
    min_max_harvest_month = models.CharField(max_length=100)
    min_max_seed_month_inside = models.CharField(max_length=100)
    min_max_seed_month_outside = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    seeding_advice = models.CharField(max_length=100)
    soil_nature = models.CharField(max_length=100)
    soil_quality = models.CharField(max_length=100)
    sun_expo = models.CharField(max_length=100)
    texture = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    water_need = models.CharField(max_length=100)
    class Meta:
        db_table = 'VegetableModel'
    def __str__(self):
        return self.name
    def get_family(self):
        return self.family
    @classmethod
    def create_from_json_structure(cls, **kwargs):
        vegetable = cls.objects.create(
            name=kwargs['category'],
            scient_name=kwargs['scient_name'],
            family=kwargs['family'],
            colour=kwargs['colour'],
            culture_advice=kwargs['culture_advice'],
            culture_seeding=kwargs['culture_seeding'],
            culture_type=kwargs['culture_type'],
            description=kwargs['description'],
            image=kwargs['image'],
            min_max_harvest_month=kwargs['min_max_harvest_month'],
            min_max_seed_month_inside=kwargs['min_max_seed_month_inside'],
            min_max_seed_month_outside=kwargs['min_max_seed_month_outside'],
            origin=kwargs['origin'],
            seeding_advice=kwargs['seeding_advice'],
            soil_nature=kwargs['soil_nature'],
            soil_quality=kwargs['soil_quality'],
            sun_expo=kwargs['sun_expo'],
            texture=kwargs['texture'],
            variety=kwargs['variety'],
            water_need=kwargs['water_need'],
            seed_date=kwargs['seed_date'],
            Kini_days=kwargs['Kini_days'],
            Kdev_days=kwargs['Kdev_days'],
            Kmid_days=kwargs['Kmid_days'],
            Kend_days=kwargs['Kend_days'],
            Kini=kwargs['Kini'],
            Kmid=kwargs['Kmid'],
            Kend=kwargs['Kend'])




class ParcelModel(models.Model):
    #id_garden = models.ForeignKey(GardenModel, on_delete=models.CASCADE, null=True)
    num_channel = models.IntegerField()
    id_vegetable = models.ForeignKey(VegetableModel, on_delete=models.CASCADE, null=True)
    number_of_plant = models.IntegerField()
    class Meta:
        db_table = 'ParcelModel'
class GardenModel(models.Model):
    garden_id = models.AutoField(primary_key=True)
    garden_name = models.CharField(max_length=255)
    garden_postalcode = models.IntegerField(default=0)
    garden_coord_lat = models.FloatField(default=0.0)
    garden_coord_lng = models.FloatField(default=0.0)
    parcels= models.ManyToManyField(ParcelModel)
    def __str__(self):
        return self.garden_name
    class Meta:
        db_table = 'GardenModel'
class WeatherModel(models.Model):
    id_weather = models.AutoField(primary_key=True)
    id_garden = models.ManyToManyField(GardenModel)
    sunrise_hr = models.TimeField()
    sunset_hr = models.TimeField()
    temperature = models.FloatField()
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    wind_force = models.FloatField()
    wind_dir = models.FloatField()
    cloudiness = models.IntegerField()
    description = models.CharField(max_length=50)
    icon = models.CharField(max_length=10)
    surface_temperature = models.FloatField()
    surface_temperature_at_10cm = models.FloatField()
    soil_moisture = models.FloatField()
    precipitation_mm = models.FloatField()
    precipitation_risk = models.FloatField()
    dew_point = models.FloatField()
    class Meta:
        db_table = 'WeatherModel'
class UserProfileModel(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    #  ca plante -> gardens = models.ForeignKey(GardenModel, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20,null=True,verbose_name="Pseudo :")
    bio = models.TextField(max_length=500, null=True,verbose_name="Votre biographie :)")
    #email = models.EmailField()
    #location = models.CharField(max_length=30, null=True,verbose_name="Localisation de vos parcelles")
    #birth_date = models.DateField(null=True, blank=True,verbose_name="Votre ")
    avatar = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'UserProfile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfileModel.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
         print("get or create user profile")
         # instance.save()


class IrrigaiaStatistic(models.Model):
    id_stat=models.AutoField(primary_key=True)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    water_last_hour = models.FloatField(default=0)
    water_last_24hour = models.FloatField(default=0)
    water_last_week = models.FloatField(default=0)
    water_last_month = models.FloatField(default=0)
    class Meta:
        db_table = 'IrrigaiaStatistic'



class IrrigaiaDiary(models.Model):
    id_diary = models.AutoField(primary_key=True)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    channel = models.IntegerField() #@todo : limit to num of channel max https://stackoverflow.com/questions/41153114/django-limit-the-number-of-instances-of-a-model-for-every-user
    status = models.BooleanField() #OnOFF
    datetime = models.DateTimeField()
    liters = models.FloatField(default=0.0)
    alarm  = models.CharField(max_length=255)
    api_temperature = models.FloatField(default=0.0)
    measured_temp = models.FloatField(default=0.0)
    measured_press = models.FloatField(default=0.0)
    measured_soil_humidity = models.FloatField(default=0.0)
    measured_soil_fertility=models.FloatField(default=0.0)
    measured_luminosity = models.FloatField(default=0.0)
    measured_battery_level = models.FloatField(default=0.0)
    class Meta:
        db_table = 'IrrigaiaDiary'



class IrrigaiaDeviceModel(models.Model):
    device_id=models.CharField(max_length=255,primary_key=True)
    id_user = models.OneToOneField(User,on_delete=models.CASCADE)
    device_name=models.CharField(default="irrigaia",max_length=64)
    garden = models.OneToOneField(GardenModel,on_delete=models.CASCADE)
    #device_stats = models.OneToOneField(IrrigaiaStatistic, on_delete=models.CASCADE,null=True)
    #device_diary = models.OneToOneField(IrrigaiaDiary,on_delete=models.CASCADE,null=True)
    device_current_alarm = models.CharField(max_length=255) # alarm DDMMYY-HHMM- battery low
    device_uptime= models.IntegerField(default=0)
    device_version = models.CharField(max_length=255)
    device_last_time_seen = models.DateTimeField()
    device_settings_wifi_passwd=models.CharField(max_length=12)
    device_settings_wifi_ap = models.CharField(max_length=12)
    device_settings_nb_Of_Channels=models.IntegerField(default=0) #@todo : limit to num of channel max https://stackoverflow.com/questions/41153114/django-limit-the-number-of-instances-of-a-model-for-every-user
    def __str__(self):
        return self.device_id

    @classmethod
    def create(self,cls, username,device_id):
        irrigaia_device = cls(device_id=device_id)
        #rquser = request.user
        user = User.objects.get(username__iexact=username)
        irrigaia_device.id_user=user

        # do something with the book
        return irrigaia_device
    class Meta:
        db_table = 'IrrigaiaDevice'
