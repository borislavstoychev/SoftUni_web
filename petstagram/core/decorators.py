from django.shortcuts import redirect


def can_like(model_class):

    def decorator(view_func):
        def wrapper(request, pk, *args, **kwargs):
            model_obj = model_class.objects.get(pk=pk)

            if model_obj.user.id != request.user.id:
                return view_func(request, pk, *args, **kwargs)
            return redirect('sign in user')

        return wrapper

    return decorator


def can_delete_or_edit(model_class):

    def decorator(view_func):
        def wrapper(request, pk, *args, **kwargs):
            model_obj = model_class.objects.get(pk=pk)

            if model_obj.user.id == request.user.id:
                return view_func(request, pk, *args, **kwargs)
            return redirect('sign in user')

        return wrapper

    return decorator
