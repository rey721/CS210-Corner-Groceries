#include <Python.h>
#include <iostream>
#include <Windows.h>
#include <cmath>
#include <string>

using namespace std;

void CallProcedure(string pName)
{
	char* procname = new char[pName.length() + 1];
	std::strcpy(procname, pName.c_str());

	if (procname)
	{
	

	Py_Initialize();
	PyObject* my_module = PyImport_ImportModule("CS210_Starter_PY_Code");
	PyErr_Print();
	PyObject* my_function = PyObject_GetAttrString(my_module, procname);
	PyObject* my_result = PyObject_CallObject(my_function, NULL);
	Py_Finalize();
}
	delete[] procname;
}

int callIntFunc(string proc, string param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	char* paramval = new char[param.length() + 1];
	std::strcpy(paramval, param.c_str());


	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	
	Py_Initialize();	
	pName = PyUnicode_FromString((char*)"PythonCode");	
	pModule = PyImport_Import(pName);	
	pDict = PyModule_GetDict(pModule);	
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
	printf("Result is %d\n", _PyLong_AsInt(presult));
	Py_DECREF(pValue);	
	Py_DECREF(pModule);
	Py_DECREF(pName);
	
	Py_Finalize();

	 
	delete[] procname;
	delete[] paramval;


	return _PyLong_AsInt(presult);
}

int callIntFunc(string proc, int param)
{
	char* procname = new char[proc.length() + 1];
	std::strcpy(procname, proc.c_str());

	PyObject* pName, * pModule, * pDict, * pFunc, * pValue = nullptr, * presult = nullptr;
	
	Py_Initialize();	
	pName = PyUnicode_FromString((char*)"PythonCode");	
	pModule = PyImport_Import(pName);	
	pDict = PyModule_GetDict(pModule); 
	pFunc = PyDict_GetItemString(pDict, procname);
	if (PyCallable_Check(pFunc))
	{
		pValue = Py_BuildValue("(i)", param);
		PyErr_Print();
		presult = PyObject_CallObject(pFunc, pValue);
		PyErr_Print();
	}
	else
	{
		PyErr_Print();

		printf("Result is %d\n", _PyLong_AsInt(presult));
		Py_DECREF(pValue);	
		Py_DECREF(pModule);
		Py_DECREF(pName);
		
		Py_Finalize();
	}
	
	delete[] procname;

	return _PyLong_AsInt(presult);
}


int main()
{
	CallProcedure("printsomething");
	cout << callIntFunc("PrintMe", "House") << endl;
	cout << callIntFunc("SquareValue", 2);

}