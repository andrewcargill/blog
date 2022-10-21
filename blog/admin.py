from django.contrib import admin

#this imports the post table into admin


from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# our blog content (which we know is a text field - we 
# want to use summernote for this)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_field = ('content')

#before summer note the code was:

# admin.site.register(Post)

