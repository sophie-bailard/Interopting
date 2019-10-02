#include "stdafx.h"
#include <Windows.h>

#include "awesome_module.h"

// This code makes us always use the release version of Python
// even when in debug mode of this program.
// https://pytools.codeplex.com/discussions/547562
#define HAVE_ROUND
#ifdef _DEBUG
#define RESTORE_DEBUG
#undef _DEBUG
#endif
#include <Python.h>
#ifdef RESTORE_DEBUG
#define _DEBUG
#undef RESTORE_DEBUG
#endif

static PyObject* AwesomeError;

PyMethodDef awesome_methods[] =
{
	{ NULL, NULL, 0, NULL } /* Sentinel */
};

static struct PyModuleDef awesome_module =
{
	PyModuleDef_HEAD_INIT,
	"awesome",               /* Module Name */
	NULL,                    /* Module Documentation (may be NULL) */
	-1,
	awesome_methods
};

PyObject* PyInit_awesome(void)
{
	PyObject* m;
	m = PyModule_Create(&awesome_module);

	if (m == NULL)
		return NULL;

	// Add the "awesome" exception.
	AwesomeError = PyErr_NewException("awesome.error", NULL, NULL);
	Py_INCREF(AwesomeError);
	PyModule_AddObject(m, "error", AwesomeError);

	PyModule_AddStringConstant(m, "best_actor", "Sylvester Stalone");
	PyModule_AddStringConstant(m, "best_movie", "A Bug's Life");

	return m;
}