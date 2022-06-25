import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


CLIENT_SECRET_FILE = "Gmail/client_id.json"
API_SERVICE_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

token_file = "Gmail/token.json"

def Create_Service():
    creds = None
    # Se verifica si existen credenciales para acceder a la cuenta (es decir, si ya se ha accedido antes)
    if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    # Si las credenciales no son válidas o no existen, el usuario se loggea
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=5004)

        # Se guardan las credenciales para la próxima vez que se acceda
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    try: 
        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
        print("Servicio creado")
        return service
    except Exception:
        print(Exception)
        print("No se creó el servicio")
        os.remove(token_file)
        return None

def send_token_email(token, to_email):
    service = Create_Service()

    html_message = f"""\
        <html>
            <head></head>
            <body>
                <h1>Bienvenido a Ginyu Sports API!</h1>
                <img src="https://i.imgur.com/cz7kcAn.png" alt="logo">
                <p>Este es tu token único para ingresar a la API:<br> {token}</p>
            </body>
        </html>
        """

    # MIME = Multipurpose Internet Mail Extensions - formato estándar para correos
    mimeMessage = MIMEMultipart()
    mimeMessage["to"] = to_email
    mimeMessage["subject"] = "Bienvenido a Ginyu Sports API!"
    mimeMessage.attach(MIMEText(html_message, "html"))

    encoded_message = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    create_message = {
        'raw': encoded_message
    }

    email = service.users().messages().send(userId="me", body=create_message).execute()

    return email


if __name__ == "__main__":
    send_token_email("pruebas", "grover.ugarte@utec.edu.pe")