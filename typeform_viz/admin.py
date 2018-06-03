from django.contrib import admin
from typeform_viz.models import JHAPP


# Add your models here
class JHAPPAdmin(admin.ModelAdmin):
    search_fields = (
        'nationality', 'coming_from', 'first_name', 'last_name')
    list_filter = (
        'nationality', 'coming_from', '_18yo', 'needs_reimbursement',
        'dietary_requirements',
        'needs_visa', 'accepted', 'sentmail', 'first_hackathon', 'university',
        'degree')
    model = JHAPP


admin.site.register(JHAPP, JHAPPAdmin)
