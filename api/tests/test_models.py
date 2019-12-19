from django.test import TestCase
from api.models import VegetableModel,GrowModel
from datetime import datetime,timedelta
# Create your tests here.
class VegetableTestCase(TestCase):
    """Test module for Vegetable model """

    def setUp(self):
        VegetableModel.objects.create(name='vegeta')
        VegetableModel.objects.create(name='kakarot')

    def testCreation(self):
        vegetable_songoku = VegetableModel.objects.get(name='kakarot')
        vegetable_vegeta = VegetableModel.objects.get(name='vegeta')
        self.assertEqual(str(vegetable_songoku), 'kakarot')
        self.assertEqual(str(vegetable_vegeta), 'vegeta')

class GrowModelTestCase(TestCase):
    def setUp(self):
        grow_model_root = GrowModel.objects.create(vegfamilyname="root",Kini_days=10,Kdev_days=10,Kmid_days=10,Klate_days=10,Kini=0.1,Kmid=0.3,Kend=0.1,seed_date="2019-05-17")

        VegetableModel.objects.create(name='vegeta', id_growmodel=grow_model_root.id_growmodel)
        VegetableModel.objects.create(name='kakarot',id_growmodel=grow_model_root.id_growmodel)

    def testget_Kc(self):
        # tester Kini en fonction date de seeding
        vegetable_songoku = VegetableModel.objects.get(name='kakarot')
        vegetable_vegeta = VegetableModel.objects.get(name='vegeta')
        grow_model_root = GrowModel.objects.get(vegfamilyname="root", Kini_days=10, Kdev_days=10, Kmid_days=10,
                                                Klate_days=10, Kini=0.1, Kmid=0.3, Kend=0.1, seed_date="2019-05-17")



        date_format = "%Y-%m-%d"
        date = datetime.strptime('2019-05-17', date_format).date()

        self.assertEqual(grow_model_root.get_Kc(5), grow_model_root.Kini)
        self.assertEqual(grow_model_root.get_Kc(10), grow_model_root.Kini)
        self.assertAlmostEqual(grow_model_root.get_Kc(15), (grow_model_root.Kini + grow_model_root.Kmid)/2)

        self.assertAlmostEqual(grow_model_root.get_Kc(20), grow_model_root.Kmid)
        self.assertAlmostEqual(grow_model_root.get_Kc(35), (grow_model_root.Kmid+grow_model_root.Kend)/2)
        self.assertEqual(grow_model_root.get_Kc(50), grow_model_root.Kend)

    def testget_Status(self):
        # tester Kini en fonction date de seeding
        vegetable_songoku = VegetableModel.objects.get(name='kakarot')
        vegetable_vegeta = VegetableModel.objects.get(name='vegeta')
        grow_model_root = GrowModel.objects.get(vegfamilyname="root", Kini_days=10, Kdev_days=10, Kmid_days=10,
                                                Klate_days=10, Kini=0.1, Kmid=0.3, Kend=0.1, seed_date="2019-05-17")

        date_format = "%Y-%m-%d"
        date = datetime.strptime('2019-05-17', date_format).date()
        grow_model_root.get_Status(date=date)

        self.assertEqual(grow_model_root.get_Status(date + timedelta(days=5)), "germination/growth/initial stage")
        self.assertEqual(grow_model_root.get_Status(date + timedelta(days=12)), "dev stage")
        self.assertEqual(grow_model_root.get_Status(date + timedelta(days=25)), "mid stage")
        self.assertEqual(grow_model_root.get_Status(date + timedelta(days=32)), "late stage")
        self.assertEqual(grow_model_root.get_Status(date + timedelta(days=50)), "end stage")