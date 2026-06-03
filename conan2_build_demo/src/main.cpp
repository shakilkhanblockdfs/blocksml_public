#include <fmt/core.h>

#include <string>

int main() {
    const std::string tool = "Conan 2";
    fmt::print("Hello from a {} C++ dependency demo.\n", tool);
    fmt::print("The fmt library was resolved by Conan and linked by CMake.\n");
    return 0;
}

