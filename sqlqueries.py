SAVE_EVENT_SQL = u"""
INSERT INTO events (ad_id, event_name, value, ip, user_agent)
VALUES
("{ad_id}", "{event_name}", "{value}", "{ip}", "{user_agent}")
"""
