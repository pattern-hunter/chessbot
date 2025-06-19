package activities

import (
	"context"
	"os/exec"

	"github.com/pattern-hunter/chessbot/workflows_go/params"
)

type ParseDataActivityObject struct {
	Timestamp int64
}

func (pdao *ParseDataActivityObject) ParseGameDataActivity(
	ctx context.Context,
	parseDataParams params.ParseDataParams,
) error {
	err := exec.Command("python", "main.py", parseDataParams.Filename).Run()
	return err
}
