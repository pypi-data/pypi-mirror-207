/*
    Copyright (c) 2022 Advanced Micro Devices, Inc. All rights reserved.
*/

#ifndef ROCM_SYMLINK_ROCRAND_SCRAMBLED_SOBOL64_CONSTANTS_H
#define ROCM_SYMLINK_ROCRAND_SCRAMBLED_SOBOL64_CONSTANTS_H

#if defined(ROCM_NO_WRAPPER_HEADER_WARNING) || defined(ROCM_SYMLINK_GAVE_WARNING)
/* include file */
#include "rocrand/rocrand_scrambled_sobol64_constants.h"
#else
/* give warning */
#if defined(_MSC_VER)
#pragma message(": warning:This file is deprecated. Use the header file from /opt/rocm-5.5.0/include/rocrand/rocrand_scrambled_sobol64_constants.h by using #include <rocrand/rocrand_scrambled_sobol64_constants.h>")
#elif defined(__GNUC__)
#warning "This file is deprecated. Use the header file from /opt/rocm-5.5.0/include/rocrand/rocrand_scrambled_sobol64_constants.h by using #include <rocrand/rocrand_scrambled_sobol64_constants.h>"
#endif
/* include file */
#define ROCM_SYMLINK_GAVE_WARNING
#include "rocrand/rocrand_scrambled_sobol64_constants.h"
#undef ROCM_SYMLINK_GAVE_WARNING
#endif /* defined(ROCM_NO_WRAPPER_HEADER_WARNING) || defined(ROCM_SYMLINK_GAVE_WARNING) */

#endif /* ROCM_SYMLINK_ROCRAND_SCRAMBLED_SOBOL64_CONSTANTS_H */


