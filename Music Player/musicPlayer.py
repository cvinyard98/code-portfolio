import arcade
import arcade.gui
import vlc
import os

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Cameron's Music", resizable=True)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.playing = False
        self.files = os.listdir('.\Music Player\music')
        self.songs = []
        for i in self.files:
            self.songs.append("Music Player\music\\" + i)
        self.player = vlc.MediaPlayer(self.songs[0])
        
        def getNextSong(direction):
            if direction == 1:
                self.songs.append(self.songs[0])
                self.songs.pop(0)
            else:
                self.songs.insert(0, self.songs[len(self.songs) - 1])
                self.songs.pop()
            ui_text_label.text = self.songs[0]

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UITextArea(text="Cameron's MP3 Player",
                                              width=500,
                                              height=40,
                                              font_size=24,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        text = self.songs[0]
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        

        playButton = arcade.gui.UIFlatButton(text="Play", width = 200)

        @playButton.event("on_click")
        def on_click_play(event):
            
            if self.playing:
                self.player.pause()
                playButton.text = "Play"
            else:
                playButton.text = "Pause"
                self.player.play()
            self.playing = not self.playing


        self.v_box.add(playButton.with_space_around(bottom=5))

        nextButton = arcade.gui.UIFlatButton(text=">>", width = 200)

        @nextButton.event("on_click")
        def on_click_play(event):
            self.player.stop()
            getNextSong(1)
            self.player = vlc.MediaPlayer(self.songs[0])
            if self.playing:
                self.player.play()


        self.v_box.add(nextButton.with_space_around(bottom=5))

        backButton = arcade.gui.UIFlatButton(text="<<", width = 200)

        @backButton.event("on_click")
        def on_click_play(event):
            self.player.stop()
            getNextSong(-1)
            self.player = vlc.MediaPlayer(self.songs[0])
            if self.playing:
                self.player.play()

        self.v_box.add(backButton.with_space_around(bottom=20))


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        print("Start:", event)

    def on_draw(self):
        self.clear()
        
        self.manager.draw()
        


window = MyWindow()
arcade.run()