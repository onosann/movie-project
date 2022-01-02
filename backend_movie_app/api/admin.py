from django.contrib import admin

from .models import User
from .models import RatingList
from .models import MovieCllecReady
from .models import MovieTop
from .models import MovieURL

admin.site.register(User)
admin.site.register(RatingList)
admin.site.register(MovieCllecReady)
admin.site.register(MovieTop)
admin.site.register(MovieURL)
