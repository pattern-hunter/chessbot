# chessbot

## Running workflow from terminal
```
temporal workflow start \
   --task-queue lichess-queue \
   --type ContinuousLearningWorkflow \
   --workflow-id 1234 \
   --input '{"username": "punmaster_general", "since": 1736959353}'
```