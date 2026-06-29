document.addEventListener("DOMContentLoaded", () => {

    fetch("/api/users")
        .then(response => response.json())
        .then(users => {

            const list = document.getElementById("users");

            list.innerHTML = "";

            users.forEach(user => {

                const li = document.createElement("li");
                li.textContent = user.name;

                list.appendChild(li);

            });

        });

});
