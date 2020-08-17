from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=UserProfile)
def my_handler(sender=UserProfile, **kwargs):
    """
    将用户存入的明文密码改成密文。
    当UserProfile save()之后 会发送一个post_save信号，接受信号之后改写密码
    """
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    # created 只有当第一次创建的时候为True，修改密码后为update操作created=False
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()


