#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);


/**
 * print_python_bytes - Displays fundamental information about Python byte objects.
 * @p: a bytes object PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t the_size, x;
	PyBytesObject *the_bytes = (PyBytesObject *)p;
	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		the_size = 10;
	else
		the_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", the_size);
	for (x = 0; x < the_size; x++)
	{
		printf("%02hhx", the_bytes->ob_sval[x]);
		if (x == (the_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}


/**
 * print_python_float - Displays fundamental information about Python float objects.
 * @p: a float object PyObject.
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;
	PyFloatObject *obj_float = (PyFloatObject *)p;
	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(obj_float->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}

/**
 * print_python_list - Displays fundamental information about Python list
 * @p: a list object PyObject
 */
void print_python_list(PyObject *p)
{
    const char *type;
	Py_ssize_t the_size, allocation, x;
	PyListObject *the_list = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;
	the_size = variable->ob_size;
	allocation = the_list->allocated;
	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocation);

	for (x = 0; x < the_size; x++)
	{
		type = the_list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", x, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[x]);
		else if (strcmp(type, "float") == 0)
			print_python_float(the_list->ob_item[x]);
	}
}
