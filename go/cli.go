package main

import (
	"fmt"
	"os"

	"gopkg.in/urfave/cli.v1"
)

func main() {
	app := cli.NewApp()

	app.Flags = []cli.Flag{
		cli.BoolFlag{
			Name:  "verbose",
			Usage: "Prints more verbose output to the console",
		},
		cli.BoolFlag{
			Name:  "dry, d",
			Usage: "Runs the algorithm without making any changes to the filesystem",
		},
	}

	app.Commands = []cli.Command{
		{
			Name:    "parse",
			Aliases: []string{"p"},
			Usage:   "Parse the specified directory",
			Action: func(c *cli.Context) {
				fmt.Printf("%+v\n", c.GlobalBool("verbose"))
			},
		},
	}

	app.Run(os.Args)
}
