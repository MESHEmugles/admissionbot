from typing import Text
import sqlite3

from rasa.core.tracker_store import TrackerStore
from rasa.shared.core.trackers import DialogueStateTracker
from rasa.shared.core.domain import Domain



class CustomTrackerStore(TrackerStore):
    def __init__(self, domain: Domain) -> None:
        super().__init__(domain)

        # Connect to the database
        self.connection = sqlite3.connect("universitybot.db")
        self.cursor = self.connection.cursor()

        # # Create the table if it doesn't exist
        # self.cursor.execute(
        #     """
        #     CREATE TABLE IF NOT EXISTS chat_logs (
        #         sender_id TEXT,
        #         event_time TEXT,
        #         intent TEXT,
        #         entities TEXT,
        #         slots TEXT,
        #         action TEXT,
        #         action_text TEXT,
        #         input_channel TEXT,
        #         message_id TEXT,
        #         PRIMARY KEY (sender_id, event_time)
        #     )
        #     """
        # )

    def save(self, tracker: DialogueStateTracker) -> None:
        # Extract relevant information from the tracker
        sender_id = tracker.sender_id
        event_time = tracker.latest_message.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        intent = tracker.latest_message.intent.get("name") if tracker.latest_message.intent else None
        entities = tracker.latest_message.entities
        slots = tracker.current_slot_values()
        action = tracker.latest_action_name
        action_text = tracker.latest_message.action_text
        input_channel = tracker.latest_message.input_channel
        message_id = tracker.latest_message.message_id

        # Insert the data into the database
        self.cursor.execute(
            """
            INSERT INTO chat_logs (
                sender_id, event_time, intent, entities, slots,
                action, action_text, input_channel, message_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                sender_id, event_time, intent, entities, slots,
                action, action_text, input_channel, message_id
            )
        )
        self.connection.commit()

    def retrieve(self, sender_id: Text) -> DialogueStateTracker:
        # Retrieve all events for the specified sender_id from the database
        self.cursor.execute(
            """
            SELECT * FROM chat_logs WHERE sender_id = ?
            """,
            (sender_id,)
        )
        events = self.cursor.fetchall()

        # Create a DialogueStateTracker and populate it with the retrieved events
        tracker = DialogueStateTracker(sender_id, self.domain.slots)
        for event in events:
            tracker.update(event)

        return tracker






