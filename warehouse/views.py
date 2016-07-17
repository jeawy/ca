from django.shortcuts import render
import getpass
from django.contrib.auth.models import User,Group, Permission
from django.contrib import auth
import pdb
from django.utils import timezone
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import random
import string
from django.core import serializers
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import smtplib
from django.conf import settings
from django.db.models import Q
import re 
 
from django.db.models import Max, Min
 
def home( request): 
    content={}
    content['home_menu'] = True 
    
    return render(request, 'index.html', content)
     
