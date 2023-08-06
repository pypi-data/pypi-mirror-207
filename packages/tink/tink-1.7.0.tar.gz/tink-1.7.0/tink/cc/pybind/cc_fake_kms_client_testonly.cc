// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
///////////////////////////////////////////////////////////////////////////////

#include "tink/cc/pybind/cc_fake_kms_client_testonly.h"

#include <string>
#include <utility>

#include "pybind11/pybind11.h"
#include "tink/util/fake_kms_client.h"
#include "tink/util/statusor.h"
#include "tink/cc/pybind/tink_exception.h"

namespace crypto {
namespace tink {
namespace test {

using pybind11::google_tink::TinkException;

void PybindRegisterCcFakeKmsClientTestonly(pybind11::module* module) {
  namespace py = pybind11;
  py::module& m = *module;
  m.def(
      "register_fake_kms_client_testonly",
      [](const std::string& key_uri,
         const std::string& credentials_path) -> void {
        crypto::tink::util::Status result =
            FakeKmsClient::RegisterNewClient(key_uri, credentials_path);
        if (!result.ok()) {
          throw TinkException(result);
        }
      },
      py::arg("key_uri"), "URI of the key which should be used.",
      py::arg("credentials_path"), "Path to the credentials for the client.");
}

}  // namespace test
}  // namespace tink
}  // namespace crypto
