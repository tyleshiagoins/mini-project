#!/bin/bash
set -e

package_url="https://github.com/tyleshiagoins/mini-project/releases/download/staging-${RENDER_GIT_COMMIT}/task-tracker.zip"

curl --proto '=https' --proto-redir '=https' --fail --location "$package_url" --output /tmp/task-tracker.zip
unzip -o /tmp/task-tracker.zip
pip install --only-binary=:all: -r requirements.txt gunicorn

mkdir -p static
printf '%s' "$RENDER_GIT_COMMIT" > static/deployment-version.txt