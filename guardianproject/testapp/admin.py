from django.contrib import admin
from .models import EMP
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user, assign_perm
@admin.register(EMP)
class EMPAdmin(GuardedModelAdmin):
    list_display = ('name',)

    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objects(request).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        data = request.get_model_objects(request)
        return data

    def get_model_objects(self, request, action=None, klass=None):
        opts = self.opts
        actions = [action] if action else ['view', 'edit', 'delete']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in actions], klass=klass,
                                    any_perm=True)

    def has_permission(self, request,obj,action):
        opts = self.opts
        code_name = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}',obj)
        else:
            return True




    def has_change_permission(self, request, obj=None):
        return self.has_permission(request,obj,'change')

    def has_view_permission(self, request, obj=None):
        return self.has_permission(request,obj,'view')

    def has_delete_permission(self, request, obj=None):
        return self.has_permission(request,obj,'delete')

