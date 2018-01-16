from django.contrib.auth.models import AbstractUser
from django.db import models

from common.base_model import BaseModel
from common.constant import Gender


class Group(BaseModel):
    name = models.CharField(verbose_name="分组/角色名", max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = "分组/角色表"
        db_table = "group"

    def __str__(self):
        return self.name


class Permission(BaseModel):
    name = models.CharField(verbose_name="权限名", max_length=100, unique=True)
    desc = models.CharField(verbose_name="权限描述", max_length=200)

    class Meta:
        verbose_name = verbose_name_plural = "权限表"
        db_table = "permission"

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):

    class Meta:
        verbose_name = verbose_name_plural = "用户信息"
        db_table = "user_profile"

    def __str__(self):
        return self.username


class UserGroup(BaseModel):
    user_id = models.PositiveIntegerField(verbose_name="用户id")
    group_id = models.PositiveIntegerField(verbose_name="分组/角色id")

    class Meta:
        verbose_name = verbose_name_plural = "用户分组/角色表"
        db_table = "user_group"
        unique_together = ("user_id", "group_id")

    def __str__(self):
        return "用户:" + str(self.user_id) + "， 分组：" + str(self.group_id)


class GroupPermission(BaseModel):
    group_id = models.PositiveIntegerField(verbose_name="分组id")
    permission_id = models.PositiveIntegerField(verbose_name="权限id")

    class Meta:
        verbose_name = verbose_name_plural = "分组/角色权限表"
        db_table = "group_permission"
        unique_together = ("group_id", "permission_id")

    def __str__(self):
        return "分组:" + str(self.group_id) + "， 权限：" + str(self.permission_id)


class UserPermission(BaseModel):
    user_id = models.PositiveIntegerField(verbose_name="用户id")
    permission_id = models.PositiveIntegerField(verbose_name="权限id")

    class Meta:
        verbose_name = verbose_name_plural = "用户权限表"
        db_table = "user_permission"
        unique_together = ("user_id", "permission_id")

    def __str__(self):
        return "用户:" + str(self.user_id) + "， 权限：" + str(self.permission_id)


class UserExtendInfo(BaseModel):
    """
    用户扩展表，创建一个用户的时候必须创建一个这个表一一对应
    """
    user_id = models.PositiveIntegerField(unique=True, verbose_name="用户id")

    nick_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="昵称")

    # 让前端自己设置一个默认值
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")

    gender = models.IntegerField(
        choices=((Gender.MALE.value, "男"), (Gender.FEMALE.value, "女"), (Gender.NONE.value, "未知")),
        default=Gender.NONE.value
    )

    desc = models.CharField(max_length=300, default="", null=True, blank=True, verbose_name="个人描述")

    address = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name="住址")

    mobile = models.CharField(max_length=11, default="", null=True, blank=True, verbose_name="电话")

    focus = models.IntegerField(default=0, verbose_name="关注人数")

    refocus = models.IntegerField(default=0, verbose_name="被关注人数")

    integral = models.IntegerField(default=0, verbose_name="积分")

    # 设置默认头像和上传头像的路径
    image = models.ImageField(
        upload_to="image/user",
        default="image/user/default.jpg",
        max_length=200,
        verbose_name="个人头像"
    )

    class Meta:
        verbose_name = verbose_name_plural = "用户信息扩展表"
        db_table = "user_info"

    def __str__(self):
        return self.nick_name
