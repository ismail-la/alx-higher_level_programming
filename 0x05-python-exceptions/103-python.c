/*
 * File: 103-python.c
 * Auth: Lahbari ismail
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - for Prints basic info about Python lists
 * @p: the PyObject list object
 *
 */
void print_python_list(PyObject *p)
{
	const char *type;
	Py_ssize_t size, alloc;
	int i = 0;

	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", alloc);

	while (i < size)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
		i++;
	}
}

/**
 * print_python_bytes - for Prints basic info about Python byte objects
 * @p: PyObject byte object
 *
 */
void print_python_bytes(PyObject *p)
{
	char *string = NULL;
	Py_ssize_t size = 0, i = 0;

	fflush(stdout);

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);

	printf("  size: %zd\n", size);

	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));

	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}

	printf("\n");

}

/**
 * print_python_float - for Prints the basic info about Python float objects
 * @p: PyObject float object
 *
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);

	PyMem_Free(buff);
}
