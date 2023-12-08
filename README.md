# Django Interplexer

Django Interplexer is a REST API interface for tmux.

Example tmux commands:

tmux list-sessions
tmux new-session -d -s first
tmux capture-pane -b first -p
tmux send-keys -t first 'echo hello' C-m
tmux kill-session -t first

Create a REST API with the following:

1. Create a Session model with create_time and modify_time fields

2. Associate the session with a user

3. POST a new session executes "tmux new-session -d -s session-{session.id}"

4. Sessions support two special POST functions:

a. POST /session/{session.id}/capture-pane/

Which executes "tmux capture-pane -b session-{session.id} -p and returns the
output as plain text.

b. POST /session/{session.id}/send-keys/

Which executes "tmux send-keys -t session-{session.id} {keys}"

Use Django REST Framework for everything.

4. DELETE a session executes "tmux kill-session -t session-{session.id}"

## TODO

0. Develop views and URL patterns (`urls.py`) for the API endpoints
0. Implement permission classes to protect API endpoints.
0. Write tests for API endpoints to ensure functionality.
0. Incorporate tmux command execution into the view functions for `capture-pane` and `send-keys` endpoints.
0. Ensure proper error handling and response formatting.
0. Write/update documentation for the REST API, covering all endpoints and usage.
0. Perform code quality checks using `ruff`
0. Refactor and comment code for maintainability.
0. Set up Continuous Integration/Continuous Deployment (CI/CD) pipelines if needed.
