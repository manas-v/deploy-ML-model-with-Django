from django.http.response import HttpResponse
from django.shortcuts import render
import pickle
import os
import numpy as np
import json

# Create your views here.
cwd = os.getcwd()
file_path = os.path.join(cwd, 'templates\model.pkl')
loaded_model = pickle.load(open(file_path, 'rb'))

def predict(request):

    buying = request.POST['buying']
    maint = request.POST['maint']
    doors = request.POST['doors']
    persons = request.POST['persons']
    lug_boot = request.POST['lug_boot']
    safety = request.POST['safety']

    buying_dict = {'high':0, 'low':1, 'med':2, 'vhigh':3}
    maint_dict = {'high':4, 'low':5, 'med':6, 'vhigh':7}
    doors_dict = {'2':8, '3':9, '4':10, '5more':11}
    persons_dict = {'2':12, '4':13, 'more':14}
    lug_dict = {'big':15, 'med':16, 'small':17}
    safety_dict = {'high':18, 'low':19, 'med':20}    

    data = [0]*21
    data[buying_dict[buying]] = 1
    data[maint_dict[maint]] = 1
    data[doors_dict[doors]] = 1
    data[persons_dict[persons]] = 1
    data[lug_dict[lug_boot]] = 1
    data[safety_dict[safety]] = 1

    df = np.array(data)
    df = df.reshape(1,-1)

    print(df)

    predictions = loaded_model.predict(df)
    class_dict = {'unacc':'Unacceptable', 'acc':'Acceptable', 'vgood':'Very good', 'good':'Good'}
    output = class_dict[str(predictions[0])]
    print(output)
    msg = {'response': 'OK', 'class': output}
    return HttpResponse(json.dumps(msg), content_type='application/json')

def index(request):
    return render(request, 'index.html')