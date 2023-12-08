# Django Interplexer

Django Interplexer is a Django-based REST API that provides an interface for
interacting with `tmux` sessions. It allows users to create, capture, send keys
to, and destroy `tmux` sessions via HTTP requests.


## Features

- RESTful interface for `tmux` session management.
- User association with `tmux` sessions to maintain user-specific sessions.
- Creation and deletion of `tmux` sessions through API endpoints.
- Capture the output of `tmux` pane and send keystrokes to a session.


## Requirements

- Python version 3.7 or higher.
- Django
- Django REST Framework


## Installation

To install Django Interplexer, follow these steps:

1. Ensure you have Python 3.7 or higher.
2. Set up a Python virtual environment (optional but recommended).
3. Install the package and its dependencies.

```sh
pip install django-interplexer
```

Alternatively, if you are setting this up for development purposes, you might
want to install with the `-e` flag (editable mode) and development
dependencies.

```sh
git clone https://github.com/grantjenks/django-interplexer.git
cd django-interplexer
pip install -e .
pip install -r requirements-dev.txt
```


## Configuration

Include `interplexer` in your Django `INSTALLED_APPS` setting.

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'interplexer',
]
```


## Running Tests

To verify that everything is set up correctly, you can run the test suite:

```sh
pytest
```

To check code style and formatting, you can use `ruff`:

```sh
ruff format .
ruff --fix .
```


## Usage

### API Endpoints

#### Sessions Management

- **POST /api/sessions/**: Create a new `tmux` session associated with the
  authenticated user.

- **GET /api/sessions/**: List all sessions associated with the authenticated
  user.

- **GET /api/sessions/{session.id}/**: Retrieve details of a specific session.

- **DELETE /api/sessions/{session.id}/**: Terminate a `tmux` session and remove
  it from the database.


#### Special Session Functions

- **POST /api/session/{session.id}/capture-pane/**: Captures the output of the
  specified `tmux` session's pane and returns the content as plain text.

- **POST /api/session/{session.id}/send-keys/**: Send keystrokes to the
  specified `tmux` session. The keys must be included in the request body.


### Example tmux Commands

Here are some equivalent `tmux` commands for what the API facilitates:

```sh
tmux list-sessions
tmux new-session -d -s session-{session.id}
tmux capture-pane -b session-{session.id} -p
tmux send-keys -t session-{session.id} 'echo hello' C-m
tmux kill-session -t session-{session.id}
```


## License

Django Interplexer is distributed under the Apache 2.0 License.


## Additional Resources

- Official Documentation: [https://grantjenks.com/docs/django-interplexer/](https://grantjenks.com/docs/django-interplexer/)

- Source Code: [https://github.com/grantjenks/django-interplexer](https://github.com/grantjenks/django-interplexer)

- Issue Tracker: [https://github.com/grantjenks/django-interplexer/issues](https://github.com/grantjenks/django-interplexer/issues)
