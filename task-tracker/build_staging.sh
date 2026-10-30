set -e

package_url="https://github.com/tyleshiagoins/mini-project/releases/download/staging-${RENDER_GIT_COMMIT}/task-tracker.zip"

curl --fail --location "$package_url" --output /tmp/task-tracker.zip
unzip -o /tmp/task-tracker.zip
pip install -r requirements.txt gunicorn

mkdir -p static
printf '%s' "$RENDER_GIT_COMMIT" > static/deployment-version.txt