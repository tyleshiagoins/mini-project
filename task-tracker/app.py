from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Task Tracker</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 40px;
            }

            .container {
                background-color: white;
                max-width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 8px;
            }

            h1 {
                text-align: center;
            }

            p {
                text-align: center;
                color: #555;
            }

            input {
                padding: 10px;
                width: 65%;
            }

            button {
                padding: 10px;
                cursor: pointer;
            }

            li {
                margin-top: 15px;
            }

            .delete-button {
                margin-left: 10px;
            }
        </style>
    </head>

    <body>
        <main class="container">
            <h1>Task Tracker</h1>

            <input type="text" id="taskInput" placeholder="Enter a task">
            <button type="button" onclick="addTask()">Add Task</button>

            <h2>Task List</h2>
            <ul id="taskList"></ul>
            <p id="emptyMessage">No tasks added yet.</p>
        </main>

        <script>
            // load previously saved tasks when the page opens
            window.onload = function() {
                const savedTasks = JSON.parse(
                    localStorage.getItem("tasks")
                ) || [];

                for (const taskDescription of savedTasks) {
                    displayTask(taskDescription);
                }

                updateEmptyMessage();
            };

            // add a task
            function addTask() {
                const taskInput = document.getElementById("taskInput");
                const taskDescription = taskInput.value.trim();

                if (taskDescription === "") {
                    return;
                }

                displayTask(taskDescription);
                saveTasks();

                taskInput.value = "";
            }

            // display task and delete
            function displayTask(taskDescription) {
                const taskList = document.getElementById("taskList");
                const newTask = document.createElement("li");

                const taskText = document.createElement("span");
                taskText.textContent = taskDescription;

                const deleteButton = document.createElement("button");
                deleteButton.textContent = "Delete";
                deleteButton.className = "delete-button";

                deleteButton.onclick = function() {
                    newTask.remove();
                    saveTasks();
                };

                newTask.appendChild(taskText);
                newTask.appendChild(deleteButton);
                taskList.appendChild(newTask);

                updateEmptyMessage();
            }

            // remember input
            function saveTasks() {
                const taskList = document.getElementById("taskList");
                const savedTasks = [];

                for (const task of taskList.children) {
                    savedTasks.push(
                        task.querySelector("span").textContent
                    );
                }

                localStorage.setItem(
                    "tasks",
                    JSON.stringify(savedTasks)
                );

                updateEmptyMessage();
            }

            //  empty message when there's no tasks.
            function updateEmptyMessage() {
                const taskList = document.getElementById("taskList");
                const emptyMessage = document.getElementById("emptyMessage");

                if (taskList.children.length === 0) {
                    emptyMessage.hidden = false;
                } else {
                    emptyMessage.hidden = true;
                }
            }
        </script>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
