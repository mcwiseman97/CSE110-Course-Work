function updateBoard(board) {
    for (const [cellId, value] of Object.entries(board)) {
        const cellInfo = document.getElementById(cellId);
        cellInfo.textContent = value;
        cellInfo.className = 'cell'; // Reset classes
        if (value === 'X') {
            cellInfo.classList.add('x');
        } else if (value === 'O') {
            cellInfo.classList.add('o');
        }
    }
}

function updateStatus(winner, draw, currentPlayer) {
    const statusEl = document.getElementById('status');
    if (winner) {
        statusEl.textContent = `Player ${winner} Wins!`;
        startConfetti();
    } else if (draw) {
        statusEl.textContent = "It's a Draw!";
    } else {
        statusEl.textContent = `Player ${currentPlayer}'s Turn`;
    }
}

async function makeMove(cellId) {
    const response = await fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cell: cellId }),
    });
    
    const data = await response.json();
    
    if (data.status === 'success') {
        updateBoard(data.board);
        updateStatus(data.winner, data.draw, data.current_player);
    } else if (data.status === 'game_over') {
        // Game is already over, maybe shake the board or something
    }
}

async function resetGame() {
    const response = await fetch('/reset', {
        method: 'POST'
    });
    const data = await response.json();
    if (data.status === 'reset') {
        // Clear board visually
        document.querySelectorAll('.cell').forEach(cell => {
            cell.textContent = '';
            cell.className = 'cell';
        });
        document.getElementById('status').textContent = "Player X's Turn";
        stopConfetti(); 
    }
}

// Simple confetti effect placeholder - in a real app, I'd use a library like canvas-confetti
function startConfetti() {
    // For now, just change the status text color dynamically or add an emoji to show celebration
    const statusEl = document.getElementById('status');
    statusEl.innerHTML += " 🎉";
}

function stopConfetti() {
    // Valid reset
}

// Load initial state
window.onload = async () => {
    const response = await fetch('/state');
    const data = await response.json();
    updateBoard(data.board);
    updateStatus(data.winner, data.draw, data.current_player);
};
