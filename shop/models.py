from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
"""
git init
git add .
git commit -m "修改了index"
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


# 装修类型
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
        return self.name
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
    img = models.ImageField()
    description = models.CharField(max_length=300,default='宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。')

    class Meta:
        ordering = ('name',)
        verbose_name = 'cumpus'
        verbose_name_plural = 'cumpies'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:campus_list',
                       args=[self.id, self.slug])


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

#户型
class Layout(models.Model):
    bedroom_count = models.IntegerField(default=1)
    bashroom_count = models.IntegerField(default=1)
    livingroom_count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    def __str__(self):
        return '{}室{}厅{}卫'.format(str(self.bedroom_count),str(self.livingroom_count),str(self.bashroom_count))
# 行政区域
class Administrative_division(models.Model):
    name = models.CharField('行政区域', max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    def __str__(self):
        return self.name


# 城市
class City(models.Model):
    name = models.CharField('城市', max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:dashboard_for_city',
                       args=[self.slug])


class Product(models.Model):
    # 多对一
    category = models.ForeignKey(Category, related_name='products')
    # 装修质量
    apartment_layout = models.ForeignKey(ApartmentLayout, related_name='apartment')
    #户型
    layout = models.ForeignKey(Layout,related_name="huxing")
    # 设施 多对多
    device = models.ManyToManyField(Device, related_name='device')
    # city
    locate = models.ForeignKey(City, related_name='city_locate')
    # 校区
    campus = models.ManyToManyField(Campus, related_name='campus_locate')
    distance = models.CharField('与校区距离', max_length=200, db_index=True)
    locations = models.ForeignKey(Administrative_division, related_name='lactional')
    updown = models.ForeignKey(Updown, related_name='updown_locate')
    #发布账户
    author = models.ForeignKey(User,
                               related_name='product_posts')

    name = models.CharField('商品名', max_length=200, db_index=True)
    slug = models.SlugField('链接地址', max_length=200, db_index=True)
    image = models.ImageField('商品图像', upload_to='products/%Y/%m/%d', blank=True)
    orientations = models.CharField('房间朝向', max_length=20, default='朝南')
    height = models.IntegerField('房间层高', default=0)
    description = models.TextField('描述', blank=True)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)  # 小数位数
    stock = models.PositiveIntegerField('库存', )
    available = models.BooleanField('是否上架', default=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('发布时间', auto_now=True)
    tags = TaggableManager()#标签

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
