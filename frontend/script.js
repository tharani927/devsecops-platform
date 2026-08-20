async function checkBackend() {

    const status = document.getElementById("status");

    status.textContent = "Checking backend...";

    try {

        const response = await fetch("http://localhost:8000/health");

        if (response.ok) {
            status.textContent = "Backend is healthy ✓";
        } else {
            status.textContent = "Backend returned an error";
        }

    } catch (error) {

        status.textContent = "Backend is unavailable";

    }
}


async function loadDeployments() {

    const container = document.getElementById("deployments");

    container.innerHTML = "Loading deployments...";

    try {

        const response = await fetch("http://localhost:8000/deployments/");

        if (!response.ok) {
            throw new Error("Failed to load deployments");
        }

        const deployments = await response.json();

        if (deployments.length === 0) {

            container.innerHTML = "<p>No deployments found.</p>";

            return;
        }


        let html = `
            <table class="deployment-table">

                <thead>
                    <tr>
                        <th>Project</th>
                        <th>Environment</th>
                        <th>Version</th>
                        <th>Status</th>
                        <th>Security</th>
                    </tr>
                </thead>

                <tbody>
        `;


        deployments.forEach(deployment => {

            html += `
                <tr>

                    <td>${deployment.project_name}</td>

                    <td>${deployment.environment}</td>

                    <td>${deployment.version}</td>

                    <td>${deployment.status}</td>

                    <td>${deployment.security_status}</td>

                </tr>
            `;

        });


        html += `
                </tbody>

            </table>
        `;


        container.innerHTML = html;

    } catch (error) {

        console.error(error);

        container.innerHTML =
            "<p>Unable to load deployment data.</p>";

    }
}


window.onload = function () {

    checkBackend();

    loadDeployments();

};
document.getElementById("deploymentForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const message = document.getElementById("deploymentMessage");

    const deployment = {
        project_name: document.getElementById("projectName").value,
        environment: document.getElementById("environment").value,
        version: document.getElementById("version").value,
        status: document.getElementById("deploymentStatus").value,
        security_status: document.getElementById("securityStatus").value
    };

    try {

        const response = await fetch("http://localhost:8000/deployments/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(deployment)

        });

        if (!response.ok) {
            throw new Error("Failed to create deployment");
        }

        message.textContent = "Deployment created successfully ✓";

        document.getElementById("deploymentForm").reset();

        loadDeployments();

    } catch (error) {

        console.error(error);

        message.textContent = "Failed to create deployment.";

    }

});