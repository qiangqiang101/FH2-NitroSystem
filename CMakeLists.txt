cmake_minimum_required(VERSION 3.20)
project(FnFNitroInFH2 VERSION 2.0.1 LANGUAGES C CXX RC)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add the platform submodule for its header (fh2mod_api). The platform DLL itself is not built here: it needs llvm-mingw,
# so the release workflow builds it separately and ships DWrite.dll (see README)
add_subdirectory(platform EXCLUDE_FROM_ALL)

# The DLL's version info (Properties > Details), made from project(VERSION) above, so the version is only set there
file(CONFIGURE OUTPUT ${CMAKE_BINARY_DIR}/version.rc @ONLY CONTENT [[
#include <winver.h>

VS_VERSION_INFO VERSIONINFO
 FILEVERSION     @PROJECT_VERSION_MAJOR@,@PROJECT_VERSION_MINOR@,@PROJECT_VERSION_PATCH@,0
 PRODUCTVERSION  @PROJECT_VERSION_MAJOR@,@PROJECT_VERSION_MINOR@,@PROJECT_VERSION_PATCH@,0
 FILEFLAGSMASK   0x3fL
 FILEFLAGS       0x0L
 FILEOS          VOS_NT_WINDOWS32
 FILETYPE        VFT_DLL
 FILESUBTYPE     VFT2_UNKNOWN
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904b0"
        BEGIN
            VALUE "CompanyName",      "FnFNitro Mod Team"
            VALUE "FileDescription",  "Fast & Furious Nitro in Forza Horizon 2"
            VALUE "FileVersion",      "@PROJECT_VERSION@"
            VALUE "InternalName",     "FnFNitro"
            VALUE "LegalCopyright",   "MIT License"
            VALUE "OriginalFilename", "FnFNitro.dll"
            VALUE "ProductName",      "FnFNitro for FH2"
            VALUE "ProductVersion",   "@PROJECT_VERSION@"
        END
    END
    BLOCK "VarFileInfo"
    BEGIN
        VALUE "Translation", 0x409, 1200
    END
END
]])

add_library(FnFNitro SHARED
    src/nitro_mod.cpp
    ${CMAKE_BINARY_DIR}/version.rc
    src/hud.rc
)

# rc files don't track what they embed, so changing a HUD file would not rebuild the DLL
file(GLOB_RECURSE HUD_FILES CONFIGURE_DEPENDS ${CMAKE_SOURCE_DIR}/hud/* ${CMAKE_SOURCE_DIR}/particles/* ${CMAKE_SOURCE_DIR}/sounds/*)
set_source_files_properties(src/hud.rc PROPERTIES OBJECT_DEPENDS "${HUD_FILES}")

target_link_libraries(FnFNitro PRIVATE fh2mod_api user32 xinput winmm)
set_target_properties(FnFNitro PROPERTIES OUTPUT_NAME FnFNitro PREFIX "")
target_compile_definitions(FnFNitro PRIVATE
    FNFNITRO_VERSION="${PROJECT_VERSION}"
    WIN32_LEAN_AND_MEAN
    NOMINMAX
    UNICODE
    _UNICODE
)

if(MSVC)
    # Avoid loading a second C++ runtime before Azimuth initializes another game.
    set_property(TARGET FnFNitro PROPERTY MSVC_RUNTIME_LIBRARY
        "MultiThreaded$<$<CONFIG:Debug>:Debug>")
    target_compile_options(FnFNitro PRIVATE /W4 /permissive- /utf-8 /EHsc)
else()
    target_compile_options(FnFNitro PRIVATE -Wall -Wextra)
    target_link_options(FnFNitro PRIVATE -static)
endif()
