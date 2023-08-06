/*
   Copyright 2017 Toyota Research Institute

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
#pragma once

#include <fmt/format.h>

#include <stdexcept>

namespace dreal {

#define DREAL_RUNTIME_ERROR(...)                                 \
  std::runtime_error(fmt::format("{}:{} ", __FILE__, __LINE__) + \
                     fmt::format(__VA_ARGS__))

#define DREAL_UNREACHABLE() \
  throw DREAL_RUNTIME_ERROR("Should not be reachable.")  // LCOV_EXCL_LINE

}  // namespace dreal
