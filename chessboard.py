# Generating the chess board

import numpy as np
import matplotlib.pyplot as plt

board_size = 64
block_size = 8
chessboard = np.ones((board_size, board_size)) #array of ones
for i in range(board_size):
    for j in range(board_size):
        if (i // block_size) % 2 == (j // block_size) % 2:
            chessboard[i, j] = 0 #assigning value of zeros

# Displaying the chess board

plt.imshow(chessboard, cmap='binary')
plt.axis('off')
plt.savefig('chessboard.png')
