#include "tasep.h"

TASEP_LAT tasep_init(uint64_t N) {
  uint8_t *restrict C = (uint8_t *)calloc(N, sizeof(uint8_t));
  TASEP_LAT tlat = {N, C};
  return tlat;
}

void tasep_free(TASEP_LAT *tlat) {
  free(tlat->C);
  tlat->C = NULL;
}

void tasep_randomize(TASEP_LAT *restrict tlat, uint64_t x) {
  // xor shift 64
  for (uint64_t i = 0; i < tlat->N; i++) {
    x ^= x >> 12;
    x ^= x << 25;
    x ^= x >> 27;
    tlat->C[i] = (x & 1);
  }
}

double *tasep_evolve(TASEP_LAT *restrict tlat, double alpha, double beta,
                  uint64_t mcstep, randState *restrict r) {

  uint64_t last = tlat->N - 1, i;
  double *density = (double *)calloc(tlat->N, sizeof(double));

  for (uint64_t k = 0; k < tlat->N; k++) {
    density[k] = 0;
  }

  for (uint64_t step = 0; step < mcstep; step++) {

    if (step % 1000 == 0)
      printf(" Progress: %2.2f\r", (double)step/(double)mcstep);

    for (uint64_t k = 0; k < tlat->N; k++) {
      i = rand_u64(r) % tlat->N; // choose a random site.
      // entry
      //
      if ((i == 0) && (tlat->C[0] == 0) && (rand_uni(r) < alpha)) {
        tlat->C[0] = 1;
      } else if (i == last) {
        if ((tlat->C[last] == 1) && (rand_uni(r) < beta)) {
          tlat->C[last] = 0;
        }
      } else if ((tlat->C[i] == 1) && (tlat->C[i + 1] == 0)) {
        tlat->C[i] = 0;
        tlat->C[i + 1] = 1;
      }
    }
    for (uint64_t k = 0; k < tlat->N; k++) {
      density[k] += tlat->C[k];
    }
  }
  for (uint64_t k = 0; k < tlat->N; k++) {
    density[k] /= (double) mcstep;
  }
  return density;
}
