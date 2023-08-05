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

package app

import (
	"github.com/cockroachdb/errors"
	"github.com/sirupsen/logrus"
	"github.com/urfave/cli/v2"

	"github.com/tensorchord/envd/pkg/home"
)

var CommandContextUse = &cli.Command{
	Name:  "use",
	Usage: "Use the specified envd context",
	Flags: []cli.Flag{
		&cli.StringFlag{
			Name:     "name",
			Usage:    "Name of the context",
			Value:    "",
			Required: true,
		},
	},
	Action: contextUse,
}

func contextUse(clicontext *cli.Context) error {
	name := clicontext.String("name")

	err := home.GetManager().ContextUse(name)
	if err != nil {
		return errors.Wrapf(err, "failed to use the specified context %s", name)
	}
	logrus.Infof("Current context is now \"%s\"", name)
	return nil
}
