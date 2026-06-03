from conan import ConanFile
from conan.tools.cmake import cmake_layout


class Conan2BuildDemoRecipe(ConanFile):
    name = "conan2_build_demo"
    version = "0.1.0"
    package_type = "application"

    settings = "os", "compiler", "build_type", "arch"

    requires = "fmt/10.2.1"

    generators = "CMakeDeps", "CMakeToolchain"

    def layout(self):
        cmake_layout(self)
