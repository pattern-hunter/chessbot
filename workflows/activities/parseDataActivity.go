package activities

import (
	"context"
	"fmt"
	"io"
	"net/http"

	"github.com/pattern-hunter/chessbot/workflows/params"
)

type ParseDataActivityObject struct {
	Timestamp int64
}

func (lao *ParseDataActivityObject) GetUserGamesFromLichessActivity(
	ctx context.Context,
	parseDataParams params.ParseDataParams,
) (string, error) {
	url := fmt.Sprintf(
		"https://lichess.org/api/games/user/%v?since=%v",
		lichessParams.Username,
		lichessParams.Since,
	)

	response, err := http.Get(url)
	if err != nil {
		return "", nil
	}

	bodyBytes, err := io.ReadAll(response.Body)
	if err != nil {
		return "", err
	}

	return string(bodyBytes), nil
}
