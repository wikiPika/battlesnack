import os
import random

import cherrypy


class Snack(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # returns persistent snack info
        return {
            "apiversion": "v0.0.1-alpha",
            "author": "wikiPika",
            "color": "#836fbf",
            "head": "shades",
            "tail": "sharp",
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # called at the start of every match, ever
        data = cherrypy.request.json

        print("Snack match has begun!")
        print("Match information:")
        print(data)
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json

        # Choose a random direction to move in
        possible_moves = ["up", "down", "left", "right"]
        move = random.choice(possible_moves)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # called at the end of a match
        data = cherrypy.request.json

        print("Snack match has concluded!")
        print("Postmatch information:")
        print(data)
        return "ok"


if __name__ == "__main__":
    server = Snack()
    cherrypy.config.update(
        {
            "server.socket_host": "0.0.0.0"
        }
    )
    cherrypy.config.update(
        {
            "server.socket_port": int(os.environ.get("PORT", "8080")),
        }
    )
    print("Snack server is initializing...")
    cherrypy.quickstart(server)
