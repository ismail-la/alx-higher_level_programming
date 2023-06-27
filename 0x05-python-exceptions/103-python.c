
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_float - Displays fundamental information
 * about Python float objects 
 * @p: a float object PyObject.
 */
void print_python_float(PyObject *p)
{
    char *str = NULL;
	double VAL = 0;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	VAL = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(VAL, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - Displays fundamental information
 * about Python byte objects.
 * @p: a bytes object PyObject
 */
void print_python_bytes(PyObject *p)
{
	char *str = NULL;
    Py_ssize_t Sizee = 0, i = 0;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Sizee = PyBytes_Size(p);
	printf("  size: %zd\n", Sizee);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", Sizee < 10 ? Sizee + 1 : 10);
	while (i < Sizee + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - Displays fundamental information about Python list
 * @p: a list object PyObject
 */
void print_python_list(PyObject *p)
{
	PyObject *Elemm;
    Py_ssize_t Sizee = 0;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		Sizee = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", Sizee);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < Sizee)
		{
			Elemm = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, Elemm->ob_type->tp_name);
			if (PyBytes_Check(Elemm))
				print_python_bytes(Elemm);
			else if (PyFloat_Check(Elemm))
				print_python_float(Elemm);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
