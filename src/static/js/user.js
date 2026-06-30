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
                li.textContent = user.name;

                list.appendChild(li);

            });

        })
        .catch(function (error) {
            console.log(error);
        });

});

document.getElementById("change-title").addEventListener("click", function () {

    document.getElementById("title").textContent = "The title has been changed!";

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
