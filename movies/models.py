from django.core.validators import MaxValueValidator as max_val, MinValueValidator as min_val
from django.db.models import (
	CASCADE, CharField, DateField, DurationField, FileField, ForeignKey, ImageField, JSONField,
	ManyToManyField, Model, SET_NULL, SlugField, SmallIntegerField, TextField
)
from django.utils.translation import gettext_lazy as _


class Movie(Model):
	title = CharField(
		_('title of movie'),
		max_length=50,
		help_text=_('title of movie')
	)
	slug = SlugField(max_length=100, unique=True)
	thumbnail = ImageField(_('thumbnail of image'), upload_to='movies/images/thumbnails')
	genres = ManyToManyField('movies.Genre')
	date = DateField(_('date of movie'))
	durability = DurationField(_('duration of film'))
	description = TextField(_('description of film'))
	age_rating = SmallIntegerField(_('age restriction'), validators=(min_val(0), max_val(60)))
	file = FileField(upload_to='movies/')
	qualities = JSONField('video file qualities')


class Genre(Model):
	title = CharField(max_length=50)
	slug = SlugField(max_length=100, unique=True)


class Trailer(Model):
	movie = ForeignKey(Movie, CASCADE)
	video = FileField(upload_to='movies/trailers/')
	extra = ImageField(upload_to='movies/images/extras')


class Rating(Model):
	movie = ForeignKey('movies.Movie', CASCADE, null=True)
	user = ForeignKey('users.User', SET_NULL, null=True)
	value = SmallIntegerField(validators=(min_val(1), max_val(5)))
