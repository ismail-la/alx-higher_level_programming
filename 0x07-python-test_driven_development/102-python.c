#include "Python.h"

/**
 * print_python_string - Prints info about Python strings
 * @p: PyObject string object.
 */

void print_python_string(PyObject *p)
{
	long int the_Length;

	fflush(stdout);

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
		printf("  [ERROR] Invalid String Object\n");
		return;
	the_Length = ((PyASCIIObject *)(p))->the_Length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", the_Length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &the_Length));
}
