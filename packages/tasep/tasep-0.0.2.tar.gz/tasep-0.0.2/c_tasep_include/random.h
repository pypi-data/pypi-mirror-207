/* Original: Written in 2018 by David Blackman and Sebastiano Vigna
 * (vigna@acm.org) modified: in 2023 by Rohn chatterjee (rohn.ch@gmail.com)
 */

#ifndef RANDOM_H_INCLUDED
#define RANDOM_H_INCLUDED

#include <stdint.h>
#define randState xor256s_t
#define randState_init xor256s_init

inline uint64_t rotl(const uint64_t x, int k) {
  return (x << k) | (x >> (64 - k));
}

typedef struct {
  uint64_t s[4];
} xor256s_t;

uint64_t next(xor256s_t *state);

/* This is the jump function for the generator. It is equivalent
   to 2^128 calls to next(); it can be used to generate 2^128
   non-overlapping subsequences for parallel computations. */

void jump(xor256s_t *state);

/* This is the long-jump function for the generator. It is equivalent to
   2^192 calls to next(); it can be used to generate 2^64 starting points,
   from each of which jump() will generate 2^64 non-overlapping
   subsequences for parallel distributed computations. */

void long_jump(xor256s_t *state);

uint64_t smx64_next(uint64_t x);

xor256s_t xor256s_init(uint64_t x);

double rand_uni(xor256s_t *state);

uint64_t rand_u64(xor256s_t *state);
#endif
