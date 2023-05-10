class MenuClass():
    selection = 0
    choices = ["Check login", "Create playlist", "Check available playlists",
                "Delete playlist", "Add video to playlist", "List videos on playlist",
                "Remove video from playlist", "Sync Google Sheets with playlist", "Select playlist to sync",
                "Exit" ]

    def start_menu(self):
        print("Welcome to the YouTube Music Playlist Compiler!")
        while self.selection != 9:
            for x in range(len(self.choices)):
                print(x, ".", self.choices[x])
            print("Enter number")
            self.selection = input()
            self.get_menu_input()
        quit()

    def get_menu_input(self):
        match self.selection:
            case "0":
                # Check login
                quit()
            case "1":
                # Create playlist
                quit()
            case "2":
                # Check available playlists
                quit()
            case "3":
                # Delete playlist
                quit()
            case "4":
                # Add video to playlist
                quit()
            case "5":
                # List videos on playlist
                quit()
            case "6":
                # Remove video from playlist
                quit()
            case "7":
                # Sync Google Sheets with playlist
                quit()
            case "8":
                # Select playlist to sync
                quit()
            case "9":
                print("Exiting")
                quit()
            case _:
                print("Invalid Input")




