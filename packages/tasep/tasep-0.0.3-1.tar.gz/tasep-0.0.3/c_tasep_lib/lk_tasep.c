#include "lk_tasep.h"

double *lk_tasep_evolve(TASEP_LAT *restrict tlat, double alpha, double beta,
                  double Omega_a, double Omega_d, uint64_t mcstep, randState *restrict r) {

  uint64_t last = tlat->N - 1, i, j;
  double *restrict density = (double *)calloc(tlat->N, sizeof(double));
  double omega_a = Omega_a / (double) tlat->N;
  double omega_d = Omega_d / (double) tlat->N;

  for (uint64_t k = 0; k < tlat->N; k++) {
    density[k] = 0;
  }

  for (uint64_t step = 0; step < mcstep; step++) {
    if (step % 1000 == 0)
      printf(" Progress: %2.2f\r", (double)step/(double)mcstep);

    for (uint64_t k = 0; k < tlat->N; k++) {
      i = rand_u64(r) % tlat->N; // choose a random site.
      j = rand_u64(r) % tlat->N; // choose a random site.

      if ((tlat->C[j] == 0) && (rand_uni(r) < omega_a)) {
        tlat->C[j] = 1;
      } else if ((tlat->C[j] == 1) && (rand_uni(r) < omega_d)) {
        tlat->C[j] = 0;
      }

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
