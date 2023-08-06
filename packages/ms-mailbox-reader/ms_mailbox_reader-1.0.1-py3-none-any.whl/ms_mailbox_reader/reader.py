import re
from typing import Generator
import win32com.client
from datetime import datetime, timedelta


class MessageFilter:
    """
    A class to represent an email message filter.

    Attributes:
        sender_email (str): The email address of the message sender.
        subject (str): The subject of the message.
        received_since (timedelta): The time period since which the message was received.
        message_class (str): The message class of the email message. Default is 'IPM.Note'.
        limit (int): The maximum number of messages to retrieve. Default is 10.

    Methods:
        render(): Returns the filter string to be used to retrieve email messages based on the filter attributes.
    """

    def __init__(self, sender_email: str = None,
                 subject: str = None,
                 received_since: timedelta = None,
                 message_class: str = 'IPM.Note',
                 limit: int = 10):
        """
        Initializes a MessageFilter object.

        Args:
            sender_email (str, optional): The email address of the message sender. Default is None.
            subject (str, optional): The subject of the message. Default is None.
            received_since (timedelta, optional): The time period since which the message was received.
            message_class (str, optional): The message class of the email message. Default is 'IPM.Note'.
            limit (int, optional): The maximum number of messages to retrieve. Default is 10.
        """
        self.sender_email = sender_email
        self.subject = subject
        self.received_since = received_since
        self.message_class = message_class
        self.limit = limit

    def render(self) -> str:
        """
        Returns the filter string to be used to retrieve email messages based on the filter attributes.

        Returns:
            str: The filter string for retrieving email messages.
        """
        filter_parts = []
        if self.received_since:
            received_since_str = self.received_since.strftime(
                '%m/%d/%Y %H:%M %p')
            filter_parts.append(f"[ReceivedTime] >= '{received_since_str}'")
        if self.message_class:
            filter_parts.append(f"[MessageClass] = '{self.message_class}'")
        return ' AND '.join(filter_parts)


class SimpleMessage:
    """
    A class to represent an email message.

    Attributes:
        sender_name (str): The name of the message sender.
        subject (str): The subject of the message.
        date (datetime): The date and time the message was received.
        body (str): The content of the message body.
        conversation_id: None

    """

    def __init__(self, sender_name: str, subject: str, date: datetime, body: str):
        """
        Initializes a SimpleMessage object.

        Args:
            sender_name (str): The name of the message sender.
            subject (str): The subject of the message.
            date (datetime): The date and time the message was received.
            body (str): The content of the message body.
        """
        self.sender_name = sender_name
        self.subject = subject.strip()
        self.date = date
        self.body = body.strip()
        self.conversation_id = None


class MsOutlookMessageReader:
    @staticmethod
    def __extract_content_before_from_pattern(message_body: str) -> str:
        """
        Extracts the latest unique message from a message body by removing all
        previous responses and duplicated message history.

        Args:
            message_body (str): The message body to extract the content from.

        Returns:
            str: The original content of the message before any replies or previous messages were included.
        """

        pattern = r"From: .*?<.*?>"
        match = re.search(pattern, message_body)

        if match:
            end_index = match.start()
            text_before_match = message_body[:end_index]
        else:
            text_before_match = message_body

        return text_before_match

    @staticmethod
    def __get_default_message_filter() -> MessageFilter:
        return MessageFilter(limit=10)

    def get_outlook_messages(self, message_filter: MessageFilter = None) -> Generator[SimpleMessage, None, None]:
        """
        Returns a generator of SimpleMessage objects from emails that match the given message filter.

        Args:
            message_filter (MessageFilter, optional): A MessageFilter object to filter the messages by.
                If None, a default filter is used to get the last 10 messages.

        Yields:
            SimpleMessage: A SimpleMessage object representing a single email message.

        Raises:
            AttributeError: If the message filter object is invalid or missing required attributes.
            pywintypes.com_error: If there is an error accessing the Outlook application or inbox.
        """

        outlook = win32com.client.Dispatch(
            "Outlook.Application").GetNamespace("MAPI")

        # Get the default Inbox folder
        inbox = outlook.GetDefaultFolder(6)  # 6 represents the Inbox folder

        message_filter = message_filter or MsOutlookMessageReader.__get_default_message_filter()

        # Get all messages that match the filter
        messages = inbox.Items.Restrict(message_filter.render())
        messages.Sort("[ReceivedTime]", True)

        message_counter = 0
        for message in messages:
            if message_counter >= message_filter.limit:
                break

            sender_email = message.SenderEmailAddress
            subject = message.Subject

            if message_filter.sender_email and message_filter.sender_email not in sender_email:
                continue

            if message_filter.subject and message_filter.subject not in subject:
                continue

            original_message_content = MsOutlookMessageReader.__extract_content_before_from_pattern(
                message.Body)

            yield SimpleMessage(message.SenderName, subject, message.ReceivedTime, original_message_content)

            message_counter += 1
