SAVE_EVENT_SQL = u"""
INSERT INTO events (event_name, client, value, ip, user_agent, gender, email, 
	age_group, ad_id, channel, device)
VALUES
("{event_name}", "{client}", "{value}", "{ip}", "{user_agent}", "{gender}", 
	"{email}", "{age_group}", "{ad_id}", "{channel}", "{device}")
"""
