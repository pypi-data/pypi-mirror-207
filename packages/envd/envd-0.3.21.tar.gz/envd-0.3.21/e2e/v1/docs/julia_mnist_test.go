// Copyright 2023 The envd Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package docs

import (
	"strconv"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"

	"github.com/tensorchord/envd/e2e/v1"
)

var _ = Describe("julia_mnist", Ordered, func() {
	exampleName := "julia_mnist"
	testcase := "e2e"
	e := e2e.NewExample(e2e.BuildContextDirWithName(exampleName), testcase)
	BeforeAll(e.BuildImage(true))
	BeforeEach(e.RunContainer())
	It("execute runtime command `julia-mnist`", func() {
		res, err := e.ExecRuntimeCommand("julia-mnist")
		Expect(err).To(BeNil())
		IsNumber := func(s string) bool {
			_, err = strconv.ParseFloat(s, 64)
			return err == nil
		}
		Expect(res).To(Satisfy(IsNumber))
	})
	AfterEach(e.DestroyContainer())
})
