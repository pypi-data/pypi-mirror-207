#ifndef LK_TASEP_H_INCLUDED
#define LK_TASEP_H_INCLUDED

#include "tasep.h"
double *lk_tasep_evolve(TASEP_LAT *restrict tlat, double alpha,
    double beta, double omega_a, double omega_d,
    uint64_t mcstep, randState *restrict r);
#endif
