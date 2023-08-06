/*
    Copyright (c) 2022 Advanced Micro Devices, Inc. All rights reserved.
*/

#ifndef ROCM_SYMLINK_HIPSPARSE_H
#define ROCM_SYMLINK_HIPSPARSE_H

#if defined(ROCM_NO_WRAPPER_HEADER_WARNING) || defined(ROCM_SYMLINK_GAVE_WARNING)
/* include file */
#include "hipsparse/hipsparse.h"
#else
/* give warning */
#if defined(_MSC_VER)
#pragma message(": warning:This file is deprecated. Use the header file from /opt/rocm-5.5.0/include/hipsparse/hipsparse.h by using #include <hipsparse/hipsparse.h>")
#elif defined(__GNUC__)
#warning "This file is deprecated. Use the header file from /opt/rocm-5.5.0/include/hipsparse/hipsparse.h by using #include <hipsparse/hipsparse.h>"
#endif
/* include file */
#define ROCM_SYMLINK_GAVE_WARNING
#include "hipsparse/hipsparse.h"
#undef ROCM_SYMLINK_GAVE_WARNING
#endif /* defined(ROCM_NO_WRAPPER_HEADER_WARNING) || defined(ROCM_SYMLINK_GAVE_WARNING) */

#endif /* ROCM_SYMLINK_HIPSPARSE_H */


