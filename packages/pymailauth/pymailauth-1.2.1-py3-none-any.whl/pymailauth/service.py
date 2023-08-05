import base64
from email.mime.text import MIMEText
import logging
import os

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .consts import SCOPES

log = logging.getLogger(__name__)


class Service:
    def __init__(self, credential_file_path, token_file_path):
        self.cred_fp = credential_file_path
        self.token_fp = token_file_path

    def authorize(self, credentials_file_path, token_file_path, SCOPES):
        """Shows basic usage of authorization"""
        # based on https://developers.google.com/people/quickstart/python
        try:
            credentials = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists(token_file_path):
                try:
                    credentials = Credentials.from_authorized_user_file(
                        token_file_path, SCOPES
                    )
                    credentials.refresh(Request())
                except RefreshError as error:
                    # if refresh token fails, reset creds to none.
                    credentials = None
                    log.error(f"An refresh authorization error occurred: {error}")
            # If there are no (valid) credentials available, let the user log in.
            if not credentials or not credentials.valid:
                if credentials and credentials.expired and credentials.refresh_token:
                    credentials.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_file_path, SCOPES
                    )
                    credentials = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(token_file_path, "w") as token:
                    token.write(credentials.to_json())
        except HttpError as error:
            log.error(f"An authorization error occurred: {error}")

        return credentials

    def create_service(
        self,
    ):
        credentials = self.authorize(self.cred_fp, self.token_fp, SCOPES)
        service = build("gmail", "v1", credentials=credentials)
        return service

    def create_message_body(self, to, subject, body):
        message = MIMEText(body)
        message["to"] = to
        message["subject"] = subject
        return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def send_email(self, to, subject, body):
        service = self.create_service()
        create_message = self.create_message_body(to, subject, body)
        try:
            message = (
                service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            log.info(f'sent message to {message} Message Id: {message["id"]}')
        except HttpError as error:
            log.error(f"An error occurred: {error}")
            message = None
        return message
