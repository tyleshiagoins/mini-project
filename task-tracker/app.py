import os

from flask import Flask

app = Flask(__name__)
app.config["APP_ENV"] = os.getenv("APP_ENV", "development")


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

            #taskInput {
                padding: 10px;
                width: 65%;
            }

            .edit-input {
                padding: 10px;
                max-width: 60%;
            }

            button {
                padding: 10px;
                cursor: pointer;
            }

            li {
                margin-top: 15px;
            }

            .task-button {
                margin-left: 10px;
            }
        </style>
    </head>

    <body>
        <main class="container">
            <h1>Task Tracker</h1>

            <form id="task_form">
                <input type="text" id="taskInput" placeholder="Enter a task" aria-label="Task description">
                <button type="submit">Add task</button>
            </form>

            <h2>Task list</h2>
            <ul id="taskList"></ul>
            <p id="emptyMessage">No tasks added yet.</p>
        </main>

        <script>
            const task_list = document.getElementById("taskList");
            const task_input = document.getElementById("taskInput");
            const task_form = document.getElementById("task_form");

            task_form.onsubmit = function(event) {
                event.preventDefault();
                addTask();
            };

            window.onload = function() {
                const saved_tasks = JSON.parse(localStorage.getItem("tasks")) || [];

                for (const description of saved_tasks) {
                    display_task(description);
                }

                updateEmptyMessage();
            };

            function addTask() {
                const description = task_input.value.trim();

                if (description === "") {
                    return;
                }

                display_task(description);
                save_tasks();
                task_input.value = "";
                task_input.focus();
            }

            function display_task(description) {
                const task = document.createElement("li");

                const task_text = document.createElement("span");
                task_text.textContent = description;

                const edit_input = document.createElement("input");
                edit_input.type = "text";
                edit_input.className = "edit-input";
                edit_input.setAttribute("aria-label", "Edit task description");
                edit_input.required = true;
                edit_input.hidden = true;

                const edit_button = document.createElement("button");
                edit_button.type = "button";
                edit_button.textContent = "edit";
                edit_button.className = "task-button";

                function close_editor() {
                    edit_input.hidden = true;
                    task_text.hidden = false;
                    edit_button.textContent = "edit";
                    edit_button.focus();
                }

                function save_edit() {
                    const new_description = edit_input.value.trim();

                    if (new_description === "") {
                        edit_input.value = "";
                        edit_input.reportValidity();
                        edit_input.focus();
                        return;
                    }

                    task_text.textContent = new_description;
                    save_tasks();
                    close_editor();
                }

                edit_button.onclick = function() {
                    if (edit_input.hidden) {
                        edit_input.value = task_text.textContent;
                        edit_input.hidden = false;
                        task_text.hidden = true;
                        edit_button.textContent = "save";
                        edit_input.focus();
                        edit_input.select();
                    } else {
                        save_edit();
                    }
                };

                edit_input.onkeydown = function(event) {
                    if (event.key === "Enter") {
                        event.preventDefault();
                        save_edit();
                    }

                    if (event.key === "Escape") {
                        close_editor();
                    }
                };

                const delete_button = document.createElement("button");
                delete_button.type = "button";
                delete_button.textContent = "delete";
                delete_button.className = "task-button";

                delete_button.onclick = function() {
                    task.remove();
                    save_tasks();
                };

                task.append(task_text, edit_input, edit_button, delete_button);
                task_list.appendChild(task);
            }

            function save_tasks() {
                const tasks = [];

                for (const task of task_list.children) {
                    tasks.push(task.querySelector("span").textContent);
                }

                localStorage.setItem("tasks", JSON.stringify(tasks));
                updateEmptyMessage();
            }

            function updateEmptyMessage() {
                const empty_message = document.getElementById("emptyMessage");
                empty_message.hidden = task_list.children.length > 0;
            }
        </script>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
