from django.db import models

# Create your models here.

#django数据库参数设置学习资料：https://blog.csdn.net/u013677491/article/details/95974941

#这里直接使用了数据的CSV表格处理后的CSV文件作为查询对应电影的数据
#电影的详细信息、照片通过调取IMDB数据库API进行数据获取


class User(models.Model):
    userId = models.IntegerField(blank=False, primary_key=True, unique=True)
    accont = models.IntegerField(blank=False, unique=True)
    nickname = models.TextField(blank=False)
    phone = models.IntegerField(blank=False)
    password = models.IntegerField(blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return "{}".format(self.userId)


class RatingList(models.Model):
    userId = models.IntegerField(blank=False)
    movieId = models.IntegerField(blank=False)
    rating = models.FloatField(blank=False)
    content = models.TextField(blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    def __str__(self):
        return "{} {}".format(self.userId, self.movieId)


class MovieCllecReady(models.Model):
    userId = models.IntegerField(blank=False)
    movieId = models.IntegerField(blank=False)
    is_collect = models.BooleanField(blank=False)
    is_towatch = models.BooleanField(blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return "{} {}".format(self.userId, self.movieId)


class MovieTop(models.Model):
    movieId = models.IntegerField(blank=False, primary_key=True)
    avg_rating = models.FloatField(blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return "{}".format(self.userImovieId)
#电影数据表 直接调去API使用 电影数据表：movieId，title，movie_image，movie_content，move_rating
#暂时使用，后续要外接数据库


class MovieURL(models.Model):
    movieId = models.IntegerField(blank=False, primary_key=True)
    tmdbId = models.IntegerField(blank=False)
    movie_url = models.TextField(blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return "{}".format(self.movie_url)
