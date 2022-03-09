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
        size_t inputLen = strlen(input);
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
    } else if (strcmp(platform, "win") == 0) {
    } else {
        printf("Unknown platform\n");
    }

    
}

// ImportError: dynamic module does not define init function (initkeyboard)

