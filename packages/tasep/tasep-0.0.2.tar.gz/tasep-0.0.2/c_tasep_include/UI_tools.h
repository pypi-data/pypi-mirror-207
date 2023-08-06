char *get_arg_param(int argc, char **argv, char *option);
int get_flag(int argc, char **argv, char *flag);
double parse_arg_d(int argc, char **argv, char *option, double def_val);
unsigned long parse_arg_ul(int argc, char **argv, char *option,
                           unsigned long def_val);
unsigned long long parse_arg_ull(int argc, char **argv, char *option,
                                 unsigned long long def_val);
unsigned int parse_arg_ui(int argc, char **argv, char *option,
                          unsigned int def_val);
int parse_arg_i(int argc, char **argv, char *option, int def_val);
int parse_help(int argc, char **argv, char *helpstr);
