cmake_minimum_required(VERSION 3.15)

project(conan2_build_demo VERSION 0.1.0 LANGUAGES CXX)

find_package(fmt REQUIRED CONFIG)

add_executable(conan2_build_demo src/main.cpp)
target_compile_features(conan2_build_demo PRIVATE cxx_std_17)
target_link_libraries(conan2_build_demo PRIVATE fmt::fmt)

