function getCsrfToken() {
    return document.getElementById('csrf_token').value;
}

function authenticateAndDelete(bookingId) {
    const username = prompt("Please enter your username:");
    const password = prompt("Please enter your password:");

    if (!username || !password) {
        alert("Both username and password are required.");
        return;
    }

    fetch(`/delete_booking/${bookingId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Booking deleted successfully.");
            window.location.reload();  // Reload to show the updated list
        } else {
            alert(data.error || "Something went wrong while deleting the booking.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while deleting the booking. Please try again.");
    });
}

function authenticateAndUpdate(bookingId) {
    const username = prompt("Please enter your username:");
    const password = prompt("Please enter your password:");

    if (!username || !password) {
        alert("Both username and password are required.");
        return;
    }

    const newDate = prompt("Please enter the new date (YYYY-MM-DD):");
    const newTime = prompt("Please enter the new time (HH:MM):");

    if (!newDate || !newTime) {
        alert("Both date and time are required.");
        return;
    }

    fetch(`/update_booking/${bookingId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ username, password, new_date: newDate, new_time: newTime })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Booking updated successfully.");
            window.location.reload();  // Reload to show the updated list
        } else {
            alert(data.error || "Something went wrong while updating the booking.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while updating the booking. Please try again.");
    });
}

// Add event listeners for update and delete buttons
document.querySelectorAll(".delete-button").forEach(button => {
    button.addEventListener("click", function(event) {
        event.preventDefault();
        const bookingId = button.getAttribute("data-booking-id");
        authenticateAndDelete(bookingId);
    });
});

document.querySelectorAll(".update-button").forEach(button => {
    button.addEventListener("click", function(event) {
        event.preventDefault();
        const bookingId = button.getAttribute("data-booking-id");
        authenticateAndUpdate(bookingId);
    });
});
