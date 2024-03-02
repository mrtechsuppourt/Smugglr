function fetchAndDisplayTracks() {
    const playlistInput = document.getElementById('playlistInput');
    const playlistTracks = document.getElementById('playlistTracks');

    // Clear previous results
    playlistTracks.innerHTML = '';

    const playlistURI = playlistInput.value.trim();

    if (!playlistURI) {
        alert('Please enter a valid Spotify Playlist URI');
        return;
    }

    // Fetch tracks using Spotify API
    fetch(`/api/getPlaylistTracks?uri=${encodeURIComponent(playlistURI)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(`Error: ${data.error.message}`);
            } else {
                displayTracks(data.tracks);
            }
        })
        .catch(error => {
            console.error('Error fetching playlist tracks:', error);
            alert('An error occurred while fetching playlist tracks. Please try again.');
        });
}

function displayTracks(tracks) {
    const playlistTracks = document.getElementById('playlistTracks');

    tracks.forEach(track => {
        const li = document.createElement('li');
        li.textContent = `${track.name} - ${track.artists.map(artist => artist.name).join(', ')}`;
        playlistTracks.appendChild(li);
    });
}
