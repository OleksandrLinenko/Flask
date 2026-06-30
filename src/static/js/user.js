document.addEventListener("DOMContentLoaded", () => {
    console.log('Content loaded');
    fetch("/api/users")
        .then(function(response) {return response.json()})
//       .then(response => response.json())
        .then(function(users) {
            console.log(users);
            const list = document.getElementById("users");

            list.innerHTML = "";

            users.forEach(user => {

                const li = document.createElement("li");
                li.textContent = user.name;

                list.appendChild(li);

            });

        });
});
