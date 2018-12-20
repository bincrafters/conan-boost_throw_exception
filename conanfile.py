#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostThrow_ExceptionConan(base.BoostBaseConan):
    name = "boost_throw_exception"
    url = "https://github.com/bincrafters/conan-boost_throw_exception"
    lib_short_names = ["throw_exception"]
    header_only_libs = ["throw_exception"]
    b2_requires = [
        "boost_assert",
        "boost_config"
    ]
