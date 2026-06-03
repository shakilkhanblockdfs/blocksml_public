.PHONY: install configure build run clean distclean

BUILD_TYPE ?= Release
APP := conan2_build_demo

install:
	conan install . --build=missing -s build_type=$(BUILD_TYPE)

configure:
	cmake --preset conan-release

build:
	cmake --build --preset conan-release

run:
	./build/$(BUILD_TYPE)/$(APP)

clean:
	cmake --build --preset conan-release --target clean

distclean:
	rm -rf build CMakeUserPresets.json

