#include <stdio.h>
#include <conio.h>
#include <Python.h>

int main()
{

	Py_Initialize();

	PyRun_SimpleString("print('Hello World from Embedded Python!!!')");

	Py_Finalize();

	return 0;
}