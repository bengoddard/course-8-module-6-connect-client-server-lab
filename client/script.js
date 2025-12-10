fetch("http://127.0.0.1:5000/events")
    .then(response => response.json())
    .then(events => {
        events.forEach(renderEvent);
    });

document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    const title = document.querySelector("#title").value;

    fetch("http://127.0.0.1:5000/events", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title })
    })
        .then(response => response.json())
        .then(renderEvent);
});

function renderEvent(event) {
    const li = document.createElement("li");
    li.textContent = event.title;
    document.querySelector("#event-list").appendChild(li);
}