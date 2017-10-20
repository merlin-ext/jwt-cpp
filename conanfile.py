from conans import ConanFile, CMake

class JwtCppConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "OpenSSL/1.1.0c@madduci/stable" # comma separated list of requirements
   generators = "cmake"
   default_options = "OpenSSL:shared=False"

   def imports(self):
      self.copy("*.dll", dst="bin", src="bin") # From bin to bin
      self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin