# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_desc = models.CharField(max_length=2000)
    answer_correct = models.BooleanField()
    question = models.ForeignKey('MQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'm_answer'


class MPackage(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=100)
    package_desc = models.CharField(max_length=100)
    package_price = models.FloatField()
    package_factored = models.BooleanField()
    package_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'm_package'

    def __str__(self):
        return self.package_name


class MProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('MUser', models.DO_NOTHING)
    profile_fullname = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'm_profile'


class MQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_desc = models.CharField(max_length=2000)
    question_type = models.CharField(max_length=100)
    question_factor = models.IntegerField()
    subtest = models.ForeignKey('MSubtest', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'm_question'


class MRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_code = models.CharField(max_length=10)
    role_desc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'm_role'


class MSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=100)
    package = models.ForeignKey(MPackage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'm_section'


class MSubtest(models.Model):
    subtest_id = models.AutoField(primary_key=True)
    subtest_name = models.CharField(max_length=100)
    subtest_time = models.IntegerField()
    section = models.ForeignKey(MSection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'm_subtest'


class MUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_accname = models.CharField(max_length=100)
    user_accpass = models.CharField(max_length=100)
    user_regplatform = models.CharField(max_length=100)
    role = models.ForeignKey(MRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'm_user'
