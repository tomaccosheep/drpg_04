# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from .models import Play_Project
import json
import os
import subprocess
import fileinput
from django.utils.crypto import get_random_string
from proxy.views import proxy_view
from django.views.decorators.csrf import csrf_exempt

# Path settings
# {{
dir_path = "/app"
script_string = dir_path + "/scripts"
bash_make_cont = "/bin/bash {script_string}/make_cont.sh {project_id}"
bash_stop_cont = "/bin/bash {script_string}/stop_cont.sh {project_id}"

my_env = os.environ.copy()
my_env["DJANGO_SETTINGS_MODULE"] = "user_project.settings"
# }}

def hello(request):
    return render(request, 'make_dj/hello.html')

def index(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    context_dict = {'con_001': proj.con_001,
                    'id': proj.id,
                    'project_id': project_id,
                    }
    return render(request, 'make_dj/index.html', context=context_dict)

def new_project(request):
    # This creates a new project and gives it a unique id based on the
    # get_random_string function, which will be in the url
    # {{
    proj = Play_Project()
    def_id = get_random_string(length=32)
    proj.unique_id = def_id.lower()
    proj.save()
    # }}
    return HttpResponseRedirect('/index/{}/'.format(def_id.lower()))

@csrf_exempt
def save(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    saved = False
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        proj.con_001 = json_data['con_001']
        proj.save()
        saved = True
    return JsonResponse({'saved': saved})

@csrf_exempt
def make(request, project_id):

    proj = Play_Project.objects.get(unique_id=project_id)

    # This writes our database configuration into a python file in /configs/
    # {{
    filename = "/app/configs/" + project_id + ".json"
    file = open(filename, "w")
    file.truncate()
    conf_dict = {"sty_con_001" : proj.con_001 }
    json.dump(conf_dict, file)
    file.close()
    # }}
    return JsonResponse({'ran': True})


@csrf_exempt
def run(request, project_id):
    # This runs the script in /scripts/ to put up a docker container
    # {{
    subprocess.run(bash_make_cont.format(script_string=script_string,project_id=project_id).split(), env=my_env)
    # }}
    return JsonResponse({'ran': True})


@csrf_exempt
def view(request, project_id):
    return proxy_view(request, "http://" + project_id)

@csrf_exempt
def kill(request, project_id):
    # This runs the script in /scripts/ that stops a container by project_id
    # {{
    subprocess.run(bash_stop_cont.format(script_string=script_string, project_id=project_id).split(), env=my_env)
    # }}
    return JsonResponse({'killed': True})
 
