from django.db import models
from django.core.urlresolvers import reverse

"""
git init
git add .
git commit -m "单元测试-判断url正确性"
git remote add origin https://github.com/luoying1105/zhufang.git
git push -u origin master

"""


# 类型
class Category(models.Model):  # 种类
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# 户型
class ApartmentLayout(models.Model):
    name = models.CharField('装修质量', max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'layout'
        verbose_name_plural = 'Layouts'

    def __str__(self):
        return '{}小区{}'.format(self.name, self.address)
        # 3室2厅1卫 整租69㎡ 向南 高层/共16层 精装修 普通住宅


# 设备
class Device(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'device'
        verbose_name_plural = 'devices'

    def __str__(self):
        return self.name


# 校区
class Campus(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'cumpus'
        verbose_name_plural = 'cumpies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:campus_for_city',
                       args=[self.slug])


# 小区 路段
class Updown(models.Model):
    name = models.CharField('小区名称', max_length=200,
                            db_index=True)
    address = models.CharField('详细地址', max_length=300,
                               db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = ''
        verbose_name_plural = 'cities'

    def __str__(self):
        return '{}小区{}'.format(self.name, self.address)

    def get_absolute_url(self):
        return reverse('shop:dashboard_for_updown',
                       args=[self.id, self.slug])


# 行政区域
class Administrative_division(models.Model):
    name = models.CharField('行政区域', max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    updown = models.ForeignKey(Updown, related_name='updown_locate')

    def __str__(self):
        return '该住房位于 {}{}'.format(self.name, self.updown)


# 城市
class City(models.Model):
    name = models.CharField('城市', max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    # 校区
    campus = models.ManyToManyField(Campus, related_name='campus_locate')
    distance = models.CharField('与校区距离', max_length=200, db_index=True)
    locations = models.ForeignKey(Administrative_division, related_name='lactional')

    class Meta:
        ordering = ('name',)
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return '该住房位于 {}{}附近学校为{}'.format(self.name, self.locations, self.campus)

    def get_absolute_url(self):
        return reverse('shop:dashboard_for_city',
                       args=[self.slug])


class Product(models.Model):
    # 多对一
    category = models.ForeignKey(Category, related_name='products')
    # 户型
    apartment_layout = models.ManyToManyField(ApartmentLayout, related_name='apartment')
    # 设施 多对多
    device = models.ManyToManyField(Device, related_name='device')
    # city
    locate = models.ForeignKey(City, related_name='city_locate')

    name = models.CharField('商品名', max_length=200, db_index=True)
    slug = models.SlugField('链接地址', max_length=200, db_index=True)
    image = models.ImageField('商品图像', upload_to='products/%Y/%m/%d', blank=True)
    bedroom = models.IntegerField('卧室数量')
    living_room = models.IntegerField('卧室数量', default=0)
    tolet = models.IntegerField('卫生间数量', default=1)
    orientations = models.CharField('房间朝向', max_length=20, default='朝南')
    height = models.IntegerField('房间层高', default=0)
    description = models.TextField('描述', blank=True)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)  # 小数位数
    stock = models.PositiveIntegerField('库存', )
    available = models.BooleanField('是否上架', default=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('发布时间', auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
