INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MSGTOOLS msgtools)

FIND_PATH(
    MSGTOOLS_INCLUDE_DIRS
    NAMES msgtools/api.h
    HINTS $ENV{MSGTOOLS_DIR}/include
        ${PC_MSGTOOLS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MSGTOOLS_LIBRARIES
    NAMES gnuradio-msgtools
    HINTS $ENV{MSGTOOLS_DIR}/lib
        ${PC_MSGTOOLS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MSGTOOLS DEFAULT_MSG MSGTOOLS_LIBRARIES MSGTOOLS_INCLUDE_DIRS)
MARK_AS_ADVANCED(MSGTOOLS_LIBRARIES MSGTOOLS_INCLUDE_DIRS)

