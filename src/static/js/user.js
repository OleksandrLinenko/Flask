const title = document.getElementById("title");
const originalTitle = title.textContent;

document.getElementById("load-users").addEventListener("click", function () {
    fetch("/api/users")
        .then(function (response) {
            return response.json();
        })
        .then(function (users) {

            const list = document.getElementById("users");
            list.innerHTML = "";

            users.forEach(function (user) {

                const li = document.createElement("li");
                const a = document.createElement("a");
                a.href = "/users/" + user.id + "/edit";
                a.textContent = user.name;

                li.appendChild(a);
                
                li.dataset.id = user.id;

                li.addEventListener("click", function () {

                    const id = this.dataset.id;

                    document.getElementById("edit-user-form").action =
                        "/users/" + id + "/edit";

                    fetch("/api/users/" + id)
                        .then(function (response) {
                            return response.json();
                        })
                        .then(function (user) {

                            document.querySelector("#edit-user-form input[name='name']").value =
                                user.name;

                            document.getElementById("result").textContent =
                                "Editing: " + user.name;

                        });
                });
                list.appendChild(li);
            });
        });
});

document.getElementById("change-title").addEventListener("click", function () {
    title.textContent = "The title has been changed!";
});

document.getElementById("restore-title").addEventListener("click", function () {
    title.textContent = originalTitle;
});

document.getElementById("show-alert").addEventListener("click", function () {
    alert("Hello from JavaScript!");
});

document.getElementById("ask-name").addEventListener("click", function () {
    const name = prompt("What is your name?");

    if (name) {
        document.getElementById("result").textContent =
            "Nice to meet you, " + name + "!";
    }
});

const messages = document.querySelectorAll(".message");
messages.forEach(function (message) {
    message.style.fontWeight = "bold";
    message.addEventListener("click", function () {

        alert(message.textContent);
    });
});

const errorBlock = document.querySelector("div.error");
errorBlock.addEventListener("click", function () {
    errorBlock.style.color = "green";
    errorBlock.textContent = "Error fixed!";
});


