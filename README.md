# chessbot

## Running workflow from terminal
```
temporal server start-dev 
```

```
go run main.go
```


```
temporal workflow start \
   --task-queue lichess-queue \
   --type ContinuousTrainingWorkflow \
   --workflow-id 1234 \
   --input '{"username": "punmaster_general", "since": 1736959353}'
```