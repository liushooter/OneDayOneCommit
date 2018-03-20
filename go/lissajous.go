// https://en.wikipedia.org/wiki/Lissajous_curve

package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"log"
	"math"
	"math/rand"
	"net/http"
	"os"
	"time"
)

var palette = []color.Color{color.White, color.Black}

const (
	whiteIndex = 0
	blockIndex = 1
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())

	if len(os.Args) > 1 && os.Args[1] == "web" {
		handler := func(w http.ResponseWriter, r *http.Request) {
			lissajous(w)
		}

		http.HandleFunc("/", handler)
		log.Fatal(http.ListenAndServe("localhost:3000", nil))
		return

	}

}

func lissajous(out io.Writer) {
	const (
		cycles  = 5     // 完整的x振荡器变化的个数
		res     = 0.001 // 角度分辨率
		size    = 100   // 图像画布范围
		nframes = 64    // 帧数
		delay   = 8     // 以 10ms为单位的帧见延迟
	)

	freg := rand.Float64() * 3.0 // y振荡器的相对频率
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0

	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)

		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freg + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), blockIndex)
		}

		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)

	}

	gif.EncodeAll(out, &anim) // 忽略编码错误
}
