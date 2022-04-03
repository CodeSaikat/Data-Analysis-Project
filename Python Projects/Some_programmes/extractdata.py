import requests
import pickle
r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
txt=r.text
py_dict=txt.split() # This is a list type class.
print(py_dict)
# This programe makes pickling a data which are contain in list.
myfile = open('mohit.pkl','wb')
pickle.dump(py_dict,myfile)
myfile.close()
"""
#This is unpickling the file from the pickle file.
myfile = open('mohit.pkl','rb')
py_dict = pickle.load(myfile)
myfile.close()
print(py_dict)
"""