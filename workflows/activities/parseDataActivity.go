package activities

import (
	"context"
	"fmt"
	"os/exec"

	"github.com/pattern-hunter/chessbot/workflows/params"
)

type ParseDataActivityObject struct {
	Timestamp int64
}

func (pdao *ParseDataActivityObject) ParseGameDataActivity(
	ctx context.Context,
	parseDataParams params.ParseDataParams,
) error {
	err := exec.Command(fmt.Sprintf("python main.py parse %v", parseDataParams.Filename)).Run()
	return err
}
