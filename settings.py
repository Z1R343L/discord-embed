import os
import sys

from dotenv import load_dotenv


class Settings:
    description = (
        "Discord will only create embeds for videos and images if they are smaller than 8mb. We can 'abuse' this"
        " by using the 'twitter:image' HTML meta tag."
    )
    # Load environment variables
    load_dotenv()

    # Check if user has added a domain to the environment.
    try:
        domain = os.environ["DOMAIN"]
    except KeyError:
        sys.exit("discord-embed: Environment variable 'DOMAIN' is missing!")

    # We check if the domain ends with a forward slash. If it does, we remove it.
    if domain.endswith("/"):
        domain = domain[:-1]

    # Check if we have a folder for uploads.
    try:
        upload_folder = os.environ["UPLOAD_FOLDER"]
    except KeyError:
        sys.exit("discord-embed: Environment variable 'UPLOAD_FOLDER' is missing!")

    # We check if the upload folder ends with a forward slash. If it does, we remove it.
    if upload_folder.endswith("/"):
        upload_folder = upload_folder[:-1]
