from django.contrib import admin
from . import models as m 


admin.site.register(m.Cart)
admin.site.register(m.Project)
admin.site.register(m.ProjectMember)
admin.site.register(m.Task)
