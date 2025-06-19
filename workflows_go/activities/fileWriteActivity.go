package activities

import (
	"context"
	"os"

	"github.com/pattern-hunter/chessbot/workflows_go/params"
)

type FileWriteActivityObject struct {
	Timestamp int64
}

func (fwao *FileWriteActivityObject) WriteStringToFileActivity(
	ctx context.Context,
	fileWriteParams params.FileWriteParams,
) (string, error) {
	f, err := os.Create("games_from_workflow.txt")
	if err != nil {
		return "failed", err
	}
	defer f.Close()
	_, err = f.WriteString(fileWriteParams.Contents)
	if err != nil {
		return "failed", err
	}

	return "succeeded", nil
}
