import argparse
import json

from swarm.drone import Drone

def main():
    # Parse Command Line Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", type = str, help = "MQTT Host IP")
    parser.add_argument("-port", type = int, help = "MQTT Port")
    parser.add_argument("config", type = str, help = "Config file", nargs="?", default="./robot_config.json")
    parser.add_argument("-local", action = "store_true")
    parser.add_argument("-verbose", action = "store_true")

    args = parser.parse_args()

    # Ensure that Node Descriptor File can be Opened
    config = None
    try:
        f = open(args.config, 'r')
        config = json.load(f)
        f.close()
    except Exception as e:
        print(repr(e))
        print("Couldn't open config file " + args.config)
        return -1
    
    host = args.host
    port = args.port
    if host == None:
        host = config["host"]
    if port == None:
        port = config["port"]
    connection_string = "/dev/serial/by-id/" + config["device_id"]

    bot = Drone(connection_string, host, port, config["node"], local = args.local, verbose = args.verbose)
    if not args.local:
        bot.add_event_listener("message", execute)
    else:
        bot.add_event_listener("message", test)
    bot.start()

def execute(bot: Drone, message: str):
    """
    Execute MQTT message
    """
    if bot.vehicle.mode.name == "STABLIZE":
        command = json.loads(message)["command"]
        pitch = int(command[0])
        roll = int(command[1])
        yaw = int(command[2])
        speed = int(command[3])
        #bot.stabilized_command(pitch, roll, yaw, speed)
        bot.channel_command(pitch, roll, yaw, throttle = speed)
    elif bot.vehicle.mode.name == "GUIDED":
        command = json.loads(message)["command"]
        lat = command["lat"]
        lon = command["lon"]
        #alt = command["alt"]
        bot.guided_command(lat, lon)

def test(bot: Drone, message: str == ""):
    """
    Testing with empty message
    """
    bot.commandMavLink((0,0,0), 100)

if (__name__ == "__main__"):
    main()