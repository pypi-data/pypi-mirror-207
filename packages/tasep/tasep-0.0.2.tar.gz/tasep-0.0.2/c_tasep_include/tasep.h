#ifndef TASEP_H_INCLUDED
#define TASEP_H_INCLUDED

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include "random.h"

typedef struct {
  uint64_t N;               // number of lattice sites.
  uint8_t *restrict C;      // microscopic configuration.
} TASEP_LAT;

TASEP_LAT tasep_init(uint64_t N);
void tasep_free(TASEP_LAT *tlat);
void tasep_randomize(TASEP_LAT *tlat, uint64_t x);
double *tasep_evolve(TASEP_LAT *tlat, double alpha, double beta,
                  uint64_t mcstep, randState *r);
#endif
