#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints python bytes information
 * @p: pointer Python Object
 * Return: nothing
 *
 */
void print_python_bytes(PyObject *p)
{
	long int size, x, limit;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	
	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;
	printf("  first %ld bytes:", limit);

	for (x = 0; x < limit; x++)
		if (string[x] >= 0)
			printf(" %02x", string[x]);
		else
			printf(" %02x", 256 + string[x]);
	printf("\n");
}

/**
 * print_python_list - Prints python list information
 *
 * @p: pointer Python Object
 * Return: nothing
 *
 */

void print_python_list(PyObject *p)
{
	PyObject *Obj;
	long int size, x;
	PyListObjt *list;
	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (x = 0; x < size; x++)
		Obj = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((Obj)->ob_type)->tp_name);
		if (PyBytes_Check(Obj))
			print_python_bytes(Obj);
}
