#ifndef AWESOME_MODULE_H_
#define AWESOME_MODULE_H_

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

#ifdef __cplusplus
extern "C" {
#endif

	extern PyObject* PyInit_awesome(void);

#ifdef __cplusplus
}
#endif

#endif