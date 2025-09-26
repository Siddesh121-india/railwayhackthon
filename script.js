
document.getElementById("routeForm").addEventListener("submit", async function(e) {
    e.preventDefault();
    let start = document.getElementById("start").value;
    let end = document.getElementById("end").value;

    const res = await fetch(`http://127.0.0.1:5000/shortest_path?start=${start}&end=${end}`);
    const data = await res.json();

    const resultDiv = document.getElementById("result");
    if (data.error) {
        resultDiv.innerHTML = `<p class="text-danger">${data.error}</p>`;
    } else {
        resultDiv.innerHTML = `<p>Shortest Path: ${data.path.join(" → ")}<br>Distance: ${data.distance} km</p>`;
    }
});
