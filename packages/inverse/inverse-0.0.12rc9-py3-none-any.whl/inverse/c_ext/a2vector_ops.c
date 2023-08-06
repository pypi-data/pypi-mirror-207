#include <Python.h>


static PyObject *vector_ops_multiply(PyObject *self, PyObject *args) {

    PyObject *vec;

    double factor;


    if (!PyArg_ParseTuple(args, "Od", &vec, &factor)) {

        return NULL;

    }


    if (!PyList_Check(vec)) {

        PyErr_SetString(PyExc_TypeError, "Input must be a list");

        return NULL;

    }


    for (Py_ssize_t i = 0; i < PyList_Size(vec); i++) {

        PyObject *elem = PyList_GetItem(vec, i);

        if (!PyNumber_Check(elem)) {

            PyErr_SetString(PyExc_TypeError, "List must contain only numbers");

            return NULL;

        }

        double val = PyFloat_AsDouble(elem);

        val *= factor;

        PyList_SetItem(vec, i, PyFloat_FromDouble(val));

    }



    Py_INCREF(vec);

    return vec;

}


static PyMethodDef VectorOpsMethods[] = {

    {"multiply", vector_ops_multiply, METH_VARARGS, "Multiply each element of a vector by a given factor"},

    {NULL, NULL, 0, NULL}

};


static struct PyModuleDef vector_ops_module = {

    PyModuleDef_HEAD_INIT,

    "vector_ops",

    "Vector operations module",

    -1,

    VectorOpsMethods

};

/* Define the module initialization function */

PyMODINIT_FUNC PyInit_vector_ops(void) {

    return PyModule_Create(&vector_ops_module);

}