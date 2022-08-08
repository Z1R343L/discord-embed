import os

from discord_embed.generate_html import generate_html_for_videos


def test_generate_html_for_videos():
    """Test generate_html_for_videos() works."""
    domain = os.environ["SERVE_DOMAIN"]

    # Remove trailing slash from domain
    if domain.endswith("/"):
        domain = domain[:-1]

    # Delete the old HTML file if it exists
    if os.path.exists(f"Uploads/test_video.mp4.html"):
        os.remove(f"Uploads/test_video.mp4.html")

    generated_html = generate_html_for_videos(
        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        width=1920,
        height=1080,
        screenshot="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
        filename="test_video.mp4",
    )
    assert generated_html == f"{domain}/test_video.mp4"

    # Open the generated HTML and check if it contains the correct URL, width, height, and screenshot.

    with open("Uploads/test_video.mp4.html", "r") as generated_html_file:
        generated_html_lines = generated_html_file.readlines()
        """
        <!DOCTYPE html>
        <html>
        <!-- Generated at 2022-08-08 08:16:53 -->
        <head>
            <meta property="og:type" content="video.other">
            <meta property="twitter:player" content="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
            <meta property="og:video:type" content="text/html">
            <meta property="og:video:width" content="1920">
            <meta property="og:video:height" content="1080">
            <meta name="twitter:image" content="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg">
            <meta http-equiv="refresh" content="0;url=https://www.youtube.com/watch?v=dQw4w9WgXcQ">
        </head>
        </html>
        """

        for line, html in enumerate(generated_html_lines):
            # Strip spaces and newlines
            html = html.strip()

            # Check each line
            if line == 1:
                assert html == "<!DOCTYPE html>"
            elif line == 2:
                assert html == "<html>"
            elif line == 3:
                assert html.startswith("<!-- Generated at ")
            elif line == 4:
                assert html == '<head>'
            elif line == 5:
                assert html == '<meta property="og:type" content="video.other">'
            elif line == 6:
                assert html == '<meta property="twitter:player" content="https://www.youtube.com/watch?v=dQw4w9WgXcQ">'
            elif line == 7:
                assert html == '<meta property="og:video:type" content="text/html">'
            elif line == 8:
                assert html == '<meta property="og:video:width" content="1920">'
            elif line == 9:
                assert html == '<meta property="og:video:height" content="1080">'
            elif line == 10:
                assert html == '<meta name="twitter:image" content="https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg">'
            elif line == 11:
                assert html == '<meta http-equiv="refresh" content="0;url=https://www.youtube.com/watch?v=dQw4w9WgXcQ">'
            elif line == 12:
                assert html == "</head>"
            elif line == 13:
                assert html == "</html>"
