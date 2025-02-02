package workflows

import (
	"time"

	"github.com/pattern-hunter/chessbot/workflows/activities"
	"github.com/pattern-hunter/chessbot/workflows/params"
	"go.temporal.io/sdk/workflow"
)

// ...

// ContinuousTrainingWorkflow periodically trains the chessbot
func ContinuousTrainingWorkflow(ctx workflow.Context, lichessParams params.LichessParams) error {
	activityOptions := workflow.ActivityOptions{
		StartToCloseTimeout: 30 * time.Second,
	}
	ctx = workflow.WithActivityOptions(ctx, activityOptions)

	lichessActivityParams := params.LichessParams{
		Username: "punmaster_general",
		Since:    1736959353,
	}

	var lao *activities.LichessActivityObject
	var lichessActivityResult string
	err := workflow.ExecuteActivity(ctx, lao.GetUserGamesFromLichessActivity, lichessActivityParams).Get(ctx, &lichessActivityResult)
	if err != nil {
		return err
	}

	fileWriteActivityParams := params.FileWriteParams{
		Contents: lichessActivityResult,
	}

	var fwao *activities.FileWriteActivityObject
	var fileWriteActivityResult string
	err = workflow.ExecuteActivity(ctx, fwao.WriteStringToFileActivity, fileWriteActivityParams).Get(ctx, &fileWriteActivityResult)
	if err != nil {
		return err
	}

	return nil
}
