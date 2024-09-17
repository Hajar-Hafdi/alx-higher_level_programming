#include <Python.h>

/**
 * print_python_list_info - outputs basic info abt Py lists
 *
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int sz, allocate, u;
	PyObject *jct;

	sz = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (u = 0; u < sz; u++)
	{
		printf("Element %d: ", u);
		jct = PyList_GetItem(p, u);
		printf("%s\n", Py_TYPE(jct)->tp_name);
	}
}
