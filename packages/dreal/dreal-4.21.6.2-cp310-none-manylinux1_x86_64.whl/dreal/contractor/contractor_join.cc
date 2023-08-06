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
#include "dreal/contractor/contractor_join.h"

#include <utility>

#include "dreal/util/assert.h"

using std::ostream;
using std::vector;

namespace dreal {

ContractorJoin::ContractorJoin(vector<Contractor> contractors,
                               const Config& config)
    : ContractorCell{Contractor::Kind::JOIN,
                     DynamicBitset(ComputeInputSize(contractors)),
                     config},
      contractors_{std::move(contractors)} {
  DREAL_ASSERT(!contractors_.empty());
  DynamicBitset& input{mutable_input()};
  for (const Contractor& c : contractors_) {
    input |= c.input();
    if (c.include_forall()) {
      set_include_forall();
    }
  }
}

void ContractorJoin::Prune(ContractorStatus* cs) const {
  ContractorStatus saved_original{*cs};
  cs->mutable_box().set_empty();
  for (const Contractor& contractor : contractors_) {
    ContractorStatus state_i{saved_original};
    contractor.Prune(&state_i);
    cs->InplaceJoin(state_i);
  }
}

ostream& ContractorJoin::display(ostream& os) const {
  os << "Join(";
  for (const Contractor& c : contractors_) {
    os << c << ", ";
  }
  return os << ")";
}

}  // namespace dreal
