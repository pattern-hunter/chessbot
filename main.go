package main

import (
	"github.com/pattern-hunter/chessbot/workflows"
	"github.com/pattern-hunter/chessbot/workflows/activities"
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/worker"
)

func main() {
	temporalClient, err := client.Dial(client.Options{})
	if err != nil {
		panic(err)
	}
	defer temporalClient.Close()
	chessBotWorker := worker.New(temporalClient, "lichess-queue", worker.Options{})

	chessBotWorker.RegisterWorkflow(workflows.ContinuousTrainingWorkflow)

	lichessActivityObject := activities.LichessActivityObject{
		Timestamp: 1,
	}
	chessBotWorker.RegisterActivity(lichessActivityObject.GetUserGamesFromLichessActivity)

	fileWriteActivityObject := activities.FileWriteActivityObject{
		Timestamp: 1,
	}
	chessBotWorker.RegisterActivity(fileWriteActivityObject.WriteStringToFileActivity)

	parseDataActivityObject := activities.ParseDataActivityObject{
		Timestamp: 1,
	}
	chessBotWorker.RegisterActivity(parseDataActivityObject.ParseGameDataActivity)

	// Run the Worker
	err = chessBotWorker.Run(worker.InterruptCh())
	if err != nil {
		panic(err)
	}
}
