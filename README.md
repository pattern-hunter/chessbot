# chessbot

## Running python workflor from terminal
```
python run_worker.py
```

```
python run_workflow.py
```


## Running go workflow from terminal
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