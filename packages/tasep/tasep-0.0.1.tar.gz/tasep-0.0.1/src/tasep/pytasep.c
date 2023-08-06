#include <Python.h>
#include <stdio.h>
#include "tasep.h"
#include "lk_tasep.h"

typedef struct {
  PyObject_HEAD
  randState rs;
} TasepRandStateObject;

static int
TasepRandState_init(TasepRandStateObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"seed", NULL};
    uint64_t seed = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|k", kwlist,
                                     &seed))
        return -1;

    self->rs = randState_init(seed);
    return 0;
}

static PyObject *
py_rand_uni(TasepRandStateObject *self, PyObject *Py_UNUSED(ignored)) {
  return PyFloat_FromDouble(rand_uni(&self->rs));
}

static PyObject *
py_rand_u64(TasepRandStateObject *self, PyObject *Py_UNUSED(ignored)) {
  return PyLong_FromUnsignedLongLong(rand_u64(&self->rs));
}

static PyMethodDef RandState_methods[] = {
    { "rand_uni",
      (PyCFunction) py_rand_uni, METH_NOARGS,
     "Generate uniform random number. [0, 1]"
    },
    { "rand_u64",
      (PyCFunction) py_rand_u64, METH_NOARGS,
     "Generate uniform random number. (INTEGER)"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject TasepRandState = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "tasep.RandState",
    .tp_doc = PyDoc_STR("Random State for tasep."),
    .tp_basicsize = sizeof(TasepRandStateObject),
    .tp_itemsize = 0,
    .tp_init = (initproc) TasepRandState_init,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_methods = RandState_methods,
};

// =====================================================================
typedef struct {
  PyObject_HEAD
  TASEP_LAT tlat;
} TasepObject;

static void
pytasep_dealloc(TasepObject *self)
{
  tasep_free(&self->tlat);
  Py_TYPE(self)->tp_free((PyObject *) self);
}

static int
Tasep_init(TasepObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"N", NULL};
    uint64_t N = 0;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "k", kwlist,
                                     &N))
        return -1;

    self->tlat = tasep_init(N);
    return 0;
}


static PyObject *
py_tasep_randomize(TasepObject *self, PyObject *args, PyObject *kwds) {
  static char *kwlist[] = {"seed", NULL};
  uint64_t seed = 0;

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "k", kwlist,
                                   &seed))
      // raise a error.
      return Py_False;

  tasep_randomize(&self->tlat, seed);
  return Py_True;
}

static PyObject *
py_tasep_evolve(TasepObject *self, PyObject *args, PyObject *kwds) {
  static char *kwlist[] = {"alpha", "beta", "mc_step", "rand", NULL};
  TasepRandStateObject *trs;
  uint64_t mc_step;
  double alpha, beta, *rho;
  PyObject *den_tuple = PyTuple_New((Py_ssize_t) self->tlat.N);

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "ddkO", kwlist,
                                   &alpha, &beta, &mc_step, &trs))
      // raise a error.
      return den_tuple;

  rho = tasep_evolve(&self->tlat, alpha, beta, mc_step, &trs->rs);

  for (Py_ssize_t k=0; k < (Py_ssize_t) self->tlat.N; k++) {
    PyTuple_SetItem(den_tuple, k, PyFloat_FromDouble(rho[k]));
  }
  return den_tuple;
  free(rho);
}

static PyObject *
py_lk_tasep_evolve(TasepObject *self, PyObject *args, PyObject *kwds) {
  static char *kwlist[] = {"alpha", "beta", "Omega_a",
                           "Omega_d", "mc_step", "rand", NULL};
  TasepRandStateObject *trs;
  uint64_t mc_step;
  double alpha, beta, Omega_a, Omega_d, *rho;
  PyObject *den_tuple = PyTuple_New((Py_ssize_t) self->tlat.N);

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "ddddkO", kwlist,
                                   &alpha, &beta, &Omega_a, &Omega_d, &mc_step, &trs))
      // raise a error.
      return den_tuple;

  rho = lk_tasep_evolve(&self->tlat, alpha, beta, Omega_a,
                        Omega_d, mc_step, &trs->rs);

  for (Py_ssize_t k=0; k < (Py_ssize_t) self->tlat.N; k++) {
    PyTuple_SetItem(den_tuple, k, PyFloat_FromDouble(rho[k]));
  }
  return den_tuple;
  free(rho);
}


static PyMethodDef TASEP_methods[] = {
    { "randomize",
      (PyCFunction) py_tasep_randomize,  METH_VARARGS | METH_KEYWORDS,
     "Randomize tasep state."
    },
    { "evolve",
      (PyCFunction) py_tasep_evolve,  METH_VARARGS | METH_KEYWORDS,
     "Simulate tasep and return density as tuple."
    },
    { "lk_evolve",
      (PyCFunction) py_lk_tasep_evolve,  METH_VARARGS | METH_KEYWORDS,
     "Simulate tasep with LK and return density as tuple."
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject Tasep = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "tasep.Tasep",
    .tp_doc = PyDoc_STR("Tasep Object."),
    .tp_basicsize = sizeof(TasepRandStateObject),
    .tp_itemsize = 0,
    .tp_init = (initproc) Tasep_init,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
    .tp_methods = TASEP_methods,
    .tp_dealloc = (destructor) pytasep_dealloc
};


static PyModuleDef tasep_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "tasep",
    .m_doc = "Simulate Tasep from Python using C.",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_tasep(void)
{
    PyObject *m;
    if (PyType_Ready(&TasepRandState) < 0)
        return NULL;
    if (PyType_Ready(&Tasep) < 0)
        return NULL;

    m = PyModule_Create(&tasep_module);
    if (m == NULL)
        return NULL;

    Py_INCREF(&TasepRandState);
    if (PyModule_AddObject(m, "RandState", (PyObject *) &TasepRandState) < 0) {
        Py_DECREF(&TasepRandState);
        Py_DECREF(m);
        return NULL;
    }

    Py_INCREF(&Tasep);
    if (PyModule_AddObject(m, "Tasep", (PyObject *) &Tasep) < 0) {
        Py_DECREF(&Tasep);
        Py_DECREF(m);
        return NULL;
    }
    return m;
}
