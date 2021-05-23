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

    buying_dict = {'vhigh':3, 'high':0, 'med':2, 'low':1}
    maint_dict = {'vhigh':3, 'high':0, 'med':2, 'low':1}
    doors_dict = {'2':0, '3':1, '4':2, '5more':3}
    persons_dict = {'2':0, '4':1, 'more':2}
    lug_dict = {'small':2, 'med':1, 'big':0}
    safety_dict = {'low':1, 'med':2, 'high':0}    

    data = [buying_dict[buying], maint_dict[maint], doors_dict[doors], persons_dict[persons], lug_dict[lug_boot], safety_dict[safety]]
    df = np.array(data)
    df = df.reshape(1,-1)

    predictions = loaded_model.predict(df)
    class_dict = {'2':'Unacceptable', '0':'Acceptable', '3':'Very good', '1':'Good'}
    output = class_dict[str(predictions[0])]
    print(output)
    msg = {'response': 'OK', 'class': output}
    print(msg)
    return HttpResponse(json.dumps(msg), content_type='application/json')

def index(request):
    return render(request, 'index.html')