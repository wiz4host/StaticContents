// Update API URL
const apiUrl = 'http://localhost:5000';

const presentationForm = document.getElementById('addForm');
const presentationList = document.getElementById('presentationList');

// Function to fetch presentations and update the UI
async function fetchPresentations() {
    try {
        const response = await fetch(`${apiUrl}/presentations`);
        const presentations = await response.json();

        console.log(presentations);

        // Clear previous entries
        presentationList.innerHTML = '';

        // Update UI with fetched presentations
        presentations.forEach(presentation => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${presentation.name}</td>
                <td>${presentation.description}</td>
                <td>${presentation.topic}</td>
                <td>${presentation.completed}</td>
                <td>${presentation.date}</td>
                <td><button class="deleteBtn" data-id="${presentation.id}">Delete</button></td>
            `;
            presentationList.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching presentations:', error);
    }
}

// Function to handle form submission
presentationForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const topic = document.getElementById('topic').value;
    const completed = document.getElementById('completed').value;
    const date = document.getElementById('date').value;

    try {
        // Send POST request to API
        const response = await fetch(`${apiUrl}/presentations`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, description, topic, completed, date })
        });

        if (response.ok) {
            // Clear form fields and update presentations
            presentationForm.reset();
            fetchPresentations();
        } else {
            console.error('Failed to add presentation');
        }
    } catch (error) {
        console.error('Error adding presentation:', error);
    }
});

// Function to handle delete button clicks
presentationList.addEventListener('click', async (e) => {
    if (e.target.classList.contains('deleteBtn')) {
        const presentationId = e.target.getAttribute('data-id');

        try {
            // Send DELETE request to API
            const response = await fetch(`${apiUrl}/presentations/${presentationId}`, { method: 'DELETE' });

            if (response.ok) {
                // Update presentations
                fetchPresentations();
            } else {
                console.error('Failed to delete presentation');
            }
        } catch (error) {
            console.error('Error deleting presentation:', error);
        }
    }
});

// Initial fetch and render presentations
fetchPresentations();
