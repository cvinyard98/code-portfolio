from re import L
import arcade
import time
#number of cells
ROWS = 40
COLS = 50

#cell measurements
WIDTH = 20
HEIGHT = 20

MARGIN = 3

SCREEN_WIDTH = (WIDTH + MARGIN) * COLS + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROWS + MARGIN
SCREEN_TITLE = "Game of Life"


class gameOfLife(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.running = False
        self.grid = []
        for row in range(ROWS):

            self.grid.append([])
            for col in range(COLS):
                self.grid[row].append(0)  

        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        self.grid_sprite_list = arcade.SpriteList()
        #set up default grid
        for row in range(ROWS):
            for col in range(COLS):
                x = col * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)

    def resync_grid_with_sprites(self):
        #redraw all squares with updated colors
        for row in range(ROWS):
            for col in range(COLS):
                pos = row * COLS + col
                if self.grid[row][col] == 0:
                    self.grid_sprite_list[pos].color = arcade.color.WHITE
                else:
                    self.grid_sprite_list[pos].color = arcade.color.YELLOW_ORANGE

    def on_draw(self):

        self.clear()
        self.grid_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        col = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

    #change colors of square that was clicked
        if row < ROWS and col < COLS:
            if self.grid[row][col] == 0:
                self.grid[row][col] = 1
            else:
                self.grid[row][col] = 0

        self.resync_grid_with_sprites()

    def on_key_press(self, symbol: int, modifiers: int):
        #control actions on key press
        if symbol == arcade.key.SPACE:
            self.update_cells()
            self.resync_grid_with_sprites()
        if symbol == arcade.key.C:
            self.clear_grid()
            self.resync_grid_with_sprites()



    def clear_grid(self):
        for i in range(ROWS):
            for j in range(COLS):
                self.grid[i][j] = 0


    def update_cells(self):
        #create result grid so I'm not changing the grid underneath itself
        updates_grid = []
        for row in range(ROWS):
            updates_grid.append([])
            for col in range(COLS):
                updates_grid[row].append(self.grid[row][col]) 
        
        #determines the cell changes to occur after one tick of the clock
        for i in range(ROWS):
            for j in range(COLS):
                neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                living_neigbors = 0
                for k in neighbors:
                    if(0 <= k[0] and k[0] < ROWS and 0 <= k[1] and k[1] < COLS):
                        if self.grid[k[0]][k[1]] == 1:
                            living_neigbors += 1
                if self.grid[i][j] == 1 and (living_neigbors < 2 or living_neigbors > 3):
                    updates_grid[i][j] = 0
                elif living_neigbors == 3:
                    updates_grid[i][j] = 1
    
        for i in range(ROWS):
            for j in range(COLS):
                self.grid[i][j] = updates_grid[i][j]


def main():
    gameOfLife(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()