#define PY_SSIZE_T_CLEAN
#include <python3.8/Python.h>
#include <stdio.h>
#define MAX_STRING_SIZE 100


static PyObject *
is_pressed(PyObject *self, PyObject *args)
{
    char *platform;
    if (!PyArg_ParseTuple(args, "s", &platform))
        return NULL;
    if (strcmp(platform, "unix") == 0) {
        char input[MAX_STRING_SIZE] = {0};
        fgets(input, sizeof(input), stdin);
        int inputLen = strlen(input);
        for (int i = 0; i < inputLen; i++) {
            if (input[i] == '\33') {
                if (input[i + 1] == 'A') {
                    return Py_BuildValue("s", "up");
                }
                if (input[i + 1] == 'B') {
                    return Py_BuildValue("s", "down");
                }
            }
            else if (input[i] == '\r') {
                return Py_BuildValue("s", "enter");
            }
            // check for space key wich has ascii code 32
            else if (input[i] == 32) {
                return Py_BuildValue("s", "space");
            }

        }
}}

static PyMethodDef is_pressedMethods[] = {
    {"is_pressed",  is_pressed, METH_VARARGS,
     "keyboard input."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};
static struct PyModuleDef is_pressedmodule = {
    PyModuleDef_HEAD_INIT,
    "is_pressed",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    is_pressedMethods
};

PyMODINIT_FUNC
PyInit_keyboard(void)
{
    return PyModule_Create(&is_pressedmodule);
}