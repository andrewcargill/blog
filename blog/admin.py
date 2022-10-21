from django.contrib import admin

#this imports the post table into admin


from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin

# our blog content (which we know is a text field - we 
# want to use summernote for this)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_field = ('content')

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        


#before summer note the code was:

# admin.site.register(Post)

