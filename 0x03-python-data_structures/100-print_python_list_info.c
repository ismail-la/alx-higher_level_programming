#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - function prints some basic info about
* pytohn list
* @p: the python object
*
**/

void print_python_list_info(PyObject *p)
{
	PyListObject *Listobj = (PyListObject *)p;
	long int size = PyList_Size(p);
        int i = 0;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", Listobj->allocated);
	while (i < size)
	{
	printf("Element %i: %s\n", i, Py_TYPE(Listobj->ob_item[i])->tp_name);
	i++;
	}
}
