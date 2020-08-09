from model_market.models import Task, Framework


def categories(request):
    task_list = Task.objects.all()
    framework_list = Framework.objects.all()
    return {"framework_list": framework_list, "task_list": task_list}