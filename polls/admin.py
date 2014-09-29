from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # rearranged the order displayed
    # customize the fieldset listed when admining a question
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
#        ('Date information',    {'fields': ['pub_date']}),
        # add 'collapse' HTML class builtin via Django
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # add choices inline when admining a question
    inlines = [ChoiceInline]
    
    # change the Question display in the admin panel to show more detail before
    # clicking the Question to edit
    list_display = ('question_text','pub_date', 'was_published_recently')
    # add a filter to the Question admin page
    list_filter = ['pub_date']
    # add search capability
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text','question','votes')
    search_fields = ['choice_text']
    list_filter = ['votes']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
