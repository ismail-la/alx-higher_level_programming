#include <stdio.h>
#include <Python.h>


/**
 * print_python_bytes - Prints python bytes information
 * @p: Python Object
 * Return: nothing
 *
 */

void print_python_bytes(PyObject *p)

{
printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

long int size = PyBytes_Size(p);
char *string = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);

long int limit = (size >= 10) ? 10 : size + 1;

printf("  first %ld bytes:", limit);

for (long int i = 0; i < limit; i++)
{
unsigned char byte = (unsigned char)string[i];
printf(" %02x", byte);
}

printf("\n");
}

/**
 * print_python_list - Prints python list information
 * @p: Python Object
 * Return: nothing
 *
 */

void print_python_list(PyObject *p)
{
long int size = PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
PyListObject *list = (PyListObject *)p;
long int allocated = list->allocated;
printf("[*] Allocated = %ld\n", allocated);
}
for (long int i = 0; i < size; i++)
{
PyObject *obj = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}
