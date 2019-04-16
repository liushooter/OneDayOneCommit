package main

import (
	"os"

	"github.com/olekukonko/tablewriter"
)

func main() {
	tableView()
}

func tableView() {
	data := [][]string{
		[]string{"1", "63.2734", "131.01", "Jackie Chan北京耀莱", "19914", "1063583.70", "152", "53.41"},
		[]string{"2", "48.4789", "93.88", "太原龙湖万达广场店", "10608", "796759.40", "113", "75.11"},
		[]string{"3", "76.7733", "153.34", "金逸北京荟聚IMAX店", "12727", "782341.40", "83", "61.47"},
		[]string{"4", "67.5394", "121.80", "阜阳颍州万达广场店", "12545", "780178.80", "103", "62.19"},
		[]string{"5", "49.0023", "50.77", "鹤壁银兴国际影城", "15433", "749703.00", "304", "48.58"},
	}

	table := tablewriter.NewWriter(os.Stdout)
	table.SetHeader([]string{"排名", "上座率", "场均人次", "影院名称", "当日观众人数", "当日票房", "当日场次", "场均票价"})
	table.SetBorders(tablewriter.Border{Left: true, Top: false, Right: true, Bottom: false})
	table.SetCenterSeparator("|")
	table.AppendBulk(data)

	table.Render()
}
