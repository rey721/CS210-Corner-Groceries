import re
import string
import os.path
from os import path

    def CountAll() :
    text = open('CS210_Project_Three_Input_File.txt', 'r') 
    dictionary = dict() 
    for line in text :
line = line.strip() 
word = line.lower() 
if word in dictionary :
dictionary[word] = dictionary[word] + 1 
else:
dictionary[word] = 1 
for key in list(dictionary.keys()) :
    print(key.capitalize(), ":", dictionary[key])
    text.close() 
   
def CountInstances(searchTerm) :
    searchTerm = searchTerm.lower()
    text = open('CS210_Project_Three_Input_File.txt', 'r')
    wordCount = 0
    for line in text :
line = line.strip()
word = line.lower()
if word == searchTerm :
wordCount += 1
return wordCount
text.close()
def CollectData() :
    text = open('CS210_Project_Three_Input_File.txt', 'r+')
    frequency = open('frequency.dat', 'w+')
    dictionary = dict()
    for line in text :
line = line.strip()
word = line.lower()
if word in dictionary :
dictionary[word] = dictionary[word] + 1
else :
    dictionary[word] = 1
    for key in list(dictionary.keys()) : 
        frequency.write(str(key.capitalize()) + " " + str(dictionary[key]) + "\n")
        text.close()
        frequency.close()
        int callIntFunc(string proc, string param)
    {
        char* procname = new char[proc.length() + 1];
        std::strcpy(procname, proc.c_str());
        char* paramval = new char[param.length() + 1];
        std::strcpy(paramval, param.c_str());
        cout << "Enter a number." << endl;
        cin >> param;
        PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
        // Initialize the Python Interpreter
        Py_Initialize();
        // Build the name object
        pName = PyUnicode_FromString((char*)("CS210_Starter_PY_Code"));
        // Load the module object
        pModule = PyImport_Import(pName);
        // pDict is a borrowed reference 
        pDict = PyModule_GetDict(pModule);
        // pFunc is also a borrowed reference 
        pFunc = PyDict_GetItemString(pDict, procname);
        if (PyCallable_Check(pFunc))
        {
            pValue = Py_BuildValue("(z)", paramval);
            PyErr_Print();
            presult = PyObject_CallObject(pFunc, pValue);
            PyErr_Print();
        }
        else
        {
            PyErr_Print();
        }
        //printf("Result is %d\n", _PyLong_AsInt(presult));
        Py_DECREF(pValue);
        // Clean up
        Py_DECREF(pModule);
        Py_DECREF(pName);
        // Finish the Python Interpreter
        Py_Finalize();
        // clean 
        delete[] procname;
        delete[] paramval;
        return _PyLong_AsInt(presult);
    }
def get_frequency_of_single_item(item_name) :
amount of times a specific item appears
filename = "frequency.dat"
f = open(filename, "r") 
data = f.read() 
list_of_items = data.split() 
frequency = {}
for item in list_of_items :
frequency[item] = frequency.get(item, 0) + 1
if item_name in frequency : 
return frequency[item_name]
