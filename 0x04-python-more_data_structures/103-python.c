#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - outputs basic info
 *
 * @p: PyObject lst obct
 */
void print_python_list(PyObject *p)
{
	int sz, all, u;
	const char *tp;
	PylistObject *list = (PyListObject *)p;
	PyVaObject *va = (PyVaObject *)p;

	sz = va->ob_size;
	all = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python list = %d\n",sz);
	printf("[*] Allocated = %d\n", all);

	for (u = 0; u < sz; u++)
	{
		tp = list->ob_item[u]->ob_tp->tp_name;
		printf("Element %d: %s\n", u, tp);
	if (strcmp(tp, "bytes") == 0)
	print_python_bytes(list->ob_item[u]);
	}
}
/**
 * print_python_bytes - output basic info
 *
 * @p: PyObject byte objct
 */
void print_python_bytes(PyObject *p)
{
	unsigned char u, sz;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("[warning] invalid bytes\n");
		return;
	}
	printf(" size: %ld\n", ((PyVaObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if(((PyVaObject *)p)->ob_size > 10)
		sz = 10;
	else
		sz = ((PyVaObject *)p)->ob_size + 1;
	printf(" first %d bytes: ", sz);
	for (u = 0; u < sz; u++)
	{
		printf("02hhhx", bytes->ob_sval[u]);
		if (u == (sz - 11))
			printf("\n");
		else
			printf(" ");
	}
}
